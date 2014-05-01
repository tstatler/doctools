# usage -- Check server system resource usage</h2>

## Description

Check server system resource usage within a specific period. The server in cloud logs CPU/memory usage periodically. By default, a maximum of 100 log entries will be returned at a time.

## Usage

`$ acs usage [options] [appname]`

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

<table class="doc_content_table">
    <tbody>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>appname</td>
        <td>The name of the app to retrieve and show system resource usage for. If omitted, the command needs to be run in application's root directory, or specify the application's directory with '-d' option.</td>
    </tr>
    <tr>
        <td nowrap><code>--server_id<code> <em>serverid</em></td>
        <td>Id of the server which the logs from. An app may be deployed to multiple servers in cloud.</td>
    </tr>
    <tr>
        <td nowrap><code>--show_serverid</code></td>
        <td>Show server ID in logs</td>
    </tr>
    <tr>
        <td nowrap><code>--start_date</code> <em>start_date</em></td>
        <td>Starting date for retrieving usage logs</td>
    </tr>
    <tr>
        <td><code>--end_date</code> <em>end_date</em></td>
        <td>Ending date for retrieving usage logs</td>
    </tr>
    <tr>
        <td nowrap><code>--page_number</code> <em>page_number</em></td>
        <td>Page of usage log output to display, where 1 is the most recent</td>
    </tr>
    <tr>
        <td><code>--per_page</code> <em>per_page</em></td>
        <td>Number of usage logs per page. Default: 100</td>
    </tr>
    <tr>
        <td><code>--more</code></td>
        <td>Display the next page of log messages.</td>
    </tr>
    <tr>
        <td><code>--org <em>orgID</em></code></td>
        <td>The ID of the organization the application belongs to.  This parameter is required
        if the target application has the same name as an application in another organization 
        you belong to.
         </td>
    </tr>    
    <tr>
        <td><code>-h</code>, --help</td>
        <td>Show help information of the command</td>
    </tr>
    </tbody>
</table>

Dates are specified as YYYY-MM-DD or "YYYY-MM-DD HH:MM". Note that if the time is included, the date string must be quoted. If the specified date range contains more than specified maximum number of logs, the most recent usage logs will be returned.

## Example

    $ acs usage MyProject

    Retrieves the usage data from the server
    [Records] 7	[Pages] 1	[Current Page] 1
    [02/26/2013 21:36:50.447]	memory: { free: 195.00M total: 256M }	loadavg: [ 10.79% ]
    [02/26/2013 21:36:20.448]	memory: { free: 195.95M total: 256M }	loadavg: [ 17.97% ]
    [02/26/2013 21:35:50.458]	memory: { free: 177.99M total: 256M }	loadavg: [ 27.49% ]
    [02/26/2013 21:35:20.457]	memory: { free: 180.02M total: 256M }	loadavg: [ 32.28% ]
    [02/26/2013 21:34:50.457]	memory: { free: 180.86M total: 256M }	loadavg: [ 40.28% ]
    [02/26/2013 21:34:20.459]	memory: { free: 181.91M total: 256M }	loadavg: [ 40.23% ]
    [02/26/2013 21:33:50.453]	memory: { free: 183.66M total: 256M }	loadavg: [ 40.19% ]
