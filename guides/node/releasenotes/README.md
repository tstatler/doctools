# Node.ACS Release Notes

## 6 December 2013 -- version 1.0.10

  * Fixed an issue where an application could not be published due to node-tar not generating the
    correct headers for certain NPM modules.

## 23 November 2013 -- version 1.0.9

  * Fixed an issue where the CLI was not working on Windows systems.

## 22 November 2013 -- version 1.0.8

  * New Node.ACS library method to make generic REST API calls to ACS.  For more information, see
    [Using ACS APIs from Node](http://docs.appcelerator.com/cloud/latest/#!/guide/node_acs).

  * Upgraded servers to Node v0.8.26.

  * Fixed an issue where the CLI help command did not print out usage information for the `acs crt`
    command.

  * Fixed an issue when trying to send truncated data with express compression.  For MVC apps, the
    server will try to reenable express compression.

  * Fixed an issue where uploading a certificate containing a domain name with wildcard characters
    would fail.

## 26 September 2013 -- version 1.0.7

  * Fixed an issue where using the ACS CLI with Node.js v0.10.14 did not display
    the correct error output when testing locally.

  * Changed the `accesslog`, `loglist` and `usage` commands to support
    a `--more` option to load results faster. The `--page_number` option is removed
    since results will not be pre-counted. Previously, results were pre-counted.

  * Fixed an issue where running `acs logcat` returned a 502 error.

  * Fixed an issue where a request to the sync server returned a truncated response.

## 15 August 2013 -- version 1.0.6

This update includes bug fixes and performance improvements.

## 1 August 2013 -- version 1.0.5

This update includes bug fixes and performance improvements.

## 22 July 2013 -- version 1.0.4

  * Updated "The app is being deployed" message to display the application name.

  * Added a check to prevent the application from including `acs` as a dependency.
    `acs` is automatically installed by the server when the application is deployed.
    This check was added to prevent possible version compatibility issues.

  * Fixed an issue where setting the CNAME with the protocol prefix (`http://` or `https://`)
    in the URL reported a 404 error. The CLI now reports the error as an invalid domain name.
    Do not include the protocol prefix when setting the CNAME.

## 13 June 2013 -- version 1.0.3

  * Fixed an issue to support proxies requiring authentication.

  * Added "The app is being deployed and will be available soon" message to all URL endpoints
    after an app is deployed.  Previously, only the main index would display this message and all
    other endpoints would show an error message.

  * Fixed an issue with the remove command to delete project files both locally and remotely.
    Previously, only the remote files were deleted and not the local files.

  * Fixed an issue where the list command did not indicate if an application failed to launch.

  * Fixed an issue where the usage command did not accurately report the memory usage.  Previously, the
    free memory would be reported lower than actual.


## 2 May 2013 -- version 1.0.2

Version 1.0.2 fixes an issue where the **acs list** command included some incorrect
information. 

This update includes a bug fix for the Node.ACS server. When an application receives an
unhandled exception, the process is terminated and restarted. This prevents the
application from hanging.

## 15 Apr 2013 -- Node.ACS GA

<p>The Node.ACS service is now a General Availability (GA) product. The new version of the Node.ACS CLI
is 1.0.0. For the GA release, we've created a new, production environment for
publishing your Node.ACS applications. </p>

<p>If you have existing Node.ACS applications created during the developer preview,
you must republish your existing applications to take advantage of the new
environment. See the instructions in the next section.</p>

<h4>Migrating Applications to the Production Environment</h4>

<p>To migrate existing applications to the new production environment:</p>
 
<ol>
<li><p>Update to the latest <b>acs</b> npm package.</p>
    <ul>
    <li>If you are using Node.ACS from the command line, run the following command:
    <pre>sudo npm install –g acs</pre>
    </li>
    <li> If you are using Node.ACS through Titanium Studio, you will be prompted
    to install an updated <b>acs</b> package the next time you launch Studio. To manually check for
    updates, in the menu bar, select <b>Help</b> > <b>Check for Titanium Updates</b>.
    </li>
    </ul>
    <p>Note that you cannot use older versions of the <b>acs</b> npm package to create or publish new
 Node.ACS services.</p>
 <li><p>Publish your existing apps with the updated package:
    <ul>
    <li><p>From the command line:</p>
    <pre>acs publish &lt;project name&gt; </pre>
    </li>
    <li><p>From Studio:</p>
    <ol>
    <li>Select the project.</li>
    <li>Click on the <b>Publish</b> icon.</li>
    <li>Click <b>Deploy App</b>.</li>
    </ol>
    </ul>
 </li>
 <li>Your app is published with the following URL:
 <pre>https://&ltappid&gt;.cloudapp.appcelerator.com
 </pre>
 </li>
 <li>If you have a custom CName set up for your application, modify your CName entry 
 to point to the new URL, then run the <b>acs cname</b> command to bind the CName with 
 your application.</li>

</ol>

<p>Your existing applications will continue to run in the preview environment for the
next month. Any applications still running in the preview environment will stop working
after that point. </p>

## 28 Mar 2013 -- version 0.9.34

<ul>
<li><p>Added new <b>acs usage</b> command to show a record of memory and CPU usage for a
published application. For example:</p>

<pre class="prettyprint">
$ acs usage MyProject

[Records] 7  [Pages] 1  [Current Page] 1
[02/26/2013 21:36:50.447]  memory: { free: 195.00M total: 256M }  loadavg: [ 10.79% ]
[02/26/2013 21:36:20.448]  memory: { free: 195.95M total: 256M }  loadavg: [ 17.97% ]
[02/26/2013 21:35:50.458]  memory: { free: 177.99M total: 256M }  loadavg: [ 27.49% ]
[02/26/2013 21:35:20.457]  memory: { free: 180.02M total: 256M }  loadavg: [ 32.28% ]
[02/26/2013 21:34:50.457]  memory: { free: 180.86M total: 256M }  loadavg: [ 40.28% ]
[02/26/2013 21:34:20.459]  memory: { free: 181.91M total: 256M }  loadavg: [ 40.23% ]
[02/26/2013 21:33:50.453]  memory: { free: 183.66M total: 256M }  loadavg: [ 40.19% ]
</pre>
<p>See the <a href="#!/guide/node_cli"><b>acs usage</b> reference page</a> for a list of options.</p>
</li>

<li><p>The ACS CLI is now compatible with Node.js 0.10.</p></li>

<li><p>Accessing an application URL while the app is being deployed now displays a message
indicating that the application is being deployed, instead of a generic
message.</p></li>
</ul>

## 21 Mar 2013 -- version 0.9.33

<p>Updated Node.ACS CLI to version 0.9.33 to fix an issue in the previous version
which prevented the CLI from running on Windows 7/8. If you are on Windows, upgrade 
to the latest version of the Node.ACS CLI:</p> 

<pre class='prettyprint'>npm install -g acs</pre>

<p>Depending on how the Node.ACS client is installed, you may need to invoke <b>npm</b>
with <b>sudo</b>.</p>

<pre class='prettyprint'>sudo npm install -g acs</pre>

## 14 Mar 2013

<ul>
<li>
<p>Added support for proxy servers in the <b>acs</b> command. If your computer is behind a proxy, 
   set the proxy server address in the <code>.acs</code> config file in your home directory:</p>
<pre class='prettyprint'>"proxy": "http://&lt;host&gt;:&lt;port&gt;"</pre>
</li>
<li>
<p>Added validation for the <code>package.json</code> file.</p>
</li>
<li>
<p>Added support for the Node global namespace object, <code>global</code>.</p>
</li>
<li>
<p>Removed a conflict for using the <code>formidible</code> <b>npm</b> package in MVC applications.
   The express framework uses <code>formidible</code> internally to implement <code>express.bodyParser</code>,
   so if <code>bodyParser</code> is in use, you cannot require <code>formidible</code> directly. This 
   fix removes <code>bodyParser</code> from the default configuration for users who wish to use <code>formidible</code>
   directly. To use <code>bodyParser</code>, you can import it explicitly in your <code>start</code> function:</p>
<pre class='prettyprint'>app.use(express.bodyParser({defer:true}));</pre>
</li>
<li>
<p>MVC applications now log an error message if the application attempts to start up a new HTTP server. Since a Node.ACS
   app can only have a single port open, it cannot open a new HTTP server in an MVC app, which includes a built-in HTTP server.</p>
</li>
