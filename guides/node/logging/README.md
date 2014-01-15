
# Application Logging

A Node.ACS application typically runs in the cloud, so getting to know what is
happening in the app is very important. Any log output written to stdout or stderr is 
captured and and stored by Node.ACS, and can be viewed using the **acs** command-line
tool.

**Note:** Errors such as syntax errors, application crashes and system level failures, are logged
automatically. These messages can be viewed the same way as any other log output from your
application.

## Logging Utilities  

The Node.ACS CLI (**acs**) provides three commands for viewing logs for a
published application, **accesslog**, **logcat**, **loglist**.

* The `accesslog` command lists all requests processed by the Node.ACS server in a specified time
period. By default, a maximum of 100 log messages are returned at a time. See [`accesslog`](#!/guide/node_cli_accesslog).

* The `loglist` command lists your published application's log for a specific
period. By default, a maximum of 100 log messages are returned at a time. See [`loglist`](#!/guide/node_cli_loglist).

* The `logcat` command tails your published application's log continuously
from Node.ACS cloud. See [`logcat`](#!/guide/node_cli_logcat).

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

The times reported by the 
