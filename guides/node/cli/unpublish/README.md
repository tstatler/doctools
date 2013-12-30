
# unpublish -- Unpublish an Application

## Description

By default, unpublishes the currently deployed and active application, shutting the application down
and deleting it from the Node.ACS cloud. You can also unpublish a specific version with the `--ver`
option, regardless of whether it is deployed or not. For more information about publishing
application versions, see the [publish](#!/guide/node_cli_publish) command.

The local application directory is not removed after an unpublish operation, so you can republish
the application again with the [publish](#!/guide/node_cli_publish) command.

## Usage

<code>
$ acs unpublish [ <em>appname</em> |\--dir <em>app_dir</em>] [\--ver <em>version</em>]
</code>

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

<!-- ## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>

    </tbody>
</table> -->

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code><em>appname</em></code></td>
            <td>Name of the app to be unpublished. If omitted, the command needs to be run
                in application's root directory, or the application's directory must be specified with the 
                <code>-d</code> or <code>--dir</code> option.</td>
        </tr>        
        <tr>
            <td><code>--ver <em>version</em></code></td>
            <td>Unpublishes the version of the application specified by <em>version</em>. 
            If not specified, the currently deployed version is unpublished.</td>
        </tr>
    </tbody>
</table>

## Examples

The following un-publishes the deployed and active version of the application named `MyProject`:

    $ acs unpublish MyProject
    
    App 'MyProject' is now marked for unpublication.

The following un-publishes version 0.3.0 of the ChatApp application located in the `myprojects/chatapp/` folder:

    $ cd myprojects/chatapp
    $ acs unpublish  --ver 0.3.0
    
    App 'ChatApp' is now marked for unpublication.



