# Getting Started: Using the iOS SDK


## Download the SDK

Grab the ACS iOS SDK from <https://github.com/cocoafish/cocoafish-ios-sdk>. See the 
[DemoApp](https://github.com/cocoafish/cocoafish-ios-sdk/tree/master/samples/DemoApp) and 
[APIs](https://github.com/cocoafish/cocoafish-ios-sdk/tree/master/samples/APIs) sample projects for 
examples of how to store and retrieve data with the SDK.

## Adding ACS to your XCode Project

1.  Create a ACS app from the [My Apps page](https://my.appcelerator.com/apps). Then in
    XCode, create an iOS project and add the following folders from `cocoafish-ios-sdk/src/` to your project:
    
        ACS
        ASIHTTPRequest
        FBConnect
    
    {@img ios1.png}  
  
    You can choose to use your own copy of `ASIHTTPRequest` (v1.8 or above) and
    `FBConnect` from facebook-ios-sdk (updated on or after Jan 31, 2011). The only
    change we made to the `ASIHTTPRequest` in our copy is in `ASIHttpRequest.m`:    
    
        - (void)readResponseHeaders
        {
          ...
          if ([self responseStatusCode] == 401) {
            // Commented out by ACS	
            // [self setAuthenticationNeeded:ASIHTTPAuthenticationNeeded];
          } else if ([self responseStatusCode] == 407) {
            [self setAuthenticationNeeded:ASIProxyAuthenticationNeeded];
          }
          ...
        }
        
    The ACS API server returns HTTP response code `401` in a number
    of different error situations. However, `ASIHttpRequest` interprets all `401`
    responses as Authentication Needed. This can be confusing if you want to
    show users the exact error that has occurred. For instance: Invalid user
    email/password, invalid oauth token. We commented out the above line to let
    the server error message to pass through.  
      
    If you are using your own version of `ASIHttpRequest`, you can choose to do the
    same to let server authentication error message pass through.  
  
2.  Add the following frameworks to your project:   
    
        libz.1.2.3.dylib
        SystemConfiguration.framework
        MobileCoreService.framework
        CoreLocation.framework
        CFNetwork.framework
        YAJL.framework
        AssetsLibrary.framework
        
    There are two copies of `YAJL.framework` under `cocoafish-ios-sdk/src/`:
    
        cocoafish-ios-sdk/src/YAJL.framework
        cocoafish-ios-sdk/src/ARMv7s-YAJL-framework
        
    We suggest that you add `ARMv7s-YAJL-framework` to your project, which is the newest 
    version of the YAJL framework, for ARMv7s. If you get any errors when using
    `ARMv7s-YAJL-framework`, please switch to the older version YAJL framework 
    (`cocoafish-ios-sdk/src/YAJL.framework`). The older version of the YAJL framework
    is also availabe from the following github repo:
    
    <https://github.com/gabriel/yajl-objc>
      
    {@img ios2.png}  
  
3.  Under Other Linker Flags in your target, add:
    
        -ObjC -all_load
    
    {@img ios3.png}  
  
4.  In your code, include the ACS header:
 
        #import "Cocoafish.h"
    
    {@img ios4.png}  

Now you're ready to go!

  
## Initialization & Authorization

If you choose to use oauth consumer key/secret to authenticate your app with
ACS, in your `AppDelegate.m`, define: 
    
    #define COCOAFISH_OAUTH_CONSUMER_KEY @"your consumer key here"
    #define COCOAFISH_OAUTH_CONSUMER_SECRET @"your consumer secret here"
    
and initialize ACS with the key/secret:
    
    [Cocoafish initializeWithOauthConsumerKey:oauthConsumerKey consumerSecret:oauthConsumerSecret customAppIds:nil];
    
Or, if you choose to use app key to authenticate your app, in your `AppDelegate.m`, define:

    #define COCOAFISH_APP_KEY @"your app key here"  

and initialize ACS with the app key:
    
    [Cocoafish initializeWithAppKey:COCOAFISH_APP_KEY customAppIds:nil];    

Once ACS is initialized, you can access it by calling:  
    
    [Cocoafish defaultCocoafish]
    
## Facebook Integration

1.  Create a new [Facebook App](https://developers.facebook.com/apps) if you
    don't have one yet.

2.  Obtain the Facebook App ID from Facebook.  
    You can get the Facebook App ID from Facebook, you will use it later in your
    project.

3.  Add the Facebook framework to your Xcode project.  
    The Cocoafish iOS SDK currently uses the Facebook SDK version 3.1, which only
    provides a framework. To use this framework, you must add it to your Xcode
    project:  

    1.  In Xcode with your project open, and your target selected go to the **Build Phases** 
        tab and expand the **Link Binary With Libraries** item.  

    2.  Click the **Add** button (+) located at the bottom of the 
        **Link Binary With Libraries** section.  

    3.  In the **Choose frameworks and libraries to add:** click **Add Other**.

    4.  Select the folder: `cocoafish-ios-sdk/src/FacebookSDK.framework`.

4.  Add additional iOS frameworks. Some additional frameworks must be linked in
    your Xcode project.  

    1.  In Xcode with your project open, and your target selected go to the **Build
        Phases** tab and expand the **Link Binary With Libraries** item.  

    2.  Click the **Add** button (+) located at the bottom of the **Link Binary With
        Libraries** section.  

    3.  Select `Accounts.framework`, `AdSupport.framework`, and `Social.framework` and
        click the **Add** button.

5.  Add the SQLite dynamic linked library to your Xcode project.

    1.  In Xcode with your project open, and your project selected go to the **Build
        Settings** tab and expand the **Linking** item  

    2.  Add the flag `-lsqlite3.0` to the **Other Linker Flags** item.

6.  Add two Facebook bundles to your project.

    Drag the following two files to your project navigator pane to add them to your project:  

        cocoafish-ios-sdk/src/FacebookSDK.framework/Resources/FacebookSDKResources.bundle  
        cocoafish-ios-sdk/src/FacebookSDK.framework/Resources/FBUserSettingsViewResources.bundle

7.  Add the Facebook SDK Header files to your project.
    
    Drag the following folder to your project navigator pane to add it to your project:  

        cocoafish-ios-sdk/src/FBConnect

8.  Add the Facebook ID to your app's `Info.plist` file under `URL types`.

    {@img facebook_ios_setting.png}

9.  Add the following code to your `AppDelegate.m` file:
    
        // pre 4.2
        - (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url
        {
        	return [[[Cocoafish defaultCocoafish] getFacebook] handleOpenURL:url];
        }
        
        // 4.2+
        - (BOOL)application:(UIApplication *)application openURL:(NSURL *)url
          sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
        	return [[[Cocoafish defaultCocoafish] getFacebook] handleOpenURL:url];
        }
    
## Push Notification

To enable Apple Push Notification service for your application, create an
Apple Push Notification certificate and upload the certificate to the ACS server.

Note that Apple push notifications do **not** work on simulators. 

For information about iOS push notifications, see
[iOS Developer Library: Local and Push Notification Programming Guide](http://developer.apple.com/library/ios/#documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Introduction.html).

### Create and Upload a Push Notification Certificate

To create an Apple Push Notification certificate, you need to first create an Explicit App ID.  The
App ID is used to identify where to send the push notification, which is tied to the certificate
when you create it.  After you create the certificate, export the certificate to PKCS #12 format and
upload it to the ACS server. This certificate allows the ACS server to communicate with the Apple
Push Notification server to send push notifications to iOS devices.

#### Register an App ID

  1. Log in to the [Apple Developer Member Center](https://developer.apple.com/membercenter/) as the Team Agent or Admin.
  2. Click the link under **Certificates, Identifiers & Profiles**.
  3. Click **Identifiers**, then click the plus sign (**+**) button near the top-right corner.
  4. Enter a description, which cannot include special characters (including most punctuation).
  5. Select the App ID Prefix to use.
  6. For the App ID Suffix, choose **Explicit App ID** and enter your Bundle ID. For Titanium
     applications, this is your Application ID from the `tiapp.xml` file.
  7. Under App Services, check the **Push Notifications** checkbox to enable push notifications for
     this App ID.
  8. Click **Continue**, **Submit**, then **Done**.

Note: You cannot use a **Wildcard App ID** for an application with push notifications.

#### Generate an Apple Push Notification Certificate

These directions cover how to generate an Apple Push Notification certificate for both testing
(Development) and production (Distribution).  Only step #4 differs based on which certificate you
create.

  1. Log in to the [Apple Developer Member Center](https://developer.apple.com/membercenter/) as the Team Agent or Admin.
  2. Click the link under **Certificates, Identifiers & Profiles**.
  3. Click **Certificates**, then click the plus sign (**+**) button near the top-right corner.
  4. For testing, select **Apple Push Notification service SSL (Sandbox)** and for production,
     select **Apple Push Notification service SSL (Production)**, then click **Continue**.
  5. Select the App ID that you created previously from the drop-down list, then click **Continue**.
  6. Follow the directions to create a Certificate Signing Request (CSR). Click **Continue**.
  7. Upload your CSR and click **Generate**.
  8. You will be returned to the Certificates page with the status listed as Pending. Wait a moment then
     refresh the page in your browser.
  9. Even though you are logged in as the Team Agent or Admin, you may need to approve your certificate.
     Click **Approve**.
 10. Download the certificate (.cer) file to your computer.
 11. Double-click the file to install it into your keychain.

#### Export the Certificate

  1. Open your Keychain.  Select **Applications** > **Utitlies** > **Keychain Access**.
  2. Under Categories on the left side, click **My Certificates**.
  3. Right-click the certificate you installed previously and select **Export**.
  4. In the **File Format** drop-down, select **Personal Information Exchange (.p12)**.
  5. Click **Save**.
  6. You are prompted to enter a password for the file. Enter a password, then click **Save**.

Keychain exports your certificate as a PKCS #12 file.

#### Configure the ACS Web Console

Upload your PKCS #12 (.p12) file to ACS to enable Apple Push Notification service.

  1. To open your application in the ACS web console:

     >  For Appcelerator Enterprise users, open
     >  [https://dashboard.appcelerator.com](https://dashboard.appcelerator.com), select an application
     >  from the **Apps** drop-down list, then click the **Cloud** tab.
     >
     >  For all other users, open
     >  [https://cloud.appcelerator.com/apps](https://cloud.appcelerator.com/apps), locate your application, then click
     >  the **Manage ACS** link.

  2. Select the correct environment to configure--either Development or Production.  Located in the
     top-right corner of the console, this is either a drop-down (enterprise version) or a set of two
     buttons (non-enterprise version).

  3. Click either **Configuration & Settings** (enterprise version) or **Settings** (non-enterprise version).

  4. Under the **Apple iOS Push Configuration** section, click **Choose File**, navigate to and select
     your PKCS #12 file, then click **Open**.

  5. Enter your certificate password in the password textbox. This is required despite the optional
     note or hint text.

  6. Save your changes.

ACS will verify that the certificate uploaded correctly and is valid.

{@img ios_push1.png}

{@img ios_push2.png}

### Create a Provisioning Profile

You need to create a provisioning profile to embed in your application.  This verifies the
integrity of the application based on the information within the profile,
such as the App ID and certificate you created previously.

These directions cover how to generate a provisioning profile for Development, Ad Hoc, In House and App Store distribution.
If you are distributing as a member of the iOS Developer Enterprise Program, you will have the
**In House** distribution option instead of the **App Store** option.
Only steps #4 and #7 differ based on which profile you create.

  1. Log in to the [Apple Developer Member Center](https://developer.apple.com/membercenter/) as the Team Agent or Admin.
  2. Click the link under **Certificates, Identifiers & Profiles**.
  3. Click **Provision Profiles**, then click the plus sign (**+**) button near the top-right corner.
  4. For testing, select **iOS App Development**, and for production, select either **App Store** to distribute to the
     App Store, **Ad Hoc** to distribute to a limited number of devices or **In House** for in house
     distribution to your company's employees, then click **Continue**.
  5. Select the App ID you created previously from the drop-down list, then click **Continue**.
  6. Select the certificate you created previously, then click **Continue**.
  7. For development and ad hoc distributions, select the devices you want to be able to run the app on, then click
     **Continue**.
  8. Enter a name for your provisioning profile. You should use a word like "dev", "distribution" or "ad hoc" in
     the name so that it is clear later what this profile is for. Click **Generate**.
  9. Click **Download** to save your provisioning profile file (.mobileprovision) to your computer, then
     click **Done**.
 10. Double-click the provisioning profile file to install it to Xcode.

### Update your code to register for push notifications

In yourAppDelegate.m, add the following code after initializing ACS
in method didFinishLaunchingWithOptions:

    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
    {
    	// Initialize Cocoafish with Facebook App Id if you set one
    	[Cocoafish initializeWithOauthConsumerKey:COCOAFISH_OAUTH_CONSUMER_KEY consumerSecret:COCOAFISH_OAUTH_CONSUMER_SECRET customAppIds:[NSDictionary dictionaryWithObject:facebookAppId forKey:@"Facebook"]];
    	
    	...
    
    	[[UIApplication sharedApplication] registerForRemoteNotificationTypes:(UIRemoteNotificationTypeSound | UIRemoteNotificationTypeAlert | UIRemoteNotificationTypeBadge)];
    	
    	// Code below is optional if you want to handle the notification after the app is launched by push notification
    	if (launchOptions != nil)
    	{
    		NSDictionary* dictionary = [launchOptions objectForKey:UIApplicationLaunchOptionsRemoteNotificationKey];
    		if (dictionary != nil)
    		{
    			NSLog(@"Launched from push notification: %@", dictionary);
    			...
    		}
    	}
    
        return YES;
    }
    
Also add the following code to `yourAppDelegate.m` to receive a device token to
pass to ACS:
    
    - (void)application:(UIApplication*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData*)deviceToken
    {    
    	NSString* newToken = [deviceToken description];
    	newToken = [newToken stringByTrimmingCharactersInSet:[NSCharacterSet characterSetWithCharactersInString:@"<>"]];
    	newToken = [newToken stringByReplacingOccurrencesOfString:@" " withString:@""];
        
    	NSLog(@"My token is: %@", newToken);
        
    	// Add to ACS
    	[[Cocoafish defaultCocoafish] setDeviceToken:newToken];
    }
    
Then refer to the {@link PushNotifications} API reference to
see how to subscribe and send push notifications. You can also log on to your
ACS App Console to send push notifications to all your
subscribed clients.

## ACS Model Classes

The SDK defines a list of object model classes that correspond to the server
objects under `ACS/Models`. They are all subclasses of `CCObject`
or `CCObjectWithPhoto`.

## Making API Calls

The ACS iOS SDK provides the `CCRequest` class with delegate
callbacks to make synchronous or asynchronous REST calls to the ACS
server easier. `CCRequest` is a subclass of the `ASIHttpRequest` class.
(For more information on `ASIHTTPRequest`, see the 
[`ASIHTTPRequest` web site](http://allseeing-i.com/ASIHTTPRequest/).)

To instantiate a `CCRequest` object:
    
    // Use HTTPS by default
    -(id)initWithDelegate:(id)requestDelegate httpMethod:(NSString *)httpMethod baseUrl:(NSString *)baseUrl paramDict:(NSDictionary *)paramDict;
    
    or 
    
    // Use HTTP. set protocol to @"http"
    -(id)initWithDelegate:(id)requestDelegate httpProtocol:(NSString *)protocol httpMethod:(NSString *)httpMethod baseUrl:(NSString *)baseUrl paramDict:(NSDictionary *)paramDict;

### `delegate`

If you want to perform an asynchronous call, pass in the delegate object that
implements the `CCRequestDelegate` methods `didSucceed` and `didFailWithError`:
    
    -(void)ccrequest:(CCRequest *)request didSucceed:(CCResponse *)response;
    
    -(void)ccrequest:(CCRequest *)request didFailWithError:(NSError *)error;
    
If you want to perform a synchronous REST call, you can pass in `nil` to the
`delegate` parameter.

### `baseUrl`

If the request url is:
    
    http://api.cloud.appcelerator.com/v1/users/create.json

Then the baseUrl is:
    
    @"users/create.json"

### `httpMethod`

The possible values are `@"GET"`, `@"POST"`, `@"PUT:` or `@"DELETE"`

### `paramDict`

It is a NSDictionary of parameters and values that will be passed to the
baseUrl.

### Example

Register a new user:

    NSMutableDictionary *paramDict = [NSMutableDictionary dictionaryWithCapacity:5];
    [paramDict setObject:@"email@email.com" forKey:@"email"];   
    [paramDict setObject:@"John" forKey:@"first_name"];   
    [paramDict setObject:@"Woo" forKey:@"last_name"];   
    [paramDict setObject:@"pass" forKey:@"password"];   
    [paramDict setObject:@"pass" forKey:@"password_confirmation"];
    CCRequest *request = [[CCRequest alloc] initWithDelegate:self httpMethod:@"POST" baseUrl:@"users/create.json" paramDict:paramDict];
    [request startAsynchronous]; // for asynchronous call and use ASIHttp's shared operation queue
    
To make an asynchronous request and use your own operation queue, replace the last line
with:

    [myOperationQueue addOperation:request]; // for asynchronous call and use my own operation queue
    
Or to make a synchronous call, replace the `startAsynchronous` call with the following
line:
    
    CCResponse *response = [request startSynchronousRequest]; // for synchronous call

## Asynchronous call

It is recommended to run all the REST calls asynchronously for better user
experience. If you want to be able to identify the request in the callback,
you can add custom `userInfo` to the `CCRequest` object for your own record.
    
    NSDictionary *userInfo = [NSDictionary dictionaryWithObjectsAndKeys:@"custom", @"type", nil];
    [request setUserInfo:userInfo];

## Handling Server Responses

The `CCResponse` object defined in `ACS/Network/CCResponse.h` contains the
response sent back from the ACS server. It has the following
objects:

*   `response.meta` contains the response metadata.
*   `response.response` is an `NSDictionary` representation of the raw JSON response.
    
For example, if the REST call is expected to return an array of {@link Users}, your
handler code might look like this:
    
    -(void)ccrequest:(CCRequest *)request didSucceed:(CCResponse *)response
    {
    	NSArray *results = [response getObjectsOfType:[CCUser class]];
    	for (CCUser *user in results) {
    		NSLog(@"user is %@", user)
    	}
    }
    
The `getObjectsOfType` method is used to extract a list of objects from the response.
Refer to `ACS/Models` for a list of supported class names.

## Photo Uploads

To upload a photo, after you have instantiated a `CCRequest` object, you can use
one of the following two methods:
    
    // For uploading directly from photo album using ALAssetLibrary
    [request addPhotoALAsset:(ALAsset *)alasset paramDict:(NSDictionary *)paramDict];
    
    or 
    
    // For uploading an UIImage
    [request addPhotoUIImage:(UIImage *)image paramDict:(NSDictionary *)paramDict];

If you have more than one photo to send, you can call any of the above
methods with a new image. Currently only photo update allows multiple photos
upload.

`paramDict` is optional, if you want the SDK to resize the original photo or
lower the image quality for faster uploads, you set the following key/values
in the paramDict:
    
    [params setObject:[NSNumber numberWithInt:800] forKey:@"max_size"]; // maximum pixels allowed
    [params setObject:[NSNumber numberWithDouble:0.5] forKey:@"jpeg_compression"]; // (0 < jpeg compression <= 1), 1 is the highest quality.

You can also choose to upload a photo synchronously. See [Photo Uploads and Resizing](#!/guide/photosizes)
for more information.

## Photo Downloads

`CCPhoto` class contains URLs of different sizes of a photo. By default,
photos are uploaded asynchronously and each photo comes with a boolean
`processed` attribute to indicate whether the background processing has
finished. If you want to access the actual photo, you need to download it from
the given URL and if the URL is not available, you have to try again until the
`processed` is NO.
    
    CCPhoto *photo;
    [photo getImage:(PhotoSize)photoSize];
    
It returns the `UIImage` of the photo requested if it has already been
downloaded, otherwise it returns `nil` and kicks off the download in the
background. If the photo size is not available (if you request an incorrect
size or the requested size hasn't been processed yet), no background download
will be kicked off. In order to get the notification when a download has
completed, you need to register to listen to the following notification in
your view:

    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleDownloaded:) name:@"DownloadFinished" object:[Cocoafish defaultCocoafish]];	

When the notification is delivered, the userInfo contains the requesting
CCPhoto object under key name `object`, and the size of the photo requested
under key name `size`. Then you can get the actual image by calling:
    
    CCPhoto *photo;
    [photo getImage:(NSString *)photoSize;
    
If you created a photo using default sizes, the photo sizes are:
    
      @"square_75",
      @"thumb_100",
      @"small_240",
      @"medium_500",
      @"medium_640",
      @"large_1024",
      @"original"
    
If you created a photo using custom sizes, the photo sizes are the name of your custom sizes. 
For details on custom sizes, see [Photo Uploads and Resizing](#!/guide/photosizes).

## Troubleshooting & Common Errors

If you hit the following runtime error:

    -[NSConcreteMutableData yajl_JSON]: unrecognized selector sent to instance 0x4d87400
    
Solution: Make sure you have included the YAJL framework. Click on your
project's target, select **Other Linker Flags** and add:
    
    -ObjC -all_load
    

In Xcode 4, make sure to add the above flags to all the fields under **Other
Linker Flags**:

{@img linkers_ios.png}  

## Enable and Disable Runtime Logging

To enable or disable runtime logging, set the `loggingEnabled` variable in
`Cocoafish.m`:
    
    -(void)initCommon:(NSDictionary *)customAppIds
    {
        //other code
    	
    	//true, enable log
    	//false, disable log
        self.loggingEnabled = true;
        
        // other code
    }
    
