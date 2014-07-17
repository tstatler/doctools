
# add -- Add a New Route or Service

## Description

Adds a new route or service to an existing application. The _name_ parameter specifies the new the 
route's name, as well as the name of the handler function. For example, running `acs add myservice` 
is equivalent to manually adding the following route and handler to your Node.ACS project's config.json and services.js file, respectively:

**config.json**:

    {
        "path": "/myservice", 
        "method": "get", 
        "callback": "services#myservice"
    }


**controllers/services.js**

    function myservice(req, res) {
        res.send('Hello, world!');
    };
    
## Usage

The command can be run in application's root directory, or you can specify the
application's directory with '-d' option. 

`$ acs add`  _name_  [ -d _app_directory_ ]

**Login Required:** No

## Parameters

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
        <tr>
            <td><code>-d</code>, <code>--dir</code> <em>path/to/app_directory</em></td>
            <td>Specifies the application to add a route to.</td>
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example
    
    $ acs add myservice
    
    New service added to /home/user/MyProject/controllers/services.js
    Route added to /home/user/MyProject/config.json
    

