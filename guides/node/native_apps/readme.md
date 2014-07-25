# Associating Node.ACS services with native applications

Appcelerator Dashboard can associate Node.ACS services used by a native iOS or Android application. 
This lets you see, for example, what Node.ACS services a given native application is using, or
which service methods are being used the most.

For this correlation to occur, the native application must include a custom HTTP header named **x-native-id** 
in each Node.ACS service method call it makes. The value of this header must be set to the GUID assigned 
to the application when you initially created it. The GUID for an existing native iOS or Android 
application can be found on the Overview tab in Dashboard, as shown below.

{@img guid.png}

The following sections provide common approaches to adding custom HTTP headers to your iOS and Android
network requests using well-known HTTP client libraries and frameworks.

## Adding a custom HTTP header on iOS

The [NSMutableURLRequest](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/nsmutableurlrequest_Class/Reference/Reference.html) class provides the following helper methods for setting HTTP headers:

* `addValue:(NSString \*)value forHTTPHeaderField:(NSString *)`
* `setValue:(NSString \*)value forHTTPHeaderField:(NSString *)`
* `setAllHTTPHeaderFields:(NSDictionary *)`

For example, the following uses the `addValue` method to add the `x-native-id` header to a request object:

	NSURL *url = [NSURL URLWithString:@"http://yourappid.cloudapp-enterprise.appcelerator.com/service_name"];
	NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:url];
	[request addValue:@"YOUR_APP_GUID" forHTTPHeaderField:@"x-native-id"];
	[[NSURLConnection alloc] initWithRequest:request delegate:self];

