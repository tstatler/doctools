
# login -- Login to Node.ACS

## Description

An interactive command that will prompt for username and password to login to
Node.ACS.

## Usage

`$ acs login` [ -h ] [ _username_ [, _password_ ]]

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>username</i></td>
            <td>Username for a Node.ACS user account. If not specified, **acs** prompts for the username.</td>
        </tr>
        <tr>
            <td><i>password</i></td>
            <td>Password for the Node.ACS user account. If not specified, **acs** prompts for the password.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example
    
    $ acs login
    
    Executing: login
    username: sam@nodeacs.com
    password: ********
    Welcome back, Sam! You are now logged in.
    
