
# accesslog -- List Application's Access Log

## Description

List application's access logs within a specific period. By default, a maximum
of 100 log messages will be returned at a time.

## Usage

`$ acs accesslog` [_options_] [_appname_]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>appname</td>
            <td>The name of the app to retrieve and show access logs for. If omitted, you must run the command in the application's root directory, 
                 or specify the application's directory with '-d' option.</td>
        </tr>
    </tbody>
</table>

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td nowrap>--start_date <i>start_date</i></td>
            <td>Starting date for retreiving logs.</td>
        </tr>
        <tr>
            <td>--end_date <i>end_date</i></td>
            <td>Ending date for retreiving logs.</td>
        </tr>
        <tr>
            <td nowrap>--page_number <i>page_number</i>/td>
            <td>Page of log output to display, where 1 is the most recent.</td>
        </tr>
        <tr>
            <td>--per_page <i>per_page</i></td>
            <td>Number of log messages per page. Default: 100</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

Dates are specified as YYYY-MM-DD or "YYYY-MM-DD HH:MM". Note that if the time
is included, the date string must be quoted. If the specified date range
contains more than specified maximum number of logs, the most recent messages
will be returned.

## Example
    
    $ acs accesslog MyProject
    
    Executing: accesslog
    Retrieves the latest log files from the server
    [Records] 6	[Pages] 1	[Current Page] 1
    [Thu Nov 15 2012 23:06:24 GMT+0800 (CST)]	124.126.170.159	/favicon.ico
    [Thu Nov 15 2012 23:06:24 GMT+0800 (CST)]	124.126.170.159	/css/style.css
    [Thu Nov 15 2012 23:06:23 GMT+0800 (CST)]	124.126.170.159	/
    [Thu Nov 15 2012 22:58:59 GMT+0800 (CST)]	124.126.170.159	/favicon.ico
    [Thu Nov 15 2012 22:58:58 GMT+0800 (CST)]	124.126.170.159	/css/style.css
    [Thu Nov 15 2012 22:58:58 GMT+0800 (CST)]	124.126.170.159	/
    