If you are using the CFNetwork framework, you can use the [`CFHTTPMessageSetHeaderFieldValue`](https://developer.apple.com/library/prerelease/mac/documentation/CoreFoundation/Reference/CFMessageRef/index.html#//apple_ref/c/func/CFHTTPMessageSetHeaderFieldValue) 
method of the [CFHTTPMessage](https://developer.apple.com/library/mac/documentation/CoreFoundation/Reference/CFMessageRef/Reference/reference.html) class. 
See the code listing in [Creating a CFHTTP Request](https://developer.apple.com/library/mac/documentation/Networking/Conceptual/CFNetwork/CFHTTPTasks/CFHTTPTasks.html#//apple_ref/doc/uid/TP30001132-CH5-SW1) in the CFNetwork Programming Guide for an example of this approach.

## Adding a custom HTTP custom header on Android

If you are using [URLConnection](http://developer.android.com/reference/java/net/URLConnection.html), 
or any of its subclasses (`HttpUrlConnection`, `HttpsURLConnection`), you can use its 
[`addRequestProperty(String field, String new Value)`](http://developer.android.com/reference/java/net/URLConnection.html#addRequestProperty&28java.lang.String,%20java.lang.String%29) method to add the HTTP header. The following example demonstrates adding 
the `x-native-id` header using this method:

 	URL url = new URL("https://yourappid.cloudapp-enterprise.appcelerator.com/method_name"); 	
   	URLConnection method_nameConnection = url.openConnection();
	method_nameConnection.addRequestProperty("x-native-id", "<YOUR_APP_GUID>");

If your application uses the Apache Stack (org.apache.http namespace), the [addHeader(java.lang.String, java.lang.String)](http://developer.android.com/reference/org/apache/http/message/AbstractHttpMessage.html#addHeader%28java.lang.String,%20java.lang.String%29) is available to all classes that extend [AbstractHttpMessage](http://developer.android.com/reference/org/apache/http/message/AbstractHttpMessage.html). The following example demonstrates adding the `x-native-id` header using this method:

	DefaultHttpClient httpclient = new DefaultHttpClient();
	String url = "https://yourappid.cloudapp-enterprise.appcelerator.com/method_name";
	HttpPost httpPost = new HttpPost(url);
	httpPost.addHeader("x-native-id" , "<YOUR_APP_GUID>");
	httpclient.execute(httpPost);

## Example

This section shows how to create a new Node.ACS service and associate it with a native iOS or Android
application. Before you continue:

* If you haven't yet, create a [native iOS or Android application](http://docs.appcelerator.com/platform/latest/#!/guide/Managing_Native_Applications_in_Dashboard) 
in Dashboard. 
* Make a note of the Application GUID (see above)

Node.ACS provides a [command-line tool](http://docs.appcelerator.com/cloud/latest/#!/guide/node_cli) 
called `acs` to create and manage your Node.ACS apps. If you don't have `acs` installed on your system,
run the following command:

	sudo npm install -g acs

Login to the ACS admin server and provide Appcelerator username and password at the prompts: 

	acs login --host admin.cloudapp-enterprise.appcelerator.com

To create a new Node.ACS application, you call the `acs new` sub-command followed by the application name. 
If you are a member of more than one Appcelerator Platform organization, you are prompted to select 
the desired organization in which to create the application. (If you belong to only one organization, you 
will not see this prompt.)

	$ acs new myproject
	ACS: Appcelerator Cloud Services Command-Line Interface, version 1.0.15
	Copyright (c) 2012-2014, Appcelerator, Inc.  All Rights Reserved.
	 
	Admin Hostname: https://admin.cloudapp-enterprise-preprod.appcelerator.com
	You belong to more than one organization. Please choose one to create the app for.
	  1) Appcelerator, Inc (12345)
	  2) My Personal Org (12302)
	  3) QA Org (11269)
	  : 

This creates a basic Node.ACS application with a single endpoint. To publish the application to ACS,
 `cd` to the newly created project and call `acs publish`:

	$ cd myproject
	$ acs publish

The output of the `publish` command includes the URL where the application will be available:

	Publishing to cloud...	
	...
	App helloworld version 0.1.0 published.
	App will be available at https://90b1c4ff046ba4cfe161fc9ff5e3b0b9e7719533.cloudapp-enterprise.appcelerator.com

You can also find this URL on the Overview tab in Dashboard for your native iOS or Android application
 (see above). 

Add the application URL to your network call. For example, on iOS:

    NSURL *serviceURL = [NSURL URLWithString:@"http://90a1c4bf046ba4cfe161fc9ff5e3b0b9e7719539.cloudapp-enterprise.appcelerator.com/"];
    NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:serviceURL];
    [request addValue:@"f4ff70fd-be9b-419d-8c5e-e9b8fece57fe" forHTTPHeaderField:@"x-native-id"];
    NSURLConnection *theConnection = [[NSURLConnection alloc] initWithRequest:request delegate:self];

Or, on Android:

	DefaultHttpClient httpclient = new DefaultHttpClient();
	String serviceURL = "http://90a1c4bf046ba4cfe161fc9ff5e3b0b9e7719539.cloudapp-enterprise.appcelerator.com/";
	HttpPost httpPost = new HttpPost(serviceURL);
	httpPost.addHeader("x-native-id" , "f4ff70fd-be9b-419d-8c5e-e9b8fece57fe");
	httpclient.execute(httpPost);

## Viewing Custom Services in Dashboard

Once your native application has made a Node.ACS service request, you can use Dashboard to view the association
between the application and the service. Specifically, you can see which custom services are being used
by a specific native application, as well as  

**To view the custom services being used by an application in Dashboard**: 

1. Select the application from the Dashboard apps menu.
2. Select Cloud > Custom Services to view a table of custom Node.ACS services used by the application:
	{@img services_used_by_app.png} 
3. Click a service name in the table to view its details, including:
 	* Service name, URL and status (running or stopped)
 	* Number of API calls made to the service for the selected time period
 	* Number of containers in which the service is running
 	* CPU load and memory usage
	* List of applications using the service 

	{@img connected_apps.png} 
4. Click the **Logs** tab to view details for individual HTTP service calls, including:
	* Service endpoint URL
	* Response time
	* IP address of calling client
	* Container ID
	* Date and time of call
	{@img service_logs.png}
