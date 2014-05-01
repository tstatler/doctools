
# accesslog -- List Application's Access Log

## Description

List application's access logs within a specified period. By default, a maximum
of 100 log messages will be returned at a time. Each log record contains the following fields:

* Date and time
* IP of server that handled the request
* URL of requested resource
* The execution time of the request in milliseconds

Note that these fields are only reported for Node.ACS applications that use the
 [Node.ACS MVC framework](http://docs.appcelerator.com/cloud/latest/#!/guide/node_mvc).

## Usage

`$ acs accesslog` [_options_] [_appname_]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

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
        <tr>
            <td nowrap><code>--server_id</code> <em>serverid</em></td>
            <td>Id of the server which the logs from. An app may be deployed to multiple servers in cloud.</td>
        </tr>
        <tr>
            <td nowrap><code>--show_serverid</code></td>
            <td>Show server ID in logs</td>
        </tr>
        <tr>
            <td nowrap><code>--start_date <em>start_date</em></td>
            <td>Starting date for retrieving logs.</td>
        </tr>
        <tr>
            <td><code>--end_date<code> <em>end_date</em></td>
            <td>Ending date for retrieving logs.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to. This parameter only is required if the target application has the same name as an application in another organization you belong to.
             </td>
        </tr>
        <tr>
            <td><code>--per_page<code> <em>per_page</em></td>
            <td>Number of log messages per page. Default: 100</td>
        </tr>
        <tr>
            <td nowrap><code>--more</code></td>
            <td>Display the next page of log messages.</td>
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
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
    
    Retrieving access log from the server
    [12/11/2013 08:46:23.092]   127.0.0.1   /   10068ms
    [12/11/2013 08:43:55.790]   127.0.0.1   /css/style.css   10074ms
    [12/11/2013 08:43:23.712]   127.0.0.1   /   10073ms
    [12/11/2013 08:43:07.237]   127.0.0.1   /   10073ms
    [12/11/2013 08:42:48.365]   127.0.0.1   /   10075ms


