
# new -- Create a New Application

## Description

Create a new Node.ACS application. A new application directory will be created
in current working directory, or in desired location specified by '-d' option.  
The new application directory's name will be the same as the application's. If
a folder with the name already exists, the command will be failed, then you
might need to consider to change working directory or rename the existing
folder.  

By default, **new** creates an application that uses the Node.ACS MVC framework. 
To create a standard Node.js application, call **new** with the **--framework none**
option.

## Usage

`$ acs new` [_options_] _name_

**Login Required:** Yes  (See [login](#!/guide/node_cli_login) command)

## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>name</td>
            <td>The name of new application</td>
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
            <td>--framework none</td>
            <td>Create the new app with standard node.js sample</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information of the command</td>
        </tr>
    </tbody>
</table>

## Example

    
    
    $ acs new MyProject
    
    Executing: new
    [DEBUG] Creating project at: /home/user/MyProject
    New project created at /home/user/MyProject
    

