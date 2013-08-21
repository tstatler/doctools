# config -- Configures the Cloud Servers for the Application</h2>

## Description

Note: This command is only available for enterprise customers using the Appcelerator Platform.

This command configures the number of cloud servers for the application to use.

The application can enable the autoscaling feature to automatically scale up and down the number of
cloud servers based on the access session rate.  The access session rate is the total number of HTTP
requests per second within a minute. You need to set the `maxsessionrate` to use this feature.

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
        <td>appname</td>
        <td>
            The name of the app to configure cloud server resources for. If omitted, the command needs to be run
            in the application's root directory, or specify the application's directory with the '-d' option.
        </td>
    </tr>
    <tr>
        <td nowrap>--autoscale &lt;true|false&gt;</td>
        <td>Enables or disables autoscaling.  This setting must be enabled to set the 'maxsessionrate', 'autoscaleup' and 'autoscaledown' settings.</td>
    </tr>
    <tr>
        <td nowrap>--autoscaleup &lt;true|false&gt;</td>
        <td>Enables or disables automatically scaling up the number of cloud servers based on the 'maxsessionrate' setting.</td>
    </tr>
    <tr>
        <td nowrap>--autoscaledown &lt;true|false&gt;</td>
        <td>Enables or disables automatically scaling down the number of cloud servers based on the 'maxsessionrate' setting.</td>
    </tr>
    <tr>
        <td nowrap>--setsize &lt;n&gt;</td>
        <td>Sets the current number of cloud servers to use.</td>
    </tr>
    <tr>
        <td nowrap>--maxsessionrate &lt;n&gt;</td>
        <td>Sets the session rate threshold for autoscaling.</td>
    </tr>
    <tr>
        <td>-h, --help</td>
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

