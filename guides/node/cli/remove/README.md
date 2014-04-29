
# remove -- Delete an Application

## Description

Remove an application. If the application has been published, the command 
unpublishes the application first, then removes it.  

The local application directory is not deleted by default. Use the 
**--force** option to delete it.

## Usage

`$ acs remove` [ _options_ ] [ _appname_ ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>appname</td>
            <td>The name of the app to remove. If omitted, you must run the command in the application's root directory,
                 or specify the application's directory with '-d' option.</td>
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
            <td>--force</td>
            <td>Remove local application directory. The application must be specified using 
                the _appname_ argument or **-d** option which specifies the target application directory, 
                or the command is running in application's root directory.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to.  This parameter is required
            if the target application has the same name as an application in another organization 
            you belong to.
             </td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

The following example remove the project named **MyProject**.

    $ acs remove MyProject
    
    Remove app: MyProject
    MyProject has been successfully deleted.

The following example remove the project named **MyProject** from the organization with the ID of **12345**.

    $ acs remove MyProject --org 12345
    
    Remove app: MyProject
    MyProject has been successfully deleted.
    
