# download-- Dlw

## Description

Downloads the source files for the specified application name version. 

**Login Required:** Yes

## Usage

<pre class="prettyprint">
acs download [options] [<i>appname</i>]
</pre>


## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>appname</i></td>
            <td>The name of the application. If omitted, you must run the command from the application's root directory, or specify the application's directory with the <code>-d</code> option.</td>
        </tr>
        <tr>
            <td><i>version</i></td>
            <td>The version of the application to download. If omitted, the currently deployed and active application is downloaded.</td>
        </tr>
    </tbody>
</table>

## Examples
    
	$ acs crt --add customapp.com.pem
    $ acs crt --add customapp.com.pem MyApp
    $ acs crt --remove
    $ acs crt --remove -d ../apps/myapp
