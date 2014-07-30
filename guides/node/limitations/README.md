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
