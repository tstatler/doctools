# Application Limitations

This document lists known limitations for Node.ACS applications.

## Memory

Each application container is allocated 256 MB of memory.

## Diskspace

Each application can use 1.8 GB of diskspace.  The application can only write files to the project's
root directory and to the `/tmp` folder.

## Server Ports

Currently, Node.ACS only supports applications opening one server listening
port. There cannot be more than one TCP/HTTP server started in one
application.

If you are using an [external script](#!/guide/node_config-section-scripts) to start your application,
you access the port number provided to the application by using the `process.env.PORT` variable in your
JavaScript code.
