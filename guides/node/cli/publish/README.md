
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
    
    Preparing application for publish... done
    Packing application... done
    Publishing to cloud...
    [##########################################################################] 100%
    Prepare to load node modules
    Start loading node modules...
    node_modules loading starts...
    node_modules installation starts...
    node_modules loading completed...
    Node modules are loaded. Cleaning up...
    Done loading node modules!
    App MyProject published.
    App will be available at http://bb023745a993f41e38cb35ac7dfdca9947d64873.cloudapp.appcelerator.com
