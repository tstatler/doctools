
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

## Parameters

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
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to.  This parameter is required
            if the target application has the same name as an application in another organization 
            you belong to.
             </td>
        </tr>
    </tbody>
</table>

## Examples

The following un-publishes the deployed and active version of the application named `MyProject`:

    $ acs unpublish MyProject
    
    App MyProject version 0.1.0 is now marked for unpublication

The following un-publishes version 0.3.0 of the ChatApp application located in the `myprojects/chatapp/` folder:

    $ cd myprojects/chatapp
    $ acs unpublish  --ver 0.3.0
    
    App ChatApp version 0.3.0 is now marked for unpublication.

The following uses the `--org` parameter to un-publish the active version of the ChatApp application 
that belongs to the organization with the ID of **12345**. 

    $ cd myprojects/chatapp
    $ acs unpublish  --org 12345
    
    App ChatApp version 0.3.0 is now marked for unpublication.

