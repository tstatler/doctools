
# logcat -- Tail an Active Application's Logs

## Description

Retrieves and displays a published application's runtime logs continuously from
Node.ACS. It lets you see in real-time what's happening with an application running in the cloud.  By default, runtime logs are retrieved every 5 seconds, and you can configure this interval with the `--interval` parameter. 

For an overview of Node.ACS logging utilities see , see [Logging Utilities](/cloud/latest/#!/guide/node_logging-section-logging-utilities).

## Usage

`$ acs logcat` [ _options_ ] [ _appname_ ]

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

## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td nowrap><code>--server_id<code> <em>serverid</em></td>
            <td>ID of the server to retrieve logs from. An application may be deployed to multiple servers in the cloud.</td>
        </tr>
        <tr>
            <td nowrap><code>--show_serverid<code></td>
            <td>Show server ID in logs</td>
        </tr>
        <tr>
            <td><code>--interval<code> <em>interval</em></td>
            <td>Interval for retrieving application logs, in seconds.  Default: 5s.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to.  This parameter is required
            if the target application has the same name as an application in another organization 
            you belong to.
             </td>
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

**Note: **Each line in the following example begins with the server ID.
    
    
    $ acs logcat MyProject
    
    [51069065b9d95bfc89b99222] 02/05/2013 12:24:009.126 [DEBUG] [11779] ------------ Run MVC App ------------
    [51069065b9d95bfc89b99222] info: socket.io started
    [51069065b9d95bfc89b99222] 02/05/2013 12:24:009.438 [INFO] [11779] App started
    [51069065b9d95bfc89b99222] [PERF]  GET / 3 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /guides/quickstart 186 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /favicon.ico 1 ms
    [51069065b9d95bfc89b99222] [PERF]  GET /guides/logging 15 ms
    
    

