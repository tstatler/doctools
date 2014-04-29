
# new -- Create a New Application

## Description

Creates a new Node.ACS application. A new application directory will be created
in the current working directory, or in the location specified by the '-d' option. The new application 
directory's name will be the same as the application's. If a folder with the name already exists, the command will fail. 

By default, the **new** command creates an application that uses the Node.ACS MVC framework. 
To create a standard Node.js application, call **new** with the **--framework none**
option. For more information, see [Node.ACS MVC Framework](/cloud/latest/#!/guide/node_mvc) 
and [Standard Node.js Applications](/cloud/latest/#!/guide/node_standard).

### Appcelerator Platform Notes ###

For Appcelerator Platform users, a new Node.ACS application must be assigned to a 
[Dashboard organization](http://docs.appcelerator.com/platform/latest/#!/guide/Managing_Organizations). 
If the user creating the application belongs to just one organization it's assigned 
automatically to that organization. If the user belongs to more than one organization, 
they are prompted to choose an organization for the application. 

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

In the following example, the current user belongs to a single organization, so the application 
is automatically assigned to that organization without prompting. 

    $ acs new MyProject
    
    [DEBUG] Creating project at: /home/user/MyProject
    New project created at /home/user/MyProject

In this example the current user belongs to two organizations
    
    $ acs new MyApp

    You belong to more than one organization. Please select an organization:
      1) Appcelerator, Inc (14301)
      2) Appcelerator Support (100000424)
      : 1

    Creating new Node.ACS app for organization Appcelerator, Inc (14301)...
    New project created at /projects/MyApp
