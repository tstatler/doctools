# Application Configuration File

A Node.ACS application contains a file called `package.json` located in the root directory of the
project.  A Node.ACS application uses the `package.json` file to configure settings for the
application.

Important fields for Node.ACS applications are defined below and may be different from
the [npm version](https://www.npmjs.org/doc/files/package.json.html).
The only required fields are `name`, `version`, `framework` and `main`.  For standard Node.js
applications, you may specifiy `scripts` instead of `main`.

The file below describes a basic configuration for a Node.ACS application:
    
    {
      "name": "MyNodeACSApp",
      "main": "app.js",
      "framework": "mvc",
      "version": "0.1.0",
      "description": "My first Node.ACS MVC App!",
      "author":"bob@appcelerator.com",
      "dependencies": {
        "mongodb": ">1.2.0"
      },
      "npmRegistry": "http://registry.npmjs.org/",
      "engines" : { "node": "0.10.22" }
    }

## dependencies

The application can import any third-party modules that are supported by
standard Node.js applications. Before publishing the app to the cloud, make sure
all dependencies are listed in the `dependencies` field in the application's
`package.json` file.  For example, to add support for MongoDB 1.2.0 or greater:

    "dependencies":{
      "mongodb": ">1.2.0"
    }

## engines

You can specify which version of Node.js to run your application on.  Use the `engines` field in
`package.json` to specify engine versions.  To specify the Node.js version, set the `node` key in
the `engines` dictionary to either a version or [version range](https://github.com/isaacs/node-semver)
of Node.js to use. For example, to specify to use version 0.10.22 or greater:

    "engines" : { "node": ">=0.10.22" }

If this field is undefined when you publish your application, the latest supported Node.js version
is used.  The current supported version is 0.10.22.

If this field is undefined when you republish your application and the latest supported Node.js
version changed on the ACS servers, you will receive an error message when trying to publish your
application. You must set the Node.js version to republish your application.


## framework

**Required.**

The application can use either an [MVC framework](#!/guide/node_mvc) or no framework and run as a
[standard Node application](#!/guide/node_standard).

Use the `framework` field to select the framework to use.  Set to either `mvc` to use the MVC
framework or `none` to use no framework and run as a standard Node application.

    "framework": "mvc"

By default, when you create a new Node.ACS application, it includes the Node.ACS MVC framework.


## main

**Required.**

Node.ACS uses the `main` field in `package.json` to determine the application's main entry point.
Set this field to a JavaScript file. Node.ACS loads and runs this file first.

By default, the `main` field is set to the `app.js` file located in the project's root folder:

    "main": "app.js"

For standard Node.ACS applications, you can load a module by leaving this field blank and specifying
the `scripts` field.


## name

**Required.**

Use the `name` field to specify the name of app. An app's name is unique across all the apps of a
user or organization. It will be used to ID the app when publishing/unpublishing to cloud, or setup
the app through CLI commands.

By default, this field is set to the name of the project when it was created.

    "name": "MyNodeAcsApp"


## npmRegistry

If you want to use a different npm registry besides the official public npm registry to install
dependencies, add the `npmRegistry` field to the `package.json` and set the value to the
registry URL you want to use.  For example, the entry below uses a European npm mirror:

    "npmRegistry" : "http://registry.npmjs.eu/"


## scripts

If your application's `package.json` file does not specify a `main` field, Node.ACS will now look at
the `scripts.start` field in `package.json` to determine the main module to launch.  Node.ACS will
execute the start script using `npm start`. This feature is only available to standard Node.js
applications, not those that use the MVC framework.

See the [NPM documentation](https://www.npmjs.org/doc/misc/npm-scripts.html) on the "scripts"
package.json field.

For example, to launch the foo module:

    "scripts": {
      "start": "foo"
    }

## version

**Required.**

Version of the application. Used to version the application.

By default, this field is set to `0.1.0`:

    "version": "0.1.0"

