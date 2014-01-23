# config -- Configures the Cloud Servers for the Application</h2>

## Description

<p class="note">This command is  available for enterprise customers using the Appcelerator Platform.</p>

This `config` command configures the number of cloud servers available to your application. 
You can configure your application to automatically scale up (or down) the number of servers based on the number queued requests. 
You specify the maximum number of queued requests that should occur before the application is scaled up. 
You can also specify the maximum number of servers that should be used.
 
By default, a new Node.ACS application is limited to only one cloud server. To increase the maximum
number of cloud servers, contact Appcelerator Support and provide the following information with
your request:

  * Application Name
  * E-mail address (Node.ACS username) that created the application

## Usage

`$ acs config [options] [appname]`

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

<table class="doc_content_table">
    <tbody>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>appname</code></td>
        <td>
            The name of the app to configure cloud server resources for. If omitted, the command needs to be run
            In the application's root directory, or specify the application's directory with the <code>-d</code> or <code>--directory</code> option.
        </td>
    </tr>
    <tr>
        <td nowrap><code>--autoscale &lt;true|false&gt;</code></td>
        <td>Enables or disables autoscaling.  This setting must be enabled to use the <code>autoscaleup</code> and <code>autoscaledown</code> settings.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaleup &lt;true|false&gt;</code></td>
        <td>Enables or disables automatically scaling up the number of cloud servers based on the <code>maxqueuedrequests</code> setting.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaledown &lt;true|false&gt;</code></td>
        <td>Enables or disables automatically scaling down the number of cloud servers based on the <code>maxqueuedrequests</code>  setting.</td>
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

To setup autoscaling, run the following commands:

    $ acs config --autoscale true MyFirstApp
    $ acs config --maxsize 5 MyFirstApp
    $ acs config --maxqueuedrequests 20 MyFirstApp

