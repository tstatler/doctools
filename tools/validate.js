var yaml = require('js-yaml'),
    fs = require('fs'),
    colors = require('colors'),
    basePath = '.',
    doc = {},
    parseErrors = [],
    currentFile = '',
    errorCount = 0,
    classKeys = ['base-url', 'description', 'fields', 'methods', 'mixin', 'name', 'private', 'pseudo'],
    requiredClassKeys = ['description', 'methods', 'name' ],
    requiredPseudoKeys = ['description', 'fields', 'name'],
    methodKeys = ['admin-required', 'description', 'examples', 'http-method', 'login-required', 'name',
                  'parameters', 'response-parameters', 'summary', 'url'];
    requiredMethodKeys = ['description', 'examples', 'name', 'url'],
    fieldKeys = ['description', 'name', 'required', 'type'],
    requiredFieldKeys = ['description', 'name', 'type'],
    dataTypes = ['Any', 'BinaryData', 'Boolean', 'Date', 'FileUpload', 'Hash', 'Number', 'String'],
    platforms = ['android', 'ios', 'rest', 'titanium'];

// Recursively find, load and parse YAML files
function recurseSearch (path) {
    try {
        var fsArray = fs.readdirSync(path);
        fsArray.forEach(function(fsElement) {
            var elem = path + '/' + fsElement,
                stat = fs.statSync(elem);
            currentFile = elem;
            if (stat.isDirectory()) {
                recurseSearch(elem);
            }
            else if (stat.isFile()) {
                if (elem.split('.').pop() == 'yml') {
                    var data = yaml.safeLoad(fs.readFileSync(elem, 'utf8'));
                    // data does not exist in doc
                    if (doc[data.name] == null) {
                        doc[data.name] = data;
                    }
                    // data is a method
                    else if ("methods" in data) {
                        if ("methods" in doc[data.name]) {
                            doc[data.name]["methods"].push(data.methods.pop());
                        } else {
                            doc[data.name]["methods"] = data.methods;
                        }
                    } else {
                        for (key in data) {
                            if (key in doc[data.name]) {
                                console.log("WARNING: Duplicate key: %s".yellow, data.name + "." + key);
                            }
                            doc[data.name][key] = data.key;
                        }
                    }
                }
            }
        });
    }
    catch (e) {
        if ("message" in e) {
            parseErrors.push('File: ' +  currentFile + '\n' + e.message);
        } else {
            console.log('%s'.red, e);
        }
    }
}

// Validate array of keys against the object
function validateArray(array, obj) {
    var errors = [];
    array.forEach(function(elem){
        if (!(elem in obj)) {
            errors.push(elem);
        } 
    });
    return errors;
};

// Validate platforms in method
function validateExamples(method) {
    var exPlatforms = [], errors = [];
    method.examples.forEach(function(example) {
        exPlatforms.push(example.platform);
    });
    platforms.forEach(function(platform) {
        if (exPlatforms.indexOf(platform) > -1) {
            return;
        } else {
            errors.push(platform);
        }
    });
    return errors;
};

// Validate field or parameter data types
function validateType (t) {
    var errors = [];
    if(Array.isArray(t)) { 
        t.forEach(function(elem) {
            errors.join(validateType(elem));
        });
    }
    else if (t.indexOf('Array') == 0) {
        errors.join(validateType(t.slice(6, -1)));
    }
    else if (t.indexOf(',') > 0) {
        var array = t.split(',');
        array.forEach(function(elem) {
            errors.join(validateType(elem));
        });
    }
    else if (t in doc || (dataTypes.indexOf(t) > -1)) {
        return errors;
    }
    else { 
        errors.push(t);
    }
    return errors;
};

// Validate class fields or method parameters
function validateFields(fields) {
    var errors = [];
    fields.forEach(function(field) {
        var err = {
            invalidKeys: [],
            missingKeys: [],
            name: field.name,
            types: []
        };

        for (key in field) {
           if (fieldKeys.indexOf(key) == -1) {
               err.invalidKeys.push(key);
           } else {
               switch (key) {
                   case "type":
                       err.types = validateType(field.type);
                       break;
                   default:
                       break;
               }
           }
        }
        err.missingKeys = validateArray(requiredFieldKeys, field);

        if (err.missingKeys.length + err.invalidKeys.length + err.types.length > 0) {
            errors.push(err);
        }
    });
    return errors;
};

// Validate class methods
function validateMethods(methods) {
    var errors = [];
    methods.forEach(function(method) {
        var err = {
            examples: [],
            invalidKeys: [],
            missingKeys: [],
            name: method.name,
            parameters: [],
            responseParameters: [],
        };
        for (key in method) {
            if (methodKeys.indexOf(key) == -1) {
                err.invalidKeys.push(key);
            } else {
                switch (key) {
                    case "examples":
                        err.examples = validateExamples(method);
                        break;
                    case "parameters":
                        err.parameters = validateFields(method.parameters);
                        break;
                    case "response-parameters":
                        err.responseParameters = validateFields(method['response-parameters']);
                        break;
                    default:
                        break;
                }
            }
        }
        err.missingKeys = validateArray(requiredMethodKeys, method);
        if (err.examples.length + err.missingKeys.length + err.invalidKeys.length + err.parameters.length + err.responseParameters.length > 0) {
            errors.push(err);
        }        
    });
    return errors;
};

