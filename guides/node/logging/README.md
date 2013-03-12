
# Application Logging

A Node.ACS application typically runs in the cloud, so getting to know what is
happening in the app is very important. Any log output written to stdout or stderr is 
captured and and stored by Node.ACS, and can be viewed using the **acs** command-line
tool.

**Note:** Errors such as syntax errors, app crashes or system level failures, are logged
automatically. These messages can be viewed the same way as any other log output from your
application.

## The Logging Utilities  

The Node.ACS CLI (**acs**) provides two commands for viewing logs for a
published application, **logcat** and **loglist**.

The **logcat** command tails your published application's log continuously
from Node.ACS cloud. For more detailed information, refer to
[logcat](#!/guide/cli/logcat) command usage.

The **loglist** command lists your published application's log for a specific
period. By default, a maximum of 100 log messages are returned at a time. For
more detailed information, refer to [loglist](#!/guide/cli/loglist) command usage.

