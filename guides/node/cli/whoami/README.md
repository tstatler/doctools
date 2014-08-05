
# whoami -- Shows the current logged-in user

## Description

Shows the current logged-in user. If you are an Appcelerator Platform user, this command shows the
organizations you belong to.

## Usage

`$ acs whoami`

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>--output &lt;format&gt;</code></td>
            <td>Sets the output format.  Set to either <b>report</b> for human-readable format
                or <b>json</b> for JSON output.  Defaults to <b>report</b>.
             </td>
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

The following example displays information about the currently logged-in user if they do not belong
to an organization.

    $ acs whoami
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.16
    Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.

    email        jdoh@foo.com
    firstname    Jon
    lastname     Doh


The following example displays information about the current logged-in user if they belong to an
organization.
    
    $ acs whoami
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.16
    Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.

    username     jdoh@foo.com
    email        jdoh@foo.com

    Organization(s) you belong to:

    ID:  99999      Name:  Foo, Inc         Node.ACS Admin:  false
    ID:  99998      Name:  Foo, LLC         Node.ACS Admin:  false
    ID:  99997      Name:  Foo, Ltd         Node.ACS Admin:  true


