
# cname -- Set Custom Domain Name For an Application

## Description

Binds a CNAME to a published application, so that the application can be accessed
using a custom domain as an alias for the application's `cloud.appcelerator.com` URL.  

The alias to set should be a valid domain name that has been already configured 
with a CNAME record pointing to the published application's URL. Node.ACS validates 
the CNAME record before binding it to the application.  

If a CNAME has already been bound to the application, setting the CNAME again
overwrites the previous setting.

To route an application based on a path with the domain name, use the `--path <path_name>` parameter to set a path for the
application after setting a CNAME.  For example, if you want to bind two applications to the same
CNAME, specify a path for each to route a client to the correct application.

## Usage

`$ acs cname` [ _options_ ] [ _appname_ ]

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Required Parameters

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
            <td>--check</td>
            <td>Check the current CNAME setting.</td>
        </tr>
        <tr>
            <td>--path <i>path_name</i></td>
            <td>Specifies a URL path for routing. Use this parameter when setting more than one
                application to the same domain name.  Set the CNAME first.
            </td>
        </tr>
        <tr>
            <td>--set <i>domain_name</i></td>
            <td>Set CNAME binding for the application to the specified domain name. A CNAME record must exist for the specified domain name,
                pointing to the application's `cloud.appcelerator.com` URL. Do not specify the
                protocol, that is, do not add `http://` or `https://`, when setting this parameter.
            </td>
        </tr>
        <tr>
            <td>--remove</td>
            <td>Remove CNAME binding from the application.</td>
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

The following example allows the application to be accessed from `my.nodeacs.com`:

    acs cname --set my.nodeacs.com
    
The following example allows the LegacyApp application to be accessed from `my.node.acs.com/v1` and
the BrandNewApp application to be accessed from `my.node.acs.com/v2`:

    acs cname --set my.nodeacs.com LegacyApp
    acs cname --path v1 LegacyApp
    acs cname --set my.nodeacs.com BrandNewApp
    acs cname --path v2 BrandNewApp
