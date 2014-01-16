
# Command-Line Interface

Node.ACS provides a simple command-line interface, **acs**, for creating and
administering Node.ACS applications.

**acs** requires Node.js version 0.8.13 or greater. If you don't have a suitable version of Node installed, please visit: [http://nodejs.org](http://nodejs.org/) to install or upgrade Node.

Once Node is installed, run the following command to install **acs**.
    
    npm install -g acs

Depending on how Node is installed, you may need to run the install command as
an administrator:
    
    sudo npm install -g acs

## CLI Commands

**acs** provides 14 commands for you to create, manage Node.ACS applications, command usage of these commands is like the following: 
    
    acs [_COMMAND_] [_COMMON OPTIONS_] [_COMMAND OPTIONS_]

Running `acs --help` will give you a full list of commands usage, you can also
run `acs _COMMAND_ --help` to get the usage of a specific command.

Here is a list of available commands and brief description for each of them:

<table class="doc_content_table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_accesslog"><b>accesslog</b></a></td>
            <td>List application's access log</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_add"><b>add</b></a></td>
            <td>Add a new route/service</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_cname"><b>cname</b></a></td>
            <td>Set a CNAME for an application</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_config"><b>config</b></a></td>
            <td>Configures cloud servers for the application</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_crt"><b>crt</b></a></td>
            <td>Manages SSL certificates for the application</td>
        </tr>
        <tr>
	    <td><a href="#!/guide/node_cli_download"><b>download</b></a></td>
	    <td>Download the Node.ACS application source files with specified version.</td>
	</tr>
	<tr>
            <td><a href="#!/guide/node_cli_list"><b>list</b></a></td>
            <td>List all applications</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_logcat"><b>logcat</b></a></td>
            <td>Tail active application logs</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_loglist"><b>loglist</b></a></td>
            <td>List application logs</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_login"><b>login</b></a></td>
            <td>Login to Node.ACS</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_logout"><b>logout</b></a></td>
            <td>Log out of Node.ACS</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_new"><b>new</b></a></td>
            <td>Create new application</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_publish"><b>publish</b></a></td>
            <td>Publish application to Node.ACS cloud</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_remove"><b>remove</b></a></td>
            <td>Remove an application</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_run"><b>run</b></a></td>
            <td>Run an application locally for dev./testing</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_unpublish"><b>unpublish</b></a></td>
            <td>Unpublish an application</td>
        </tr>
        <tr>
            <td><a href="#!/guide/node_cli_whoami"><b>whoami</b></a></td>
            <td>Show current login user</td>
        </tr>
    </tbody>
</table>


## Common CLI Options 


<table class="doc_content_table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show command usage information.</td>
        </tr>
        <tr>
            <td>-v, --version</td>
            <td>Show CLI version.</td>
        </tr>
        <tr>
            <td>-d, --dir <i>dir</i></td>
            <td>Specifies an application by its directory.</td>
        </tr>
        <tr>
            <td>-n, --no-colors</td>
            <td>Turn off coloring for command output.</td>
        </tr>
        <tr>
            <td>--no-banner</td>
            <td>Turn off banner for command output.</td>
        </tr>
        <tr>
            <td>--dates</td>
            <td>Turn on dates in log.</td>
        </tr>
    </tbody>
</table>

## Login with Appcelerator Credentials

It is important to have a user login session on your dev. environment since
most of the commands are about modifing your Node.ACS applications, so do a
user login before doing anything is recommended. User login can be done by
using [login](#!/guide/node_cli_login) command.

