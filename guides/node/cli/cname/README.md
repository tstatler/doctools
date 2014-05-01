
# cname -- Set Custom Domain Name For an Application

## Description

Binds a CNAME to a published application, so that the application can be accessed
using a custom domain as an alias for the application's `cloud.appcelerator.com` URL.  

The alias to set should be a valid domain name that has been already configured 
with a CNAME record pointing to the published application's URL. Node.ACS validates 
the CNAME record before binding it to the application.  

If a CNAME has already been bound to the application, setting the CNAME again
overwrites the previous setting.

## Usage

`$ acs cname` [ _options_ ] [ _appname_ ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>appname</td>
            <td>The name of the app to set CNAME for. If omitted, the command needs to be run in application's root directory, or specify the application's directory with '-d' option.</td>
        </tr>
        <tr>
            <td><code>--set</code> <em>domain_name</em></td>
            <td>Set CNAME binding for the application to the specified domain name. A CNAME record must exist for the specified domain name,
                pointing to the application's `cloud.appcelerator.com` URL.</td>
        </tr>
        <tr>
            <td><code>--remove</code></td>
            <td>Remove CNAME binding from the application.</td>
        </tr>
        <tr>
            <td><code>--org <em>orgID</em></code></td>
            <td>The ID of the organization the application belongs to. This parameter only is required if the target application has the same name as an application in another organization you belong to.
             </td>
        </tr>
        <tr>
            <td>-d <i>app_directory</i></td>
            <td>Specifies the application by its directory.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

    $ acs cname --set my.nodeacs.com
    
    Set CNAME succeed. App will be available at: my.nodeacs.com
    
    $ acs cname --set my.nodeacs.com
    
    Set CNAME succeed. App will be available at: my.nodeacs.com

