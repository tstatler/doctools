
# publish -- Publish a Node.ACS Application

## Description

Publish and run an application on Node.ACS cloud. If the application has been
previously published, publishing again will fail. But you can use the **--force**
option to overwrite a previously published application.  

You must run this command in the application's root directory, or specify the
application's directory with the **-d** option. 

## Usage

`$ acs publish` [ _options_ ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr> 
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>--force</td>
            <td>Overwrite previously published application in the cloud.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>


## Example
    
    $ acs publish
    
    Executing: publish
    [DEBUG] ready to publish
    [DEBUG] publishing...
    App MyProject published.
    App will be available at http://50a48e12aa4554c56a10029d.cloudapp.appcelerator.com
    
    

