
# unpublish -- Unpublish an Application

## Description

Unpublish an application from Node.ACS cloud. As soon as the command is
executed, the application will be shutdown and removed from the cloud.  
Local application directory will not be removed after unpublish, it can be
published again by using [publish](#!/guide/node_cli_publish) command.

## Usage

`$ acs unpublish` [ -h ] [ _appname_ | -d _app_dir_ ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>appname</i></td>
            <td>Name of the app to be unpublished. If omitted, the command needs to be run
                in application's root directory, or the application's directory must be specified with
                the **-d** option.</td>
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
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

    $ acs unpublish
    
    App 'MyProject' is now marked for unpublication.
    

