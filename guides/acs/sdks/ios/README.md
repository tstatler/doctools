# Getting Started: Using the iOS SDK


## Download the SDK

Grab the ACS iOS SDK from <https://github.com/cocoafish
/cocoafish-ios-sdk>. See the [DemoApp](https://github.com/cocoafish/cocoafish-
ios-sdk/tree/master/samples/DemoApp) and [APIs](https://github.com/cocoafish
/cocoafish-ios-sdk/tree/master/samples/APIs) sample projects for examples of
how to store and retrieve data with the SDK.

## Adding ACS to your XCode Project

1\. Create a ACS app from the [Apps page](/apps/new).  Then in
XCode, create an iOS project and add the following folders from `cocoafish-ios-sdk/src/` to your project:
    
    ACS
    ASIHTTPRequest
    FBConnect
    
{@img ios1.png}  
  
You can choose to use your own copy of ASIHTTPRequest (v1.8 or above) and
FBConnect from facebook-ios-sdk (updated on or after Jan 31, 2011). The only
change we made to the ASIHTTPRequest in our copy is in `ASIHttpRequest.m`:    
    
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
of different error situations. However, ASIHttpRequest interprets all `401`
responses as "Authentication Needed." This can be confusing if you want to
show users the exact error that has occurred. For instance: Invalid user
email/password, invalid oauth token. We commented out the above line to let
the server error message to pass through.  
  
If you are using your own version of ASIHttpRequest, you can choose to do the
same to let server authentication error message pass through.  
  
2\. Add the following frameworks to your project:   
    
    libz.1.2.3.dylib
    SystemConfiguration.framework
    MobileCoreService.framework
    CoreLocation.framework
    CFNetwork.framework
    YAJL.framework
    AssetsLibrary.framework
    
There are two copies of YAJL.framework under `cocoafish-ios-sdk/src/`,one copy
is under cocoafish-ios-sdk/src/YAJL.framework, another is under cocoafish-ios-
sdk/src/ARMv7s-YAJL-framework. We suggest that you add cocoafish-ios-sdk/src
/ARMv7s-YAJL-framework to your project, which is the newest version YAJL
framework for ARMv7s. If you get any errors when using ARMv7s-YAJL-framework,
please switch to the older version YAJL framework which is located in
cocoafish-ios-sdk/src/YAJL.framework, or you can find it at
<https://github.com/gabriel/yajl-objc>.  
  
{@img ios2.png}  
  
3\. Under Other Linker Flags in your target, add:
    
    -ObjC -all_load
    
{@img ios3.png}  
  
4\. In your code, include the ACS header:
 
    #import "Cocoafish.h"
    
now you are ready to go!

{@img ios4.png}  
  
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

