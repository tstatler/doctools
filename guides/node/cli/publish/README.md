
# publish -- Publish a Node.ACS Application

## Description

Publishes and runs an application on the Node.ACS cloud. You can publish up to three versions of
your Node application, and choose the active and deployed version from the available published
versions. This command also lists all currently published versions and the currently deployed
version.

You must run this command from the application's root directory, or specify the application's
directory with the **--dir** or **-d** option.


### About publishing application versions ###

You can publish up to three different versions of your application to the Node.ACS cloud. Only one
version may be deployed and active at a time. The application version number is determined by the
`version` field of your application's package.json file.

Applications you create with the [`acs
new`](http://docs.appcelerator.com/cloud/latest/#!/guide/node_cli_new)  command have the version **0.1.0**, by default.

You use the `--list_versions` option to list an application's currently published versions, and the
currently deployed version, if any:

```
> acs publish --list_versions
Published versions: 0.1.0, 0.2.0. The version is deployed currently: 0.2.0.`
```

If no version is currently deployed, the output will specify that (see examples below).

To change the currently deployed and active version, add the `--set_active_version` option followed
by the version to deploy. For example, the following deploys version 0.3.0 of the specified
application:

```
> acs publish --set_active_version 0.3.0
Published versions: 0.1.0, 0.2.0., 0.3.0 The version is deployed currently: 0.3.0.`
```

When you publish a new version of an application it becomes the deployed and active application. By
default, you cannot republish a version of an application that was previously published. Use the
**\--force** command option to force republish of the application (see example below).

When a version is republished it becomes the active and deployed version, regardless of whether it's
active or not currently.

You can un-publish a specific version of an application, whether it's currently deployed or not. See the 
[unpublish](#!/guide/node_cli_unpublish) command for details.

### About publishing applications with identical names in different organizations  ###

If you have created an application with the same name in different [organizations](#!/guide/node_orgs), 
and try to publish one of them, the CLI will generate an error:

    $ acs publish -d newApp
     
    [ERROR] There are multiple apps with name 'newApp' in different organizations. Please specify an organization.

To resolve this issue, use the `--org` parameter to specify the ID of the organization from which the application should be published:

    acs publish -d newApp --org 12345
     
    Preparing application for publish... done
    Packing application... done
    Publishing to cloud...
    [##########################################################################] 100%
    ...

You can run the [`list`](#!/guide/node_cli_list) CLI command to determine which organizations 
you belong to.

## Usage ##

<pre><code>
$ acs publish [-d | --dir <em>application-directory</em> ] 
              [ --list_versions ] 
              [ --set_active_version <em>version</em>] 
              [ --force ] [-h | --help]</code></pre>

**Login Required:** Yes (See [login](#!/guide/node_cli_login) command)

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr> 
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>--d, --dir <em>application-directory</em></code></td>
            <td>Specifies the directory of the application to publish. When omitted, 
            the command must be run from the application directory.</td>
        </tr>
        <tr>
            <td><code>--force</code></td>
            <td>Required when publishing a version of an application that's already been published. </td>
        </tr>
        <tr>
            <td><code>--list_versions</code></td>
            <td>List all published versions of the application, and the version deployed currently, if any.</td>
        </tr>
        <tr>
            <td><code>--org</code></td>
            <td>The ID of the organization the application belongs to. You only need to this parameter
            if you have published an application with the same name to multiple organizations.
             </td>
        </tr>
        <tr>
            <td><code>--set_active_version <em>version</em></code></td>
            <td>Set the currently deployed and active version of the application to <code><em>version</em></code>.</td>
        </tr>
        <tr>
            <td><code>-h</code>, <code>--help</code></td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>


## Examples

The following publishes the Node.ACS application in the current working directory.
    
    $ acs publish
    
    Preparing application for publish... done
    Packing application... done
    Publishing to cloud...
    [##########################################################################] 100%
    Prepare to load node modules
    Start loading node modules...
    node_modules loading starts...
    node_modules installation starts...
    node_modules loading completed...
    Node modules are loaded. Cleaning up...
    Done loading node modules!
    App MyProject version 0.1.0 published.
    App will be available at http://bb023745a993f41e38cb35ac7dfdca9947d64873.cloudapp.appcelerator.com

The following re-publishes the same version of the Node.ACS application located in the `chatapp/` directory:
    
    $ acs publish --force -d chatapp/
    
    Preparing application for publish... done
    Packing application... done
    Publishing to cloud...
    [##########################################################################] 100%
    Prepare to load node modules
    Start loading node modules...
    node_modules loading starts...
    node_modules installation starts...
    node_modules loading completed...
    Node modules are loaded. Cleaning up...
    Done loading node modules!
    App ChatApp version 0.2.0 published.
    App will be available at http://bb023745a993f41e38cb35ac7dfdca9947d123456.cloudapp.appcelerator.com


The following lists the published versions and the currently deployed version: 

    $ acs publish --list_versions

    Published versions: 0.1.0, 0.2.0. The version deployed currently: 0.2.0.

In the following example there are three published versions but no currently deployed version:

    $ acs publish --list_versions

    Published versions: 0.1.0, 0.2.0, 0.3.0. No version is deployed currently.

The following sets the active and deployed version of the current application to 1.0.1

    $ acs publish --set_active_version 1.0.1

    Published versions: 1.0.0, 1.0.1. The version deployed currently: 1.0.1.
