# Using the Cluster module with Node.ACS #

A single instance of Node runs in a single thread. To take advantage of multi-core systems, you can 
launch a cluster of Node processes to handle the load. Node.ACS applications can use the core 
Node [Cluster](http://nodejs.org/api/cluster.html) module to easily create child processes that all share server ports.

Note the following:

* You must set a path to a custom file for child processes with the 
[cluster.setupMaster()](http://nodejs.org/api/cluster.html#cluster_cluster_setupmaster_settings) 
(see Example below). The error "Please specify a file to run as cluster children" will result otherwise.
* A cluster should listen on port 9000 or greater to avoid port conflicts. If the port your application 
is trying to listen on is in use, a `EADDRINUSE` error will result.
* If application does not have privileges to listen on the specified port, an `EACCES` error will result.

## Example

In the following example, the main app.js file sets a custom file (child.js) as the 
custom child process, and then forks a child process for each available CPU. The child process 
creates an HTTP server that listens on port 9000.
 
**app.js**

    var cluster = require('cluster');
    var http = require('http');
    var numCPUs = require('os').cpus().length;


    cluster.setupMaster({exec: __dirname + '/child.js'});

    // Fork workers.
    for (var i = 0; i < numCPUs; i++) {
        cluster.fork();
    }


**child.js**

    var http = require('http');
    var logger = require('acs').logger;

    logger.debug('Running in child process of a cluster.')

    http.createServer(function(req, res) {
        res.writeHead(200);
        res.end("hello world!!!\n");
    }).listen(9000);