1\. Create a new [Facebook App](https://developers.facebook.com/apps) if you
don't have one yet.

2\. Obtain the Facebook App id from Facebook.  
You can get the Facebook App id from Facebook, you will use it later in your
project.

3\. Add the Facebook framework to your Xcode project.  
The Cocoafish iOS SDK currently uses the Facebook SDK version 3.1, which only
provides a framework. To use this framework, you must add it to your Xcode
project:  
a. In Xcode with your project open, and your target selected go to the "Build
Phases" tab and expand the "Link Binary With Libraries" item.  
b. Click the "+" button which located at the bottom of the "Link Binary With
Libraries" section.  
c. In the "Choose frameworks and libraries to add:" click the "Add Other..."
button.  
d. Select the folder: cocoafish-ios-sdk/src/FacebookSDK.framework

4\. Add additional iOS frameworks Some additional frameworks must be linked in
your Xcode project.  
a. In Xcode with your project open, and your target selected go to the "Build
Phases" tab and expand the "Link Binary With Libraries" item.  
b. Click the "+" button which located at the bottom of the "Link Binary With
Libraries" section.  
c. Select Accounts.framework, AdSupport.framework, and Social.framework and
click the "Add" button.

5\. Add SQLite dynamic linked library to your Xcode project  
a. In Xcode with your project open, and your project selected go to the "Build
Settings" tab and expand the "Linking" item  
b. Add the flag "-lsqlite3.0" to "Other Linker Flags" item.

6\. Add two Facebook bundles to your project  
Drag the two files to your project navigator pane to add them to your project:  
a. cocoafish-ios-
sdk/src/FacebookSDK.framework/Resources/FacebookSDKResources.bundle  
b. cocoafish-ios-
sdk/src/FacebookSDK.framework/Resources/FBUserSettingsViewResources.bundle

7\. Add the Facebook SDK Header files to your project  
Drag the folder to your project navigator pane to add it to your project:  
cocoafish-ios-sdk/src/FBConnect

8\. Add the facebook id to your app's plist under `URL types`.

{@img facebook_ios_setting.png}

9\. Add the following code to your AppDelegate.m
    
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

### Provisioning your Device for specialized Development

Apple push notification does not work on simulators. Please follow [Apple's in
structions](https://developer.apple.com/library/ios/#documentation/NetworkingI
nternet/Conceptual/RemoteNotificationsPG/CommunicatingWIthAPS/CommunicatingWIt
hAPS.html) to configure your device if you haven't done it.

### Create Push Notification Certificates for Development and Production

Logging into the [iOS Provisioning
Portal](https://developer.apple.com/ios/manage/overview/index.action). Go to
the "App IDs" section, create a new App or select an existing app, and click
"Configure". Make sure to log in to Apple's developer site as Team Agent to
access team provisioning profiles.  
  
{@img ios_push.png}  
  
Check the "Enable for Apple Push Notification service" checkbox. Next, click
"Configure" to walk through the Apple Certificate Assistant wizard. Finally,
click the download button to get the file.  
{@img ios_push2.png}  
  
Create a development certificate for development purpose. You will need to
create a production certificate before you release your app to the app store.
Double click on the downloaded app_developer_identity.cer to install it in
your login keychain. Once it's installed, you can see it in the "My
Certificates" category.  
  
{@img ios_push3.png}  
  
If your certificate doesn't show up in the "My Certificates" Category. Try to
drag the app_developer_identity.cer file to keychain under "Certificates"
Category. You will not be able to export the certificate until it shows up in
the "My Certificates" Category.  
Next, select "My Certificate" Category and select the newly installed push
certificate. Once selected, go to the "File" menu and select "Export Items..."
to save it as a .p12 file.  
  
{@img ios_push4.png}  
  
Now you can go to the "App Settings" in your ACS App console and
upload your .p12 file. Wait till the upload is finished and ACS
verifies that upload is successful and the certificate file is valid. You may
want to submit your certificate file password along with the certificate file
if have to, the password is only for verifying the certificate file, it won't
be persisted in ACS server.  
You can upload both your development and production certificate files but you
will only be able to choose to use one at a time. Make sure to switch to use
the production certificate before you submit your app to Apple for review. If
you want to test the push notification in production environment before you
submit your app, set the ACS app to use production certificate
and install ad-hoc release on your device.  
  
{@img ios_push5.png}  

### Update your provisional profile

You'll need to regenerate your provisioning profile if you just enabled push
notifications for your app. In [the iOS Provisioning
Portal](https://developer.apple.com/ios/manage/overview/index.action), head
over to "Provisioning" and find the profile you've been using. To ensure that
the profile gets regenerated, edit a field and set it back to its original
value if necessary. Once that's done, download the new profile and install it
in Xcode as usual.

### Update your code to register for push notifications

In yourAppDelegate.m, add the following code after initializing ACS
in method didFinishLaunchingWithOptions:

    
    
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
    {
    	// Initialize Cocoafish with facebook App Id if you set one
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
    

Also add the following code to yourAppDelegate.m to receive device token and
pass to ACS

    
    
    - (void)application:(UIApplication*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData*)deviceToken
    {    
    	NSString* newToken = [deviceToken description];
    	newToken = [newToken stringByTrimmingCharactersInSet:[NSCharacterSet characterSetWithCharactersInString:@"<>"]];
    	newToken = [newToken stringByReplacingOccurrencesOfString:@" " withString:@""];
        
    	NSLog(@"My token is: %@", newToken);
        
    	// Add to ACS
    	[[Cocoafish defaultCocoafish] setDeviceToken:newToken];
    }
    

Then refer to [Push Notification Docs](api/v1/push_notifications/subscribe) to
see how to subscribe and send push notifications. You can also log on to your
ACS App Console to send push notifications to all your
subscribed clients.

## ACS Model Classes

The sdk defines a list of object model classes that correspond to the server
objects under ACS/Models. They are all subclasses of `CCObject`
or `CCObjectWithPhoto`.

## Making API Calls

The ACS iOS SDK provides the `CCRequest` class with delegate
callbacks to make synchronized or asynchronized REST calls to the ACS
server easier. CCRequest is a subclass of
[ASIHttpRequest](https://allseeing-i.com/ASIHTTPRequest/).

To instantiate a CCRequest:

    
    
    // Use HTTPS by default
    -(id)initWithDelegate:(id)requestDelegate httpMethod:(NSString *)httpMethod baseUrl:(NSString *)baseUrl paramDict:(NSDictionary *)paramDict;
    
    or 
    
    // Use HTTP. set protocol to @"http"
    -(id)initWithDelegate:(id)requestDelegate httpProtocol:(NSString *)protocol httpMethod:(NSString *)httpMethod baseUrl:(NSString *)baseUrl paramDict:(NSDictionary *)paramDict;
    
    

### `delegate`

If you want to perform an asynchronous call, pass in the delegate object that
implements `CCRequestDelegate`methods, they are:

    
    
    -(void)ccrequest:(CCRequest *)request didSucceed:(CCResponse *)response;
    
    
    
    -(void)ccrequest:(CCRequest *)request didFailWithError:(NSError *)error;
    

If you want to perform a synchronous REST call, you can pass in nil to the
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
    [request startAsynchornous]; // for asynchronous call and use ASIHttp's shared operation queue
    
    or 
    [myOperationQueue addOperation:request]; // for asynchronous call and use my own operation queue
    
    or
    
    CCResponse *response = [request startSynchronousRequest]; // for synchronous call
    

## Asynchronous call

It is recommended to run all the REST calls asynchronously for better user
experience. If you want to be able to identify the request in the callback,
you can add custom userInfo to the CCRequest object for your own record.

    
    
    NSDictionary *userInfo = [NSDictionary dictionaryWithObjectsAndKeys:@"custom", @"type", nil];
    [request setUserInfo:userInfo];
    

## Handling Server Response

CCResponse defined in ACS/Network/CCResponse.h contains the
response sent back from the ACS server. It has the following
objects:

    
    
    response.meta contains all the meta related info. 
    response.response is a NSDictionary representation of the raw json response.
    

### Extract data from CCResponse

If the REST call is expected to return an array of Users, you can:

    
    
    -(void)ccrequest:(CCRequest *)request didSucceed:(CCResponse *)response
    {
    	NSArray *results = [response getObjectsOfType:[CCUser class]];
    	for (CCUser *user in results) {
    		NSLog(@"user is %@", user)
    	}
    }
    

`getObjectsOfType` is used to extract a list of objects from the response.
Refer to ACS/Models for a list of supported class names.

## Photo Uploads

To upload a photo, after you have instantiated a CCRequest object, you can use
one of the following two methods:

    
    
    // For uploading directly from photo album using ALAssetLibrary
    [request addPhotoALAsset:(ALAsset *)alasset paramDict:(NSDictionary *)paramDict];
    
    or 
    
    // For uploading an UIImage
    [request addPhotoUIImage:(UIImage *)image paramDict:(NSDictionary *)paramDict];
    

If you have more than one photos to send, you can call any of the above
methods with a new image. Currently only photo update allows multiple photos
upload.

`paramDict` is optional, if you want the SDK to resize the original photo or
lower the image quality for faster uploads, you set the following key/values
in the paramDict:

    
    
    [params setObject:[NSNumber numberWithInt:800] forKey:@"max_size"]; // maximum pixels allowed
    [params setObject:[NSNumber numberWithDouble:0.5] forKey:@"jpeg_compression"]; // (0 < jpeg compression <= 1), 1 is the highest quality.
    

You can also choose to [upload a photo synchronously](#!/guide/photosizes#sync)
and provide the synchronous parameters in the paramDict.

## Photo Downloads

`CCPhoto` class contains URLs of different sizes of a photo. By default,
photos are uploaded asynchronously and each photo comes with a boolean
`processed` attribute to indicate whether the background processing has
finished. If you want to access the actual photo, you need to download it from
the given URL and if the URL is not available, you have to try again until the
`processed` is NO.

    
    
    CCPhoto *photo;
    [photo getImage:(PhotoSize)photoSize];
    

It returns the UIImage of the photo requested if it has already been
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
    

If you created photo using default sizes, the photo sizes are:

    
    
      @"square_75",
      @"thumb_100",
      @"small_240",
      @"medium_500",
      @"medium_640",
      @"large_1024",
      @"original"
    

If you created photo using [custom sizes](#!/guide/photosizes#custom), the photo
sizes are the name of your custom sizes.

## Troubleshooting & Common Errors

If you hit the following runtime error:

    
    -[NSConcreteMutableData yajl_JSON]: unrecognized selector sent to instance 0x4d87400
    
Solution: Make sure you have included yajl framework and click on your
project's target, select Other Linker Flags and add:
    
    -ObjC -all_load
    

In xcode 4, make sure to add the above flags to all the fields under Other
Linker Flags:

{@img linkers_ios.png}  
  

## Enable and Disable runtime log

You can enable/disable runtime log by set loggingEnabled variable in
Cocoafish.m :
    
    -(void)initCommon:(NSDictionary *)customAppIds
    {
        //other code
    	
    	//true, enable log
    	//false, disable log
        self.loggingEnabled = true;
        
        // other code
    }
    

