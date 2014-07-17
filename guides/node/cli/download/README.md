# download-- Downloads Application Source Files

## Description

Downloads application source files for the specified Node.ACS application name and version.

**Login Required:** Yes

## Usage

<code>
acs download [--ver <em>appVersion</em>] [--path <em>folderPath</em>] [appname]
</code>


## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>--ver</code></td>
            <td>The version of the application to download. If omitted, the currently deployed and active version is downloaded.</td>
        </tr>
        <tr>
            <td><code>--path</code></td>
            <td>An existing local path to save downloaded application source files. If omitted, files are saved to the current working directory. </td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to. This parameter only is required if the target application has the same name as an application in another organization you belong to.
             </td>
        </tr>
        <tr>
            <td><code>appname</code></td>
            <td>The name of the application. If omitted, you must run the command from the application's root directory, or specify the application's directory with the <code>-d</code> or <code>--directory</code> options.</td>
        </tr>
    </tbody>
</table>

## Examples

Downloads the currently deployed and active version of the application named **testapp** to the current working directory:

    $ acs download testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    App name: testapp Version: 0.2.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'testapp_0.2.0.tar.gz'
    ########## 15%

Downloads version **0.2.0** of **testapp** to the current working directory:

    $ acs download --ver 0.2.0 testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    App name: testapp Version: 0.2.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'testapp_0.2.0.tar.gz'
    ########################### 38%

Downloads version **0.1.0** of **testapp** to the the **`acs`** folder:

    $ acs download --ver 0.1.0 --path ./acs testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    App name: testapp Version: 0.1.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'acs/testapp_0.1.0.tar.gz'
    ###### 9%

Attempts to download a non-existent application:

    $ acs download does_not_exist
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    [ERROR] App not found! 

Downloads the application named **testapp** that belongs to the organization with the ID of **12345**:

    $ acs download testapp --org 12345
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    [ERROR] App not found!     
