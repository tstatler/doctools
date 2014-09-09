
# Standard Node.js Applications

Node.ACS supports running applications built with standard Node.js. Any
application that can be started and run with the **node** command can be run seamlessly as a
Node.ACS application. However, there are some things that you need to bear in
mind when working with Node.ACS.

See [Application Limitations](#!/guide/node_limitations) for a list of known application limitations.

## Application Settings (package.json)

By default, when you create a new Node.ACS application using the `acs new` command, it includes the
[Node.ACS MVC Framework](#!/guide/node_mvc). 
To create an application without the MVC framework, pass `--framework none` as a parameter
to `acs new`:

    acs new --framework none

To convert an MVC-based Node.ACS application to a standard Node.js application,
open the application's `package.json` file and remove the following line:
    
    "framework": "mvc"

If package.json doens't include a `framework` field, the application is assumed to be a standard 
Node.js application. Equivalently, you can set the "framework" field to "none":

    "framework": "none"

## Starting Point

For standard Node.js applications, Node.ACS uses either the `main` or
`scripts.start` field in `package.json` to determine the application's main
entry point. For example, suppose that the main field is defined as follows in `package.json`, :

    {
      "name": "node-js-sample-app",
      "version": "0.1.0",
      "main": "app.js"
    }

In this case, `/app.js` is first file loaded and run by Node.ACS when the
"run" command is executed to start the app locally, or when running the app in
the cloud.

If your application's `package.json` file does not specify a `main` field, Node.ACS checks
the `scripts.start` field in `package.json` to determine the main module to launch. 
The start script is run using `npm start`. For example, the `scripts.start` field
in the following package.json file means that `node main/index.js` will be run when the application starts.

    {
      "name": "node-js-sample-app",
      "version": "0.1.0",
      "scripts": {
        "start": "node main/index.js"
      }
    }

See the [NPM documentation](https://www.npmjs.org/doc/misc/npm-scripts.html) on the "scripts" package.json field.

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

Once you have added these modules as dependencies, use `require()` to access it from JavaScript, then
use the module references to make API calls:

    var imagemagick = require('imagemagick');

    imagemagick.identify('favicon.ico', function(err, features) {
        if (err)
            throw err;
        console.log(features["image statistics"]);
    });


## Migrating Existing Node.js Applications to Node.ACS

If you already have a Node.js application and would like to run it on Node.ACS
cloud, the migration process is simple: 

1.  Login to Node.ACS by running the following command:
   
        $ acs login
     
    When prompted, enter your account credentials.

2.  If your application doesn't include a package.json file, create one.

3.  Specify the application starting point using either the `main` package.json field,
    or a `scripts.start` field. See [Application Starting Point](#!/guide/node_standard-section-starting-point)
    for details.

3.  Publish the application by running the following command:

        $ acs publish

        ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.16
        Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.

        Admin Hostname: https://admin.cloudapp-enterprise.appcelerator.com
        Preparing application for publish... |
        It looks like you don't have this app created on Node.ACS yet. 
        Do you want to create it for publishing now (yes/no)?         

  4. Type **yes** to create a new application in the Node.ACS cloud. If you belong to more than one
      Appcelerator Platform organization, you are prompted to select the organization
      the application will be assigned to:

        Creating new Node.ACS app...
        Please choose the organization to which the application should be assigned:
          1) Appcelerator Eng (55555)
          2) Appcelerator QE (77777)
          : 2
      
      The application is published, any dependent Node modules are loaded and the 
      application is started. Lastly, the URL where the application is available is shown.

        Creating new Node.ACS app for organization Appcelerator QE (77777)...
        Preparing application for publish... done
        Publishing to cloud...
        [##########################################################################] 100%
        Start verifying app...
        Start loading node modules...
        Node modules are loaded. Cleaning up...
        Done loading node modules!
        App node-js-sample version 0.1.0 published.
        App will be available at https://8eabfb3cefd09ff5991496ff40846290d58862fd.cloudapp-enterprise.appcelerator.com      

That's it! Your application is running in the Node.ACS cloud.