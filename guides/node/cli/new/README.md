
# new -- Create a New Application

## Description

Creates a new Node.ACS application. A new application directory will be created
in the current working directory, or in the location specified by the `-d` or `--dir` options. The 
application directory's name will match the specified application name. If a folder with the 
specified name already exists, the command will fail. 

By default, this command creates an application that uses the [Node.ACS MVC Framework](#!/guide/node_mvc). 
To create a [standard Node.js applications](#!/guide/node_standard) without the MVC framework, 
pass the **--framework none** CLI option. 

If the user creating the application belongs to just one Platform [organization](#!/guide/node_orgs), 
the application is assigned automatically to that organization. If the user belongs to more than one organization, 
they are prompted to choose an organization. See [Examples](#!/guide/node_cli_new-section-example).

## Usage

`$ acs new` [_options_] _name_

**Login Required:** Yes  (See [login](#!/guide/node_cli_login) command)

## Parameters

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
        <tr>
            <td><code>--framework</code> none</td>
            <td>Create a standard Node.js application with the Node.ACS 
            <a href="/cloud/latest/#!/guide/node_mvc">MVC framework</a>.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization to associate the application with. Only available for Appcelerator Platform users with Node.ACS access.</td> 
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
            <td>Show help information for the command.</td>
        </tr>
    </tbody>
</table>

## Example

In the following example, the current user belongs to a single organization so the application is automatically assigned to that organization. 

    $ acs new MyProject
    
    [DEBUG] Creating project at: /home/user/MyProject
    New project created at /home/user/MyProject

In the following example the user belongs to two organizations, "Appcelerator, Inc" and "Appceleator Support", 
and is prompted to select an organization from a list.
    
    $ acs new MyApp

    You belong to more than one organization. Please select an organization:
      1) Appcelerator, Inc (14301)
      2) Appcelerator Support (100000424)
      : 1

    Creating new Node.ACS app for organization Appcelerator, Inc (14301)...
    New project created at /projects/MyApp

The following example creates a standard Node.js application without the Node.ACS MVC framework. 

    $ acs new StandardApp --framework none
    
    [DEBUG] Creating project at: /home/user/StandardApp
    New project created at /home/user/StandardApp
