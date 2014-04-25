
# login -- Login to Node.ACS

## Description

Command for logging in to Node.ACS using your Appcelerator Network account credentials. 
[Sign-up](https://my.appcelerator.com/auth/signup) for a free account if you don't have one.

## Usage

`$ acs login` [ _username_ ] [ _password_ ]

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>username</i></td>
            <td>Your Appcelerator Network account user name. If not specified, you are prompted for the username.</td>
        </tr>
        <tr>
            <td><i>password</i></td>
            <td>Your Appcelerator Network account password. If not specified, you are prompted for the password.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

The following example specifies the username and password in the command:

    $ acs login nobody@appceleator.com mypassword

    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.14
    Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.

    Welcome back, Nobody! You are now logged in.

In the following example the CLI prompts the user to enter their username and password:

    $ acs login

    username: nobody@appceleator.com
    password: ********
    
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.14
    Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.

    Welcome back, Nobody! You are now logged in.
