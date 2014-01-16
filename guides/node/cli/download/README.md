# download-- Downloads an Application

## Description

Downloads the source files for the published application name and version from ACS.

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
	    <td>The version of the application to download. If omitted, the source files for the currently deployed and active versions are downloaded.</td>
	</tr>
	<tr>
	    <td><code>--path</code></td>
	    <td>An existing local path to save downloaded application source files. If omitted, the path </td>
	</tr>
	<tr>
	    <td><code>appname</code></td>
	    <td>The name of the application. If omitted, you must run the command from the application's root directory, or specify the application's directory with the <code>-d</code> option.</td>
	</tr>
    </tbody>
</table>

## Examples

    $ acs download testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    Admin Hostname: http://localhost
    App name: testapp Version: 0.2.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'testapp_0.2.0.tar.gz'
    ########## 15%

    $ acs download --ver 0.2.0 testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    App name: testapp Version: 0.2.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'testapp_0.2.0.tar.gz'
    ########################### 38%

    $ acs download --ver 0.1.0 --path ./acs testapp
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    Admin Hostname: http://localhost
    App name: testapp Version: 0.1.0
    – Request sent, awaiting response...
    – Length: 13825281 (13502K)
    – Saving to: 'acs/testapp_0.1.0.tar.gz'
    ###### 9%

    $ acs download does_not_exist
    ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.12
    Copyright (c) 2012-2014, Appcelerator, Inc. All Rights Reserved.
    Admin Hostname: http://localhost
    [ERROR] App not found!