// Process and output syntax errors to the console
function outputErrors (errors) {
    var str = errors.name;

    errorCount += errors.missingKeys.length + errors.invalidKeys.length;

    errors.missingKeys.forEach(function(key){
        str += '\n\tmissing class key: ' + key; 
    });

    errors.invalidKeys.forEach(function(key){
        str += '\n\tinvalid class key: ' + key;
    });

    errors.fields.forEach(function(field){
        errorCount += field.missingKeys.length + field.invalidKeys.length + field.types.length;

        str += '\n\t' + field.name + ' (field):';

        field.missingKeys.forEach(function(key){
            str += '\n\t\tmissing field key: ' + key; 
        });

        field.invalidKeys.forEach(function(key){
            str += '\n\t\tinvalid field key: ' + key; 
        });
        field.types.forEach(function(key){
            str += '\n\t\tinvalid type: ' + key; 
        });
    });

    errors.methods.forEach(function(method) {
        errorCount += method.missingKeys.length + method.invalidKeys.length + method.examples.length;

        str += '\n\t' + method.name + ' (method):';

        method.missingKeys.forEach(function(key){
            str += '\n\t\tmissing method key: ' + key; 
        });
        method.invalidKeys.forEach(function(key){
            str += '\n\t\tinvalid method key: ' + key;
        });
         method.examples.forEach(function(key){
            str += '\n\t\tmissing example for platform: ' + key;
        });
        method.parameters.forEach(function(param){
            errorCount += param.missingKeys.length + param.invalidKeys.length + param.types.length;
            str += '\n\t\t' + param.name + ' (method parameter):';
            param.missingKeys.forEach(function(key){
                str += '\n\t\t\tmissing parameter key: ' + key;
            });
            param.invalidKeys.forEach(function(key){
                str += '\n\t\t\tinvalid parameter key: ' + key;
            });
            param.types.forEach(function(key){
                str += '\n\t\tinvalid parameter type: ' + key;
            });
        });
        method.responseParameters.forEach(function(param){
            errorCount += param.missingKeys.length + param.invalidKeys.length + param.types.length;
            str += '\n\t\t' + param.name + ' (method response-parameter):';
            param.missingKeys.forEach(function(key){
                str += '\n\t\t\tmissing parameter key: ' + key;
            });
            param.invalidKeys.forEach(function(key){
                str += '\n\t\t\tinvalid parameter key: ' + key;
            });
            param.types.forEach(function(key){
                str += '\n\t\tinvalid parameter type: ' + key;
            });
        });
    });

    if (str == errors.name) {
        console.log("%s: OK".green, str)
    } else {
        console.log("%s".red, str);
    }
}

// Start of Main Flow
// Check environment
if (process.env.TI_ROOT == null) {
    console.log('TI_ROOT not defined! Set TI_ROOT to the parent directory of the cloud_docs repo.'.red);
    process.exit(1);
} else {
    basePath = process.env.TI_ROOT + '/cloud_docs/apidoc';
    if (!fs.existsSync(basePath)) {
        console.log('ERROR: Could not locate cloud_docs repo at %s.\nMake sure TI_ROOT is set to the parent directory of the repo.'.red, basePath);
        process.exit(1);
    }
}

// Load YAML files
recurseSearch(basePath);
if (doc == null) {
    console.log('ERROR: Could not find YAML files in %s.'.red, basePath);
    process.exit(1);
}

// Validate YAML
for (key in doc) {
    var cls = doc[key],
        syntaxErrors = {
            fields: [],
            invalidKeys: [],
            methods: [],
            missingKeys: [],
            name: cls.name
        };
    for (key in cls) {
       if (classKeys.indexOf(key) == -1) {
              syntaxErrors.invalidKeys.push(key);
       } else {

           switch (key) {
               case "fields":
                   syntaxErrors.fields = validateFields(cls.fields);
                   break;
               case "methods":
                   syntaxErrors.methods = validateMethods(cls.methods);
                   break;
               default:
                   break;
           }
        }
    }

    if (("pseudo" in cls && cls.pseudo == true) ||
        ("private" in cls && cls.private == true)) {

        syntaxErrors.missingKeys = validateArray(requiredPseudoKeys, cls);
    }
    else {
        syntaxErrors.missingKeys = validateArray(requiredClassKeys, cls);
    }

    outputErrors(syntaxErrors);
}

if (errorCount > 0) {
    console.log("Found %s errors.".yellow, errorCount);
}

// Output exceptions while parsing YAML files
if (parseErrors.length > 0) {
    console.log("The following files have errors: ".red);
    parseErrors.forEach(function(err) {
        console.log("%s".red, err);
    });
}

// Return error code if we found errors or handled exceptions
if (parseErrors.length + errorCount > 0) process.exit(1);
