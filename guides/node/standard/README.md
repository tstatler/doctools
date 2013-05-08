
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

## Module Dependencies

The application can import any 3rd-party modules that are supported by
standard node.js. Before publishing the app to the cloud, make sure
all dependencies are listed in the `dependencies` field in the application's
`package.json` file.

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

