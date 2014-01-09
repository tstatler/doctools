
# loglist -- List Application's Logs

## Description

List application's log within a specific period. By default, a maximum of 100
log messages will be returned at a time.

Note that results from `acs loglist` commands may require a few seconds before displaying.

## Usage

`$ acs loglist` [ _options_ ] [ _appname_ | -d _app_dir_ ]

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
            <td>The name of the app to retrieve and show runtime logs for. If omitted, you must run the command in the application's root directory,
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
            <td nowrap>--server_id <i>serverid</i></td>
            <td>ID of the server to retrieve logs from. An application may be deployed to multiple servers in the cloud.</td>
        </tr>
        <tr>
            <td nowrap>--show_serverid</td>
            <td>Show server ID in logs</td>
        </tr>
        <tr>
            <td nowrap>--start_date <i>start_date</i></td>
            <td>Starting date for retrieving logs.</td>
        </tr>
        <tr>
            <td>--end_date <i>end_date</i></td>
            <td>Ending date for retrieving logs.</td>
        </tr>
        <tr>
            <td>--per_page <i>per_page</i></td>
            <td>Number of log messages per page. Default: 100.</td>
        </tr>
        <tr>
            <td nowrap>--more</td>
            <td>Display the next page of log messages.</td>
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

**Note: **Each line in the following example begins with the server ID.
    
    
    $ acs loglist MyProject
    
    Retrieves the latest log files from the server
    [Records] 7	[Pages] 1	[Current Page] 1
    [51069065b9d95bfc89b99222] 02/05/2013 12:24:009.126 [DEBUG] [11779] ------------ Run MVC App ------------
    [51069065b9d95bfc89b99222] info: socket.io started
    [51069065b9d95bfc89b99222] 02/05/2013 12:24:009.438 [INFO] [11779] App started
    [51069065b9d95bfc89b99222] [PERF]  GET / 3 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /guides/quickstart 186 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /favicon.ico 1 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /guides/logging 15 ms
    
