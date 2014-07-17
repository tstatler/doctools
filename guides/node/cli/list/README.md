
# list -- List Applications

## Description

Shows a list of applications owned by the current user. By default, data is listed for all applications. 
You can specify an application name to only show details for that application. The information returned
by this command also includes error messages, if any, related to the application's deployment and execution. 

For Appcelerator Platform users,
applications are grouped by the Appcelerator Platform [organization](#!/guide/node_orgs) that they belong to (see [Examples](#!/guide/node_cli_list-section-examples)). 
If you've created applications that are not assigned to any organization, they are included in a group named "Not Assigned".

The following fields are displayed for each application:

* **Created by** &mdash; Email of user that created application.
* **URL** &mdash; URL of application.
* **Created at**  &mdash; Date the application was created.
* **Node Version**  &mdash; Node version used to run the application (see [Node.js Engine](#!/guide/node_standard-section-node-js-engine))
* **Maximum allowed number of servers**  &mdash; By default, this is set to **1**. Contact Appcelerator Support to increase this value.
* **Desired number of servers**  &mdash; Number of servers specified by the `--setsize` parameter of the 
[config](#!/guide/node_cli_config) command.
* **Current number of deployed servers**  &mdash; Number of servers currently in use.
* **Active version** &mdash;  Version of the currently active application. Use the [publish](#!/guide/node_cli_publish) command to change the version.
* **Published at** &mdash;  Date the application was published. Not shown if application hasn't been published.
* **Servers** &mdash; List of servers in use and their current status.

## Usage

`$ acs list` [ _appname_ | -h ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>--mine</td>
            <td>Only list apps created by the current user. Only available for Appcelerator Platform users.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>Lists applications of the specified organization ID. Only available for Appcelerator Platform users with Node.ACS access.</td>
        </tr>
        <tr>
            <td><i>appname</i></td>
            <td>Name of the app to list information for.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Examples

The following example only applies for Appcelerator Platform users.

In this example the current user owns two applications that belong to the "Appcelerator, Inc" 
organization, one that belongs to the "Acme, Inc" organization, and one that isn't assigned to any
organization. The organization ID is shown in parentheses next to the organization name; for applications
not assigned to an organization, the ID of the current user is shown in parentheses.
    
    $ acs list
    
    Organization: Appcelerator, Inc (14301)
    ============ 

    App name: app_1
     -- Created by: user1@appcelerator.com
     -- URL: https://1610c7c3912b2cddb5sdfsd2bf6ea66752a26f70a.cloudapp-enterprise.appcelerator.com
     -- Created at: Tue Apr 29 2014 12:57:40 GMT-0700 (PDT)
     -- Node Version: 0.10.22
     -- Maximum allowed number of servers: 1
     -- Desired number of servers: 1
     -- Current number of deployed servers: 1
     -- Active version: 0.1.0
     -- Published at: Tue Apr 29 2014 13:43:26 GMT-0700 (PDT)
     -- Servers: 
        No. 1   ID: 53114092321c3a5e3dd971e3    Status: Deployed


    App name: app_2
     -- Created by: anotherone@appcelerator.com
     -- Created at: Sun Dec 29 2013 16:03:49 GMT-0800 (PST)
     -- Node Version: 0.10.22
     -- Status: To be published

    Organization: Acme, Inc (12346)
    ============ 
     
    App name: someapp
     -- Created by: anotherone@appcelerator.com
     -- Created at: Sun Mar 16 2014 06:08:05 GMT+0800 (CST)
     -- Node Version: 0.10.22
     -- Status: To be published


    Organization: Not Assigned (526a27a8fe0c8a39d6b14b2e)
    ============ 
     
    App name: newApp9
     -- Created by: user1@appcelerator.com
     -- Created at: Sun Mar 16 2014 06:08:05 GMT+0800 (CST)
     -- Node Version: 0.10.22
     -- Status: To be published

The following example lists applications that belong to the organization with the ID of **14301**.

    $ acs list --org 14301

    Organization: Appcelerator, Inc (14301)
    ============ 

    App name: app_1
     -- Created by: user1@appcelerator.com
     -- URL: https://1610c7c3912b2cddb5sdfsd2bf6ea66752a26f70a.cloudapp-enterprise.appcelerator.com
     -- Created at: Tue Apr 29 2014 12:57:40 GMT-0700 (PDT)
     -- Node Version: 0.10.22
     -- Maximum allowed number of servers: 1
     -- Desired number of servers: 1
     -- Current number of deployed servers: 1
     -- Active version: 0.1.0
     -- Published at: Tue Apr 29 2014 13:43:26 GMT-0700 (PDT)
     -- Servers: 
        No. 1   ID: 53114092321c3a5e3dd971e3    Status: Deployed


    App name: app_2
     -- Created by: anotherone@appcelerator.com    
     -- Created at: Sun Dec 29 2013 16:03:49 GMT-0800 (PST)
     -- Node Version: 0.10.22
     -- Status: To be published

The following example lists applications that were created by the current user (user1@appcelerator.com).

    $ acs list --mine

    Organization: Appcelerator, Inc (14301)
    ============ 

    App name: app_1
     -- Created by: user1@appcelerator.com
     -- URL: https://1610c7c3912b2cddb5sdfsd2bf6ea66752a26f70a.cloudapp-enterprise.appcelerator.com
     -- Created at: Tue Apr 29 2014 12:57:40 GMT-0700 (PDT)
     -- Node Version: 0.10.22
     -- Maximum allowed number of servers: 1
     -- Desired number of servers: 1
     -- Current number of deployed servers: 1
     -- Active version: 0.1.0
     -- Published at: Tue Apr 29 2014 13:43:26 GMT-0700 (PDT)
     -- Servers: 
        No. 1   ID: 53114092321c3a5e3dd971e3    Status: Deployed

    Organization: Not Assigned (526a27a8fe0c8a39d6b14b2e)
    ============ 
     
    App name: newApp9
     -- Created by: user1@appcelerator.com
     -- Created at: Sun Mar 16 2014 06:08:05 GMT+0800 (CST)
     -- Node Version: 0.10.22
     -- Status: To be published        

