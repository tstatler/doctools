# config -- Configures the Cloud Servers for the Application</h2>

## Description

<p class="note">This command is only available for enterprise customers using the Appcelerator Platform. 
By default, a Node.ACS application is limited to one cloud server. To increase the maximum number of cloud servers, contact <a href="http://support2.appcelerator.com">Appcelerator Support</a>.</p>

Configures the number of cloud servers for the application to use. Enable the auto-scaling 
feature to automatically scale up and down the number of cloud servers based on the access session rate. 
The access session rate is the total number of HTTP requests received per second within a minute. You must also set the `--maxsessionrate` parameter to use auto-scaling. 

</div>

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
            in the application's root directory, or specify the application's directory with the '-d' option.
        </td>
    </tr>
    <tr>
        <td nowrap><code>--autoscale &lt;true|false&gt;</code></td>
        <td>Enables or disables autoscaling.  This setting must be enabled to set the 'maxsessionrate', 'autoscaleup' and 'autoscaledown' settings.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaleup &lt;true|false&gt;</code></td>
        <td>Enables or disables automatically scaling up the number of cloud servers based on the 'maxsessionrate' setting.</td>
    </tr>
    <tr>
        <td nowrap><code>--autoscaledown &lt;true|false&gt;</code></td>
        <td>Enables or disables automatically scaling down the number of cloud servers based on the 'maxsessionrate' setting.</td>
    </tr>
    <tr>
        <td nowrap><code>--setsize &lt;n&gt;</code></td>
        <td>Sets the current number of cloud servers to use. 
        <p><strong>Note:</strong> The current Node.ACS user must be an account administrator to change the number of cloud servers. Contact <a href="http://support2.appcelerator.com">Appcelerator Support</a> for assistance.</p> </td>
    </tr>
    <tr>
        <td nowrap><code>--maxsessionrate &lt;n&gt;</code></td>
        <td>Sets the session rate threshold for autoscaling.</td>
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
        <td>Displays help information of the command</td>
    </tr>
    </tbody>
</table>

## Example

To setup autoscaling, run the following commands:

    $ acs config --autoscale true MyProject
    $ acs config --maxsessionrate 50 MyProject
    $ acs config --autoscaleup true MyProject
    $ acs config --autoscaledown true MyProject

