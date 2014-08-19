
# Application Logging

A Node.ACS application typically runs in the cloud, so being able to see what is happening in the
application is very important. Any log output written to `stdout` or `stderr` in the application's
root process is captured and stored by Node.ACS, and can be viewed using the
[acs](#!/guide/node_cli) command-line tool. Additionally, you can use the [Logger class](#!/guide/node_logging-section-node-acs-logger-utility-class) to generate custom log messages.

**Notes:** 

* Only output written by the application's root process is included in the log file; output written by
[child processes](#!/guide/node_clustering) forked by the application's root process will not be caught.
* Errors such as syntax errors, application crashes and system level failures are logged
automatically. 

## Logging Utilities  

The Node.ACS CLI (**acs**) provides three commands for viewing logs for a
published application, **accesslog**, **logcat**, **loglist**.

* The [`accesslog`](#!/guide/node_cli_accesslog) command lists all requests processed by the
  Node.ACS server in a specified time period. By default, a maximum of 100 log messages are returned
  at a time.

* The [`loglist`](#!/guide/node_cli_loglist) command lists your published application's log for a specific
period. By default, a maximum of 100 log messages are returned at a time.

* The [`logcat`](#!/guide/node_cli_logcat) command tails your published application's log continuously
from Node.ACS cloud.

## About logged execution times ##

The execution time reported by the `loglist` and `accesslog` commands report slightly different
values. The `accesslog` command reports the time required by Node.ACS to handle the initial user
request, pass it to your Node application for processing, and deliver the response. In contrast,
`loglist` only reports the execution time for your application itself, not including the time
required to process the request and response. Consequently, the `accesslog` execution times are a
slightly longer than those of the corresponding `loglist` log item. For instance, below is `accesslog`
output:

<pre>
[12/11/2013 08:43:55.790]   127.0.0.1   /   10074ms
[12/11/2013 08:43:23.712]   127.0.0.1   /   10073ms
[12/11/2013 08:43:07.237]   127.0.0.1   /   10073ms
[12/11/2013 08:42:48.365]   127.0.0.1   /   10075ms
</pre>

And below is the corresponding `loglist` output.

<pre>
12/11/2013 16:42:028.139 [INFO] [43210] App started
[PERF]  GET / 10069 ms
[PERF]  GET / 10072 ms
[PERF]  GET / 10072 ms
[PERF]  GET / 10066 ms
</pre>

## Node.ACS Logger utility class 
The `logger` class let you add custom messages to the application log, in addition to the ones generated automatically by Node.ACS. For published applications, custom log
messages appear in the output of the [`loglist`](#!/guide/node_cli_loglist) and
[`logcat`](#!/guide/node_cli_logcat) commands. When running your application locally (via the [`acs
run`](#!/guide/node_cli_run) command, they are displayed in the local console.

### Usage
First, require the `logger` class:

	var logger = require('acs').logger;

Set the desired [log level](#!/guide/node_logging-section-specifying-application-log-level) by calling the `setLevel()` method:

	logger.setLevel('ALL');

Call one of the [logging methods](#!/guide/node_logging-section-logging-methods):

	// Initializing MVC app
	function start(app, express) {
		logger.info('STARTING APP...');
	    app.use(express.favicon(__dirname + '/public/images/favicon.ico'));
	}

For published applications, log messages are displayed by the output of the `acs loglist` and
`acs logcat` commands, for example:

	$ acs logcat

	08/19/2014 11:29:004.289 [INFO] [3279] ------------ Run MVC App ------------
	08/19/2014 11:29:004.573 [INFO] [3279] STARTING APP...

When running your application locally via the `acs run` command log messages are displayed in the console.

### Specifying Application Log Level

To set the log level, you call `logger.setLevel()` and pass it one of the following log level
strings, in ascending order of log detail:

* `"OFF"` &mdash; Disables log generation.
* `"FATAL"`
* `"ERROR"`
* `"WARN"`
* `"INFO"`
* `"DEBUG"`
* `"TRACE"`
* `"ALL"` &mdash; Includes output from all log methods.

The current log level determines which [log method](#!/guide/node_logging-section-logging-methods) output is included in the log output. 
For example, if you set the log level to `"WARN"`, only messages logged by
`logger.fatal()`, `logger.error()`, or `logger./warn()` methods will be included in the log:

	logger.setLevel('WARN');
	logger.warn("WARNING..."); 	// Included in log
	logger.debug("DEBUG...");	// Not included in log


To include messages from all log methods, set the log level to `"ALL"`:

	logger.setLevel('ALL');

To disable log generation entirely, set the log level to `"OFF"`:

	logger.setLevel('OFF');

The default log level is `"DEBUG"`, if not specified.

### Logging Methods

To log a message, call one of the following methods, passing it the string to output. The [logging level](#!/guide/node_logging-section-specifying-application-log-level) must be set to an appropriate level.

* `logger.fatal(<message>)` &mdash; Output only when log level is set to `"FATAL"`, or `"ALL"`.
* `logger.error(<message>)` &mdash; Output only when log level is set to `"FATAL"`, `"ERROR"`, or `"ALL"`.
* `logger.warn(<message>)` &mdash; Output only when log level is set to `"FATAL"`, `"ERROR"`, `"WARN"`, or `"ALL"`. 
* `logger.info(<message>)` &mdash; Output only when log level is set to `"FATAL"`, `"ERROR"`, `"WARN"`, `"INFO"`, or `"ALL"` 
* `logger.debug(<message>)` &mdash; Output only when log level is set to `"FATAL"`, `"ERROR"`, `"WARN"`, `"INFO"`, `"DEBUG"`, or `"ALL"`. 
* `logger.trace(<message>)` &mdash; Output only when log level is set to `"FATAL"`, `"ERROR"`, `"WARN"`, `"INFO"`, `"DEBUG"`, `"TRACE"`, or `"ALL"`.
