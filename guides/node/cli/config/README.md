# config -- Configures the application environment</h2>

## Description

<p class="note">This command is only available for Appcelerator Platform users.
By default, a Node.ACS application is limited to one cloud server.
To increase the maximum number of cloud servers, contact <a href="http://support2.appcelerator.com">Appcelerator Support</a>.</p>

The `config` command configures environment variables and the number of cloud servers for the application to use.

### Environment Variables

To set environment variables, use the `--set <key>=<value>` parameter.  To set more than one
variable at a time, comma separate the key-value pairs.

You can access the environment variables from the Node.ACS application using the `process.env`
namespace.  For example, if you set a variable called `foo`, use `process.env.foo` to access it in
the application.

To unset an environment variable, use the `--unset <key>` parameter.

To check the current environment variables, use the `--env` parameter.

You cannot use the following names for environment variables: "appid", "basedir", "name", "version",
"dirname", "fullpath", "framework", "config", "serverId", "bodyParser", "customConfig", "HOME",
"NODE_PATH", "USER", "TMPDIR", "PATH", "NODE", and "PWD".

After changing an environment variable, you will be prompted to restart the application.

### Auto-Scaling

To customize the number of cloud servers the application can use, enable the auto-scaling
feature to automatically scale up and down the number of cloud servers based on the number of queued requests.
You specify the maximum number of queued requests that should occur before the application is scaled up. 
You can also specify the maximum number of servers that should be used.

## Usage

**Environment variables:**

`$acs config [--set <key>=<value>] [--unset <key>] [--env] [appname]`

**Auto-scaling:**

`$ acs config [--autoscale true|false] [--autoscaleup true|false] [--autoscaledown true|false] [--setsize N] [--setmaxsize N] [--maxqueuedrequests N] [appname]`

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
        <td>Boolean (default is <code>false</code>). Enables or disables autoscaling. Must be set to <code>true</code>
            to use the <code>autoscaleup</code> and <code>autoscaledown</code> settings.</td>
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
        <td nowrap><code>--env</code></td>
        <td>Lists set environment variables.</td>
    </tr>
    <tr>
        <td nowrap><code>--maxqueuedrequests &lt;n&gt;</code></td>
        <td>Specifies the maximum number of queued requests for autoscaling to occur.
            The number should be based on the response time of your application;
            the longer the response time is, the smaller this value should be. The default value is 50.</td>
    </tr>
    <tr>
        <td nowrap><code>--set &lt;key&gt;=&lt;value&gt;</code></td>
        <td><p>Sets an environment variable.</p>
            <p>To set more than one variable, comma separate the key-value pairs.</p>
            <p>To access the variable in the application, prefix the variable with the <code>process.env</code> namepsace.</p>
        </td>
    </tr>
    <tr>
        <td nowrap><code>--setsize &lt;n&gt;</code></td>
        <td>Sets the current number of cloud servers to use.</td>
    </tr>
    <tr>
        <td nowrap><code>--maxsize &lt;n&gt;</code></td>
        <td>Sets the maximum number of cloud servers to use.
        <p><strong>Note:</strong> The current Node.ACS user must be an account administrator to set this value.
           Contact <a href="http://support2.appcelerator.com">Appcelerator Support</a> for assistance.</p> </td>
    </tr>
    <tr>
        <td nowrap><code>--unset &lt;key&gt;</code></td>
        <td>Unsets the specified environment variable.</td>
    </tr>
    <tr>
        <td><code>--org <em>orgID</em></code></td>
        <td>The ID of the organization the application belongs to. This parameter only is required if the target application has the same name as an application in another organization you belong to.
         </td>
    </tr>
    <tr>
        <td><code>-h</code>, <code>--help</code></td>
        <td>Displays help information of the command</td>
    </tr>
    </tbody>
</table>

## Example

The following example sets the `port` and `foo` environment variables, unsets the `foo` variable,
then lists all set environment variables.

    acs config --set port=8080,foo=abc
    acs config --unset foo
    acs config --env

The following example enables autoscaling, using a maximum of five servers, when there are at least
20 queued requests. The application is also configured to automatically scale down the number of servers
when the number of queued requests drops below 20.

    acs config --autoscale true MyFirstApp
    acs config --maxsize 5 MyFirstApp
    acs config --maxqueuedrequests 20 MyFirstApp
    acs config --autoscaleup true MyFirstApp
    acs config --autoscaledown true MyFirstApp
