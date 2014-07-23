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

	NSURL *url = [NSURL URLWithString:@"http://localhost:8080/method"];
	NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:url];
	[request addValue:@"YOUR_APP_GUID" forHTTPHeaderField:@"x-native-id"];
	[[NSURLConnection alloc] initWithRequest:request delegate:self];

If you are using the CFNetwork framework, you can use the [`CFHTTPMessageSetHeaderFieldValue`](https://developer.apple.com/library/prerelease/mac/documentation/CoreFoundation/Reference/CFMessageRef/index.html#//apple_ref/c/func/CFHTTPMessageSetHeaderFieldValue) method of the [CFHTTPMessage](https://developer.apple.com/library/mac/documentation/CoreFoundation/Reference/CFMessageRef/Reference/reference.html) class. For an example, see the code listing in [Creating a CFHTTP Request](https://developer.apple.com/library/mac/documentation/Networking/Conceptual/CFNetwork/CFHTTPTasks/CFHTTPTasks.html#//apple_ref/doc/uid/TP30001132-CH5-SW1) in the CFNetwork Programming Guide.

## Adding a custom HTTP custom header on Android

If you are using [URLConnection](http://developer.android.com/reference/java/net/URLConnection.html), or any of its subclasses (`HttpUrlConnection`, `HttpsURLConnection`), you can use its [`addRequestProperty(String field, String new Value)`](http://developer.android.com/reference/java/net/URLConnection.html#addRequestProperty&28java.lang.String,%20java.lang.String%29) method to add the HTTP header. The following example demonstrates adding the `x-native-id` header using this method:

 	URL method_nameURL = new URL("https://yourappid.cloudapp-enterprise.appcelerator.com/method_name"); 	
   	URLConnection method_nameConnection = method_nameURL.openConnection();
	method_nameConnection.addRequestProperty("x-native-id", "<YOUR_APP_GUID>");

If your application uses the Apache Stack (org.apache.http namespace), the [addHeader(java.lang.String, java.lang.String)](http://developer.android.com/reference/org/apache/http/message/AbstractHttpMessage.html#addHeader%28java.lang.String,%20java.lang.String%29) is available to all classes that extend [AbstractHttpMessage](http://developer.android.com/reference/org/apache/http/message/AbstractHttpMessage.html). The following example demonstrates adding the `x-native-id` header using this method:

	DefaultHttpClient httpclient = new DefaultHttpClient();
	String url = "http://localhost:8080/method";
	HttpPost httpPost = new HttpPost(url);
	httpPost.addHeader("x-native-id" , "<YOUR_APP_GUID>");
	httpclient.execute(httpPost);

## Example project

To create a Node.ACS service to use in a native iOS or Android application, you use the ACS command-line
tool. If you don't have the `acs` CLI installed on your system, you can install it using the `npm` utility:

	sudo npm install -g acs






