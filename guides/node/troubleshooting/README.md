# Node.ACS Troubleshooting Guide

This document summarizes the kinds of exceptions you may encounter when deploying or running a 
Node.ACS application, or when installing or upgrading the `acs` NPM package on your system.

The [`acs list`](#!/guide/node_cli_list) and [`acs loglist`](#!/guide/node_cli_loglist) CLI commands
are used to troubleshoot deployment or runtime issues. Note that `acs loglist` may not immediately
retrieve the latest logs from the server; you may need to wait a few seconds and try running the command
again. 

## Exceptions thrown upon deployment

### Exception in app.js outside start() method ###

The following code references an undefined variable outside application's `start()` method.

    // initialize app
    function start(app, express) {
        app.use(express.favicon(__dirname + '/public/images/favicon.ico'));     //set favicon
    }

    adsgasdg;   // This line causes exception.

    // release resources
    function stop() {
    }

In this scenario the **Message** field of `acs list` and `acs loglist` output indicates a
`ReferenceError` and the name and location of the reference. The **Status** field of the `acs list`
command is set to **"Failed to deploy"**.

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:18:26 GMT+0800 (CST)
    -- Status: Failed to deploy
    -- Message: ReferenceError: adsgasdg is not defined at /app.js:6:1

    $ acs loglist testapp
    12/26/2013 05:18:030.335 [INFO] [4454] ------------ Run MVC App ------------
    12/26/2013 05:18:030.635 [ERROR] [4454] Failed to load main script. ReferenceError: adsgasdg is not defined
    at /app.js:6:1
    12/26/2013 05:18:030.636 [ERROR] [4454] ReferenceError: adsgasdg is not defined
    at /app.js:6:1

### Exception inside app.js start() method ##

The following code references an undefined variable inside application's `start()` method.

    // initialize app
    function start(app, express) {

        adsgasdg;   // This line causes exception.

        app.use(express.favicon(__dirname + '/public/images/favicon.ico'));     //set favicon
    }

    // release resources
    function stop() {
    }

In this scenario the **Message** field of `acs list` and `acs loglist` output indicates a
`ReferenceError` and the name and location of the exception. The **Status** field of the `acs list`
command is set to **"Failed to deploy"**.

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:20:40 GMT+0800 (CST)
    -- Status: Failed to deploy
    -- Message: ReferenceError: adsgasdg is not defined
    at Object.start (/app.js:4:5)

    $ acs loglist testapp
    12/26/2013 05:20:043.923 [INFO] [4488] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:20:044.224 [ERROR] [4488] Failed to run start(). ReferenceError: adsgasdg is not defined
    at Object.start (/app.js:4:5)

    12/26/2013 05:20:044.225 [ERROR] [4488] ReferenceError: adsgasdg is not defined
    at Object.start (/app.js:4:5)


### Exception in a controller, outside a function

The following code references an undefined variable inside a controller, outside any function definition:

    function index(req, res) {
        res.render('index', { title: 'Welcome to Node.ACS! ' + process.version });
    }
     
    asgasg;dkg;as   // This line causes exception.

When accessing the application and hitting the controller over HTTP, it returns the following error: 

    Cannot get /

In this scenario the `acs list` output doesn't indicate a problem, but `acs loglist` indicates a
`ReferenceError` and the name and location of the exception. 

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Current number of deployed servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:24:54 GMT+0800 (CST)
    -- Servers: 
    No. 1 ID: 52b81468754c4184e58e8789 Status: Deployed

    $ acs loglist testapp 
    12/26/2013 05:24:059.035 [INFO] [4503] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:24:059.427 [ERROR] [4503] Failed to load controller "application.js". 
        ReferenceError: asgasg is not defined at /controllers/application.js:5:1


## Exceptions thrown at runtime ##

### Exception in synchronous calls handling requests ###

The following code references an undefined variable inside a controller function.

    function index(req, res) {

       asgasg;dkg;as    // This line causes exception.
     
       res.render('index', { title: 'Welcome to Node.ACS! ' + process.version });
    }

In this scenario the `acs list` output doesn't indicate a problem, but `acs loglist` indicates a
`ReferenceError` and the name and location of the exception.

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Current number of deployed servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:29:52 GMT+0800 (CST)
    -- Servers: 
    No. 1 ID: 52b81468754c4184e58e8789 Status: Deployed

    $ acs loglist testapp
    12/26/2013 05:33:003.721 [INFO] [4541] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:33:004.122 [INFO] [4541] App started
    ReferenceError: asgasg is not defined at index (/controllers/application.js:3:5)
    [PERF] GET / 9 ms

The response when accessing the application and hitting that function indicates the name and
location of the reference error:

    ReferenceError: asgasg is not defined
        at index (/controllers/application.js:2:4)


### Exception in asynchronous callbacks handling requests (or background jobs) ##

The following code sample uses the setTimeout() method to asynchronously call a function that
contains an exception.

    function index(req, res) {
        setTimeout(function(){
            respond(res);
        }, 2000);
    }
    function respond(res) {
        asgasg;af   //This line causes exception.
        res.render('index', { title: 'Welcome to Node.ACS! ' + process.version });
    }

In this scenario when accessing the application over HTTP and hitting the function, the following
error is returned:

    An error has occurred: {"code":"ECONNRESET"}

In this scenario `acs loglist` indicates a `ReferenceError` and the corresponding stack trace; `acs
list` does not indicate any problem.

    $ acs loglist testapp
    12/26/2013 05:44:043.639 [INFO] [4606] ------------ Run MVC App ------------

    info: socket.io started
    12/26/2013 05:44:044.054 [INFO] [4606] App started
    12/26/2013 05:44:053.999 [ERROR] [4606] ReferenceError: asgasg is not defined
    at respond (/controllers/application.js:8:5)
    at null._onTimeout (/controllers/application.js:3:9)
    at Timer.listOnTimeout [as ontimeout] (timers.js:110:15)

    12/26/2013 05:44:059.627 [INFO] [4614] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:45:000.029 [INFO] [4614] App started

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Current number of deployed servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:29:52 GMT+0800 (CST)
    -- Servers: 
    No. 1 ID: 52b81468754c4184e58e8789 Status: Deployed


### Application crashes while handling requests

The following code has request handler that quickly uses up available memory, causing the application to crash.

    function index(req, res) {
        respond(res);
    }

    function respond(res) {
        var cur = 167772160;
        var bcast = 184549375;
        var addresses = [];
        while (cur <= bcast){
            cur += 1;
            addresses.push(cur);
        }
        console.log(addresses.length);
        console.log(addresses); // memory goes from a few megs to over a gig in seconds when trying to print this
        res.send(addresses);
    }

The `acs loglist` output indicates "FATAL ERROR: JS Allocation failed - process out of memory"; `acs
list` doesn't indicate any problem.

    $ acs loglist testapp
    12/26/2013 05:58:042.432 [INFO] [4628] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:58:042.828 [INFO] [4628] App started
    FATAL ERROR: JS Allocation failed - process out of memory
    12/26/2013 05:59:000.030 [INFO] [4636] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 05:59:000.434 [INFO] [4636] App started

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Current number of deployed servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:29:52 GMT+0800 (CST)
    -- Servers: 
    No. 1 ID: 52b81468754c4184e58e8789 Status: Deployed

### Application crashes while running background jobs ###

The following code causes the application to run out of memory and crash while processing a
`setTimeout()` function call.

    // initialize app
    function start(app, express) {
        app.use(express.favicon(__dirname + '/public/images/favicon.ico'));     //set favicon
        setTimeout(dosth, 5000);
    }

    // release resources
    function stop() {
    }


    function dosth() {
        var cur = 167772160;
        var bcast = 184549375;
        var addresses = [];
        while (cur <= bcast){
            cur += 1;
            addresses.push(cur);
        }
        console.log(addresses.length);
        console.log(addresses); // memory goes from a few megs to over a gig in seconds when trying to print this
    }

The `acs loglist` output indicates "FATAL ERROR: JS Allocation failed - process out of memory"; `acs
list` doesn't indicate any problem.

    $ acs loglist testapp
    12/26/2013 06:04:043.934 [INFO] [4667] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 06:04:044.332 [INFO] [4667] App started
    FATAL ERROR: JS Allocation failed - process out of memory
    12/26/2013 06:05:000.529 [INFO] [4671] ------------ Run MVC App ------------
    info: socket.io started
    12/26/2013 06:05:000.927 [INFO] [4671] App started
    FATAL ERROR: JS Allocation failed - process out of memory

    $ acs list testapp
    App name: testapp
    -- URL: http://a3110b813195ca3a774913a767e49a1ce5f17e63.cloud-services.appcelerator.com
    -- Created at: Tue Dec 24 2013 21:15:19 GMT+0800 (CST)
    -- Node Version: 0.10.22
    -- Maximum allowed number of servers: 1
    -- Desired number of servers: 1
    -- Current number of deployed servers: 1
    -- Active version: 0.1.0
    -- Published at: Thu Dec 26 2013 09:29:52 GMT+0800 (CST)
    -- Servers: 
    No. 1 ID: 52b81468754c4184e58e8789 Status: Deployed    

## Installation errors

This section describes issues you may encounter when installing or upgrading Node.ACS using NPM.

### Error: ENOENT, no such file or directory

Node.ACS installation fails with the following error:

    ...
    fs.js:427
      return binding.open(pathModule._makeLong(path), stringToFlags(flags), mode);
                     ^
    Error: ENOENT, no such file or directory '/usr/local/lib/node_modules/acs/bin/acsx'
        at Object.fs.openSync (fs.js:427:18)
        at Object.fs.readFileSync (fs.js:284:15)
        at Object.<anonymous> (/usr/local/lib/node_modules/acs/scripts/config.js:21:19)
        at Module._compile (module.js:456:26)
        at Object.Module._extensions..js (module.js:474:10)
        at Module.load (module.js:356:32)
        at Function.Module._load (module.js:312:12)
        at Function.Module.runMain (module.js:497:10)
        at startup (node.js:119:16)
        at node.js:902:3 

To resolve, try deleting your `~/.npm` folder and cleaning the NPM cache, then re-installing:

    rm -rf ~/.npm
    npm cache clear
    sudo npm -g install acs
