
# list -- List Applications

## Description

Shows a list of applications owned by the current user. If an
application has been deployed, the information will published date
and current status (such as published, running, or deploying).

If an application name is specified, shows only the named application's
information; otherwise, shows information for all of the user's applications.

The returned application information also includes any error messages
related to deploying and running the application. 

## Usage

`$ acs list` [ _appname_ | -h ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
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

## Example
    
    $ acs list
    
    App name: MyProject
     -- URL: http://50a48e10bd4554c56a01029d.cloudapp.appcelerator.com
     -- Created at: Thu Nov 15 2012 14:39:12 GMT+0800 (CST)
     -- Published at: Thu Nov 15 2012 15:39:57 GMT+0800 (CST)
     -- Status: Starting to Deploy
    
    App name: test
     -- Created at: Wed Nov 14 2012 12:02:03 GMT+0800 (CST)
    
    App name: demo
     -- URL: http://509cc1410795842b40000001.cloudapp.appcelerator.com
     -- Created at: Fri Nov 09 2012 16:38:25 GMT+0800 (CST)
     -- Published at: Fri Nov 09 2012 16:38:49 GMT+0800 (CST)
     -- Status: Deploying
    
    App name: mywebapp
     -- URL: http://509cc1410634235b405d0034.cloudapp.appcelerator.com
     -- Created at: Fri Nov 04 2012 16:38:25 GMT+0800 (CST)
     -- Published at: Fri Nov 04 2012 20:18:49 GMT+0800 (CST)
     -- Status: Running
    

