# crt -- Manages custom SSL certificates for Node.ACS applications

## Description

Manages custom SSL certificates for accessing your application via HTTPS.

**Only available for Enterprise users.**

### Creating a custom SSL PEM file
Your SSL certificate provider will provide you with three files:

* Certificate file (`customapp.com.crt`, for example)
* Intermediate certificate authority (`gd_bundle.crt`, for example)
* Key used to generate the certificate (`customapp.com.key`, for example)

You need to combine the contents of these three files into a single text file, called a PEM file, which you will then add to your application. The PEM file must have the following structure:

    -----BEGIN CERTIFICATE----- 
    <SSL certificate file contents>
    -----END CERTIFICATE-----  
    -----BEGIN CERTIFICATE----- 
    <Intermediate certificate file contents>
    -----END CERTIFICATE----- 
    -----BEGIN RSA PRIVATE KEY----- 
    <Private key file contents>
    -----END RSA PRIVATE KEY----

This can be done manually using a text editor, or from the command line using the `cat` command:

    cat customapp.com.crt gd_bundle.crt customapp.com.key >  customapp.com.pem

Once you've created the PEM file, you can add it to your application, as follows:

    $ acs crt --add customapp.com.pem 

**Login Required:** Yes

## Usage

<pre class="prettyprint">
acs crt [options] [<i>appname</i>]
</pre>


## Required Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><i>appname</i></td>
            <td>The name of the app to associate with the SSL certificate. If omitted, the command needs to be run from the application's root directory, or specify the application's directory with the <code>-d</code> option.</td>
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
            <td><code>--add <i>PEM-file</i></code></td>
            <td> Adds the SSL certificate contained by the specified PEM file.</td>
        </tr>
        <tr>
            <td><code>--remove</code></td>
            <td> Removes the SSL certificate of the associated application, if one exists.</td>
        </tr>
    </tbody>
</table>


## Examples
    
	$ acs crt --add customapp.com.pem
    $ acs crt --add customapp.com.pem MyApp
    $ acs crt --remove
    $ acs crt --remove -d ../apps/myapp
