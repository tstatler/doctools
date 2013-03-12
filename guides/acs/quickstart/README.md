# Getting Started: QuickStart Guide

## Step 1. Register Your App with Appcelerator Cloud Services

Using the Appcelerator Cloud Services API to store and retrieve data for your
app is easy. First, create a cloud app on the [Apps
page](https://my.appcelerator.com/apps). If you would like to use Appcelerator
Cloud Services in your existing Titanium app, you can simply select 'Enable
Cloud Services'. Otherwise, select "Create a New Cloud App" to specify the app
name and description. A unique OAuth Consumer Key,OAuth Secret, and App Key
will be automatically generated and assigned to the app. After creating an
app, you can click on 'Manage Cloud App' to goto the Cloud App Management
page.

## Step 2. Titanium Integration

Titanium 2.0 and above provide full integration with Appcelerator Cloud
Services, please refer to [Titanium Appcelerator Cloud Services integration](h
ttp://docs.appcelerator.com/titanium/latest/#!/guide/Integrating_with_Appceler
ator_Cloud_Services) for more information.

## Step 3. Use Titanium, Appcelerator Cloud Services API or SDK in Your Own
App

Appcelerator Cloud Services provides methods for creating, managing, and
accessing different types of data in your app, such as
[Users](/docs/api/v1/users/info), [Places](/docs/api/v1/places/info), and
[Photos](/docs/api/v1/photos/info) over HTTP or HTTPS. Checkout the [Titanium]
(http://docs.appcelerator.com/titanium/2.0/index.html#!/guide/Integrating_with
_Appcelerator_Cloud_Services), [REST API](/docs/rest), [iOS SDK](/docs/ios),
[Javascript SDK](/docs/javascript), [Android SDK](/docs/android) and
[ActionScript 3 SDK](/docs/actionscript3) documentation to help you get
started.  
  
The [iOS SDK]( https://github.com/cocoafish/cocoafish-ios-sdk) comes with a
sample app. Open `samples/DemoApp/Demo.xcodeproj` in XCode, fill in your App
key DemoDelegate.m, then build and run the demo app. This gives you a basic
checkin app showing the place you added in the previous step.

## Step 4. Authentication

Your app must prove that it is allowed to talk to Appcelerator Cloud Services.
This keeps your data secure by preventing anyone from making requests to
Appcelerator Cloud Services that impersonate your app. the App Key must be
used in all API calls made from your app to Appcelerator Cloud Services. See
[Authentication](/docs/authentication) for more details about adding and using
authentication in your app.

## Step 5. Manage Your App

Data can be added to your app through Titanium, REST API, SDKs, or from the
Appcelerator Cloud Services App Management Web Console. As the administrator
of yours apps you can take a look at all of the people who have registered in
your app and what activities they have been doing through the Cloud App
Management Web Console.

