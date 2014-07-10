
# Standard Node.js Applications

Node.ACS supports running applications built with standard Node.js. Any
application that can be started and run with the **node** command can be run seamlessly as a
Node.ACS application. However, there are some things that you need to bear in
mind when working with Node.ACS.

## Application Settings (package.json)

By default, when you create a new Node.ACS application, it
includes the Node.ACS MVC framework.

To run your app as a pure Node.js application without the MVC framework , edit the 
`package.json` file and change: 
    
    "framework": "mvc",

To:

    "framework": "none",

(For details on the MVC framework, see [Node.ACS MVC Framework](#!/guide/mvc).)

## Starting Point

For an application that is configured as a pure node.js application, Node.ACS
uses the `main` field in `package.json` to determine the application's main entry point.

For example, in `package.json`, the main field is defined as:

    "main": "app.js"

In this case, `/app.js` is first file loaded and run by Node.ACS when the
"run" command is executed to start the app locally, or when running the app in
the cloud.

If your application's `package.json` file does not specify a `main` field, Node.ACS will now look at
the `scripts.start` field in `package.json` to determine the main module to launch.  Node.ACS will
execute start script using `npm start`. This feature is only available to standard Node.js applications,
not those that use the MVC framework.

You also need to set your application's port number to 8080.  You can either add a `service.port` field to
your `package.json` file or set the `port` environment variable:

    acs config --set port=8080

See the [NPM documentation](https://www.npmjs.org/doc/misc/npm-scripts.html) on the "scripts" package.json field.


## Node.js Engine

You can specify which version of Node.js to run your application on.  Use the `engines` field in
`package.json` to specify engine versions.  To specify the Node.js version, set the `node` key in
the `engines` dictionary to either a version or [version range](https://github.com/isaacs/node-semver)
of Node.js to use. For example, to specify to use version 0.10.22 or greater:

    "engines" : { "node": ">=0.10.22" }

If this field is undefined when you publish your application, the latest supported Node.js version is
used.  The current supported version is 0.10.22.

If this field is undefined when you republish your application and the latest supported Node.js version
changed on the ACS servers, you will receive an error message when trying to publish your application.
You must set the Node.js version to republish your application.


## Module Dependencies

The application can import any third-party modules that are supported by
standard node.js. Before publishing the app to the cloud, make sure
all dependencies are listed in the `dependencies` field in the application's
`package.json` file.

If you want to use a different npm registry besides the official public npm registry to install
dependencies, add the `npmRegistry` field to the `package.json` and set the value to the
registry URL you want to use.  For example, the entry below uses a European npm mirror:

    "npmRegistry" : "http://registry.npmjs.eu/"

## Third-Party Tools

The ACS servers include support for third-party tools, specifically ImageMagick and PhantomJS.

To use these tools, add the [imagemagick](https://www.npmjs.org/package/imagemagick),
[phantom](https://www.npmjs.org/package/phantom) and
[phantomjs](https://www.npmjs.org/package/phantomjs) node modules as dependencies of the
application:

    {
      "name": "FooApp",
      "version": "0.1.0",
      "framework": "none",
      "main": "app.js",
      "dependencies": {
         "imagemagick" : "*",
         "phantom" : "*",
         "phantomjs" : "*"
      },
    }

Once you have added these modules as depedencies, use `require()` to access it from JavaScript, then
use the module references to make API calls:

    var imagemagick = require('imagemagick');

    imagemagick.identify('favicon.ico', function(err, features) {
        if (err)
            throw err;
        console.log(features["image statistics"]);
    });

## Server Listening Port Limitation

Currently, Node.ACS only supports applications opening one server listening
port, there cannot be more than one TCP/HTTP server started in one
application.

## Migrating Existing Node.js Applications to Node.ACS

If you already have a node.js application and would like to run it on Node.ACS
cloud, the migration process is simple: 

1.  Login to Node.ACS by running the following command:
   
        acs login
     
    When prompted, enter your account credentials.

2.  Edit the `package.json` file in the in application folder. If the file doesn't
    exist, create it.

    Add or modify the `main` property. Set it to the path of your app's 
    main script, relative to the application folder.

    Add or modify the `framework` property. Set the value to "none".

        "main": "app.js",
        "framework": "none",

3.  Publish the application by running the following command:

        acs publish

    If prompted to create a new Node.ACS app before continuing, answer "yes".

That's it! Your application is running in the Node.ACS cloud.

