# config -- Configures the Cloud Servers for the Application</h2>

## Description

<p class="note">This command is only available for Appcelerator Platform users.
By default, a Node.ACS application is limited to one cloud server. To increase the maximum number of cloud servers, contact <a href="http://support2.appcelerator.com">Appcelerator Support</a>.</p>

The `config` command configures the number of cloud servers available to your application. 

You can configure your application to automatically scale up (or down) the number of servers based on the number queued requests. 
You specify the maximum number of queued requests that should occur before the application is scaled up. 
You can also specify the maximum number of servers that should be used.

## Usage

`$ acs config [--autoscale true|false] [--autoscaleup true|false] [--autoscaledown true|false] [--setsize N] [--maxsessionrate N] appname`

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

<table class="doc-table">
    <tbody>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>appname</code></td>
        <td>
            The name of the app to configure cloud server resources for. If omitted, the command needs to be run
            in the application's root directory, or specify the application's directory with the <code>-d</code> or <code>--directory</code> option.
        </td>
    </tr>
    <tr>
        <td nowrap><code>--autoscale</code></td>
        <td>Boolean (default is <code>false</code>). Enables or disables autoscaling. Must be set to <code>true</code> to use the <code>autoscaleup</code> and <code>autoscaledown</code> settings.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaleup</code></td>
        <td>Boolean (default is <code>false</code>). Enables or disables automatically scaling up the number of cloud servers based on the <code>maxqueuedrequests</code> setting.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaledown</code></td>
        <td>Boolean (default is <code>false</code>). Enables or disables automatically scaling down the number of cloud servers based on the <code>maxqueuedrequests</code>  setting.</td>
    </tr>
    <tr>
        <td nowrap><code>--maxqueuedrequests &lt;n&gt;</code></td>
        <td>Specifies the maximum number of queued requests for autoscaling to occur. The number should be based on the response time of your application; the longer the response time is, the smaller this value should be. The default value is 50.</td>
    </tr>
    <tr>
        <td nowrap><code>--setsize &lt;n&gt;</code></td>
        <td>Sets the current number of cloud servers to use.</td>
    </tr>    
    <tr>
        <td nowrap><code>--maxsize &lt;n&gt;</code></td>
        <td>Sets the maximum number of cloud servers to use.</td>
    </tr>        
    <tr>
        <td><code>-h</code>, <code>--help</code></td>
        <td>Displays help information of the command</td>
    </tr>
    </tbody>
</table>

## Example

The following example enables autoscaling, using a maximum of five servers, when there are at least
20 queued requests. The application is also configured to automatically scale down the number of servers
when the number of queued requests drops below 20.

    acs config --autoscale true MyFirstApp
    acs config --maxsize 5 MyFirstApp
    acs config --maxqueuedrequests 20 MyFirstApp
    acs config --autoscaleup true MyFirstApp
    acs config --autoscaledown true MyFirstApp

