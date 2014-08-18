# Getting Started: QuickStart Guide

Appcelerator Cloud Services provides a set of REST APIs for for creating, managing, and
accessing different types of data in your application, such as
{@link Users}, {@link Places}, and {@link Photos} over HTTP or HTTPS. You can integrate ACS into 
your application using the [Titanium](#!/guide/titanium), [iOS](#!/guide/ios) or [Android](#!/guide/android) SDKs, or by calling the
[REST APIs](#!/guide/rest) directly.

To manage your application and it's data&mdash;for example, to create or edit {@link Users} or manage 
{@link Photos}&mdash;you use [Appcelerator Dashboard](https://dashboard.appcelerator.com) 
([Platform](http://www.appcelerator.com/platform/appcelerator-platform/) users) 
or the [My Apps](https://my.appcelerator.com/apps) web console (community developers).

This guide explains the basic steps you need to take to enable and use ACS in your application in your Titanium application, or native iOS or Android application.

## Step 1: Enable Platform or Cloud Services

### Enabling Platform or Cloud Services in an Appcelerator or Titanium Studio

You use the [Titanium.Cloud](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) module, 
which is included with the Titanium SDK. To include the module in your application, and automatically create a corresponding Cloud application on ACS, you just need to enable Appcelerator Services in your Studio project's
tiapp.xml file. The specific steps depend on whether you are using Appcelerator Studio (available to Platform subscribers) or Titanium Studio.

**To enable Platform Services in Appcelerator Studio**:

* When creating a new project, in the new Mobile App Project dialog, select the organization the application belongs to, and click **Enable Appcelerator Platform Services**. {@img studio-enable-new.png}
* For an existing project, open the project's tiapp.xml file and click **Enable Services** 
in the Appcelerator Services section. {@img studio-enable-existing.png}

**To enable Cloud Services in Titanium Studio**:

* If you are creating a new project, click **Cloud-enable this Application** in the new Project dialog.
* For an existing project Titanium project, open your project's tiapp.xml file and click **Enable...** in the Cloud Services section to generate the required application keys. You will also need to manually add the application keys to your tiapp.xml file. See [Adding an Existing ACS application to a Titanium project](http://docs.appcelerator.com/cloud/latest/#!/guide/titanium-section-adding-an-existing-acs-application-to-a-titanium-project).

Enabling Platform/Cloud Services has the following affects:

* Creates a new ACS Cloud application that you can [manage](#manage) using Appcelerator Dashboard
or My Apps.
* Adds the `ti.cloud` module to your tiapp.xml; for Appcelerator Studio, modules are also added for the Test and Performance services.
* Adds application keys to tiapp.xml used to [authenticate](#!/guide/acs_authentication) your application when making ACS method calls.

Next, you can [import](#ticloud) the `ti.cloud` module and start making ACS method calls. 

### Enable Platform Services SDK for a native iOS or Android application

The Platform Services SDKs provide your native iOS and Android applications with easy access to ACS APIs
. These SDKs are only available to users with an [Appcelerator Platform](http://www.appcelerator.com/platform) subscription.

The following steps, covered in detail in the [Android SDK](#!/guide/android) and [iOS SDK](#!/guide/ios) guides, 
outline the process for enabling Platform Services in a native application:

1. In [Appcelerator Dashboard](https://dashboard.appcelerator.com), create a new Native Application for iOS or Android. {@img native.png} 
2. Download the Android or iOS SDK and obtain your application service key. You will paste this key 
	into the code of your iOS or Android project. {@img download.png}
3. Configure your existing [Android](http://docs.appcelerator.com/cloud/latest/#!/guide/android-section-enabling-cloud-services-in-a-new-project) or [iOS](http://docs.appcelerator.com/cloud/latest/#!/guide/ios-section-enabling-cloud-services-in-a-new-project)
to use the SDK.

For details on these steps, see the [Android SDK for ACS](#!/guide/android) and [iOS SDK for ACS](#!/guide/ios) guides.

## Step 2. Use the Appcelerator Cloud Services API in Your App 

### Calling Cloud Services from a Titanium Application <a name="ticloud"></a>

To use the ACS APIs in your Titanium application, you import the `ti.cloud` module and then being calling
its methods. Each method takes two parameters: a parameters object containing to pass to the method, 
and a function callback that's invoked when the method call completes, successfully or otherwise.

For example, the following code defines a simple Alloy application that defines a function named 
`createUser()` that calls the [Cloud.Users.create](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud.Users-method-create)
method.

	// app/controllers/index.js
	var Cloud = require("ti.cloud");

	function createUser(e) {
		Cloud.Users.create({
			username : "user1",
			password : "pass1",
			password_confirmation : "pass1"
		}, function(e) {
			if (e.success) {
				alert(e.users[0].username + " is logged in.");
			} else {
				alert("Error: " + e.message);
			}
		});
	}

For more examples, see the following:

* [Titanium SDK for ACS](#!/guide/titanium) guide.
* [Titanium.Cloud](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) module API reference.

### Calling Cloud Services from an iOS Application

Enabling Cloud Services in your iOS application, minimally, involves the following:

* Importing the `Appcelerator/Appcelerator.h` header file 
* Calling the [enableWithAppKey](http://docs.appcelerator.com/aps-sdk-apidoc/latest/ios/Classes/APSServiceManager.html#//api/name/enableWithAppKey:) method of the [APSServiceManager](http://docs.appcelerator.com/aps-sdk-apidoc/latest/ios/Classes/APSServiceManager.html) class,
passing it the service key generated by Dashboard. 

These steps are  typically done at start-up in the application delegate's `didFinishLaunchingWithOptions`
method:

	#import <Appcelerator/Appcelerator.h>

	@implementation AppDelegate
	- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
	{
	    NSString *appKey = @"<< YOUR APP KEY >>";
	    [[APSServiceManager sharedInstance] enableWithAppKey:appKey];
	}

You can then being using the object methods provided by the SDK, such as [\[APSUsers create:withBlock\]](http://docs.appcelerator.com/aps-sdk-apidoc/latest/ios/Classes/APSUsers.html#//api/name/create:withBlock:). For more code examples, see the following:

* [iOS SDK Guide](#!/guide/ios)
* [Appcelerator Platform Services API Reference for iOS](http://docs.appcelerator.com/aps-sdk-apidoc/latest/ios/) 

### Calling Cloud Services from an Android Application

Enabling Cloud Services in your Android application, minimally, involves the following:

* Importing the `com.appcelerator.aps.APSServiceManager` class. 
* Calling the [enable](http://docs.appcelerator.com/aps-sdk-apidoc/latest/android/com/appcelerator/aps/APSServiceManager.html#enable(android.content.Context%2C%20java.lang.String)) method of the [APSServiceManager](http://docs.appcelerator.com/aps-sdk-apidoc/latest/android/com/appcelerator/aps/APSServiceManager.html) class,
passing it the service key generated by Dashboard. 

These steps are typically done at start-up in the main activity:

	import com.appcelerator.aps.APSServiceManager;

	public class MainActivity extends Activity {
		try {
			APSServiceManager.getInstance().enable(getApplicationContext(), "<< YOUR APP KEY >>");
		} catch (RuntimeException e) {
			// Handle exception
		}
	}

You can then being using the object methods provided by the SDK, such as [APSUsers.create()](http://docs.appcelerator.com/aps-sdk-apidoc/latest/android/com/appcelerator/aps/APSUsers.html#create(java.util.Map%2C%20com.appcelerator.aps.APSResponseHandler)). For more code examples, see the following:

* [Android SDK Guide](#!/guide/android)
* [Appcelerator Platform Services API Reference for Android](http://docs.appcelerator.com/aps-sdk-apidoc/latest/android/) 

## Step 4. Manage Your Application <a name="manage"></a>

You use a web administration interface to manage your application's data, including users and other objects. Platform subscribers can refer to the [Managing ACS Data Objects](http://docs.appcelerator.com/platform/latest/#!/guide/Managing_ACS_data_objects) for details on managing specific ACS data types.

**Platform users**:

1. In a browser, open [Appcelerator Dashboard](https://dashboard.appcelerator.com).
2. Choose an application from the App menu.
3. From the right-side navigation, select **Cloud > Manage Data**.

To quickly access the Cloud management page from Appcelerator Studio, click the Details link in the Appcelerator Services section of your project's tiapp.xml file. {@img quicklinks.png}

**Community users**:

1.  In a browser, open [My Apps](https://my.appcelerator.com/apps).
2.  Locate your application and click **Manage ACS**.

<style>
	#toc: {
		max-width: 300px
	}
</style>
