# Titanium SDK and ACS

The Appcelerator Cloud Services APIs are supported in Titanium using the `ti.cloud`
module, an optional module which is packaged with the Titanium SDK.

When new APIs are added to ACS, they may not be immediately
available in the Titanium.Cloud module. See the [module API reference](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) 
for a list of supported objects and methods.

## Adding ACS to your Titanium Project

This section describes how to add ACS to a Titanium application. If you don't have an
existing ACS backend application, Studio can create one for you.

If you are using the CLI, you must create the ACS application using the ACS website and
integrate it as descibed in [Adding an Existing ACS Application to a Titanium Project](#existing_acs).

### Adding ACS to a New Titanium Application

If you are using Studio to create a new Titanium application, you can create a new ACS
application at the same time:

1. Click **File** > **New** > **Titanium Project** to start the new project wizard.
2. Choose a template and click **Next**.
3. On the next screen, make sure **Automatically cloud-enable this application** checked.
4. Enter the project name and ID and click **Finish**.

This creates a new Titanium application and a new ACS application, and configures the
Titanium project to access ACS.

### Adding ACS to an Existing Titanium Application

If you have an existing Titanium project in Studio, and want to create a new ACS backend
application for it:

1. Open the project's `tiapp.xml` and switch to the **Overview** tab.
2. Next to **Enable Cloud Services**, click the **Enable** button.

<a name="existing_acs"></a>

### Adding an Existing ACS Application to a Titanium Project

If you have already created an ACS application, you can add it to a Titanium project by
editing the `tiapp.xml` file. You'll need the API key, OAuth key, and OAuth secret
generated when you created the ACS application.

1.  Open the project's `tiapp.xml` and switch to the **tiapp.xml** (source view) tab.

2.  Add the following entries to the file:

        <property name="acs-api-key-development" type="string">YOUR DEVELOPMENT API KEY HERE</property>
        <property name="acs-oauth-key-development" type="string">YOUR DEVELOPMENT OAUTH KEY HERE</property>
        <property name="acs-oauth-secret-development" type="string">YOUR DEVELOPMENT OAUTH SECRET HERE</property>
        
        <property name="acs-api-key-production" type="string">YOUR PRODUCTION API KEY HERE</property>
        <property name="acs-oauth-key-production" type="string">YOUR PRODUCTION OAUTH KEY HERE</property>
        <property name="acs-oauth-secret-production" type="string">YOUR PRODUCTION OAUTH SECRET HERE</property>

3.  Find the `<modules>` element in the file, and add the following:

        <module platform="commonjs">ti.cloud</module>

    If there is no `<modules>` element, add the following inside the `<ti:app>`
    element:

        <modules>
            <module platform="commonjs">ti.cloud</module>
        </modules>

    (This element is usually placed just above the `<deployment-targets>` element.)

## Importing the Module

ACS support is baked into Titanium. However, you must include the cloud
services module into your project to use ACS functionality. In your app.js (or
other suitable file), include the `require()` statement as shown here:

    var Cloud = require('ti.cloud');
    Cloud.debug = true;  // optional; if you add this line, set it to false for production

## Authenticating your Application

Your app must prove that it is allowed to talk to ACS. This keeps your data
secure by preventing anyone from making requests to ACS that impersonate your
app. There are several methods for authenticating with ACS:

  * 3-Legged OAuth 

  * 2-Legged OAuth 

  * API key 

3-Legged OAuth, in which the username and password are not stored by the
application, is the preferred method in most cases. 

See the [Titanium.Cloud
Module Reference](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) for 
details on using each of the mechanisms in Titanium. 

For more information, see [Authentication](#!/guide/acs/authentication).

Each of the authentication methods requires a key or other data identifying
your ACS application.

## Using the ACS APIs

This is the magic, of course. This is where you add cloud services to your app
using our APIs. With over 25 APIs available for you to use, we obviously can't
cover them all here. But let's take a look at a couple of examples.

Create a user

    // example assumes you have a set of text fields named username, password, etc.
    Cloud.Users.create({
        username: username.value,
        password: password.value,
        password_confirmation: confirmPassword.value,
        first_name: firstName.value,
        last_name: lastName.value
    }, function (e) {
        if (e.success) {
    		// user created successfully
        } else {
            // oops, something went wrong
        }
    });

Create a user using 3-legged OAuth

    // ACS app must be configured to use 3-legged OAuth
    Cloud.Users.secureCreate({
        title: 'Sign Up Here'
    }, function (e) {
        if (e.success) {
            alert('Success:\\n' +
                'accessToken: ' + e.accessToken + '\\n' +
                'expiresIn: ' + e.expiresIn);
        } else {
            alert('Error:\\n' +
                ((e.error && e.message) || JSON.stringify(e)));
        }
    });

Post a photo

    
    
    // assumes you've obtained a photo from the camera or gallery, with blob data stored in an object named photo
    // collectionID is an ID generated by ACS for a grouping of photos, you could retrieve via code or hard-code it
    Cloud.Photos.create({
        photo: photo,
        collection_id: collectionID,
        'photo_sync_sizes[]': 'small_240'
    }, function (e) {
        if (e.success) {
    		// null out our photo objects to clean up memory
            photo = null;
            collectionID = null;
        } else {
            // oops, something went wrong
        }
    });

Linking a Facebook login with your app

    
    
    // Not shown is the code to implement the Facebook module in your app
    
    // call the ACS Facebook SocialIntegrations API to link logged in states
    function updateLoginStatus() {
        if (Ti.Facebook.loggedIn) {
            label.text = 'Logging in to ACS as well, please wait...';
            Cloud.SocialIntegrations.externalAccountLogin({
                type: 'facebook',
                token: Ti.Facebook.accessToken
            }, function (e) {
                if (e.success) {
                    var user = e.users[0];
                    alert('Logged in! You are now logged in as ' + user.id);
                }
                else {
                    error(e);
                }
            });
        }
        else {
            label.text = 'Please login to Facebook.';
        }
    }
    
    // when the user logs into or out of Facebook, link their login state with ACS
    Ti.Facebook.addEventListener('login', updateLoginStatus);
    Ti.Facebook.addEventListener('logout', updateLoginStatus);
    
    // add the Facebook login button
    win.add(Ti.Facebook.createLoginButton({
        top: 10
    }));

Of course, there are many more examples we could show. Instead, head on over
to the [ACS API documentation](#!/api) to view the samples included there plus the full
explanation of ACS APIs.

The Titanium.Cloud module also includes a sample application demonstrating
each of the ACS request types. You can find this in the modules folder under
the Titanium SDK folder. For example:

    /Library/Application Support/Titanium/modules/commonjs/ti.cloud/<version>/example

## References

  * [ACS API Reference](#!/api)

  * [Titanium.Cloud Module Reference](http://docs.appcelerator.com/titanium/latest/#!api/Titanium.Cloud)

  * [ACS Administration site](https://my.appcelerator.com/apps) (via your my.appcelerator.com page) 

