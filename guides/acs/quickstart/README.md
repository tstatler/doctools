# Getting Started: QuickStart Guide

## Step 1. Register Your App with Appcelerator Cloud Services

Using the Appcelerator Cloud Services API to store and retrieve data for your
app is easy. 

If you are using the community versions of Studio, you can add ACS 
to an existing Titanium app by opening the `tiapp.xml` file and enabling
cloud services. In Titanium Studio:

*   Click **Enable Cloud Services**.

In Appcelerator Studio:

*   In the **Appcelerator Services** section, click **Enable**.

Enabling cloud services in Studio creates a new Cloud application and adds its URL and
credentials to the Titanium project.

First, create a cloud app on the [My Apps page](https://my.appcelerator.com/apps). 
Click **Create a New Cloud App** and specify the app
name and description. A unique OAuth Consumer Key, OAuth Secret, and App Key
will be automatically generated and assigned to the app. 

## Step 2. Use the Appcelerator Cloud Services API in Your App

Appcelerator Cloud Services provides methods for creating, managing, and
accessing different types of data in your app, such as
{@link Users}, {@link Places}, and {@link Photos} over HTTP or HTTPS. 

You can integrate ACS into your application using the REST API, the Titanium SDK, 
or the ACS native iOS and Android SDKs.

Check out the [REST API](#!/guide/rest), 
[Titanium SDK](#!/guide/titanium), [iOS SDK](#!/guide/ios),
and [Android SDK](#!/guide/android) documentation to help you get
started.  
  
The [iOS SDK]( https://github.com/cocoafish/cocoafish-ios-sdk) comes with a
sample app. Open `samples/DemoApp/Demo.xcodeproj` in XCode, fill in your App
key DemoDelegate.m, then build and run the demo app. This gives you a basic
checkin app showing the place you added in the previous step.

## Step 3. Authentication

Your app must prove that it is allowed to talk to Appcelerator Cloud Services.
This keeps your data secure by preventing anyone from making requests to
Appcelerator Cloud Services that impersonate your app. The App Key must be
used in all API calls made from your app to Appcelerator Cloud Services. See
[Authentication](#!/guide/acs_authentication) for more details about adding and using
authentication in your app.

## Step 4. Manage Your App

You can use the web administration interface to add data to ACS, as well as manage users and objects.

Community users can manage their ACS applications using _my.appcelerator.com_:

1.  In a browser, open the My Apps page:

    [_my.appcelerator.com/apps_](https://my.appcelerator.com/apps)

2.  Locate your application and click **Manage ACS**.

Enterprise users can manage their ACS applications using _dashboard.appcelerator.com_:

1.  In a browser, open the Appcelerator Dashboard:

    [_dashboard.appcelerator.com_](https://dashboard.appcelerator.com)

2.  Choose an application from the application list and click the **Cloud** tab.

As an administrator, you can see all of the users who are registered for
your application, examine modify and delete ACS objects, and so on.

