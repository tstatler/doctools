
# add -- Add a New Route or Service

## Description

Adds a new route or service to an existing application. This command is a
utility that helps you to quickly add a new route and handler to your Node.ACS MVC
framework application. 

The _name_ argument specified on the command line is used as the route's name as well
as the name of the handler function

You can also add a new route and handler manually by doing the following:

*    Add a new route item into `config.json`:  

        {"path": "/myservice", "method": "get", "callback": "services#myservice"}

*    Add a new route handler (function) into `/controllers/services.js`

        function myservice(req, res) {
            res.send('Hello, world!');
        };
    
## Usage

The command can be run in application's root directory, or you can specify the
application's directory with '-d' option. 

`$ acs add`  _name_  [ -d _app_directory_ ]

**Login Required:** No

## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>name</i></td>
            <td>Name of the new route/service to add.</td>
        </tr>
    </tbody>
</table>

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>-d <i>app_directory</i></td>
            <td>Specifies the application to add a route to.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table

## Example
    
    $ acs add myservice
    
    Executing: add
    New service added to /home/user/MyProject/controllers/services.js
    Route added to /home/user/MyProject/config.json
    

