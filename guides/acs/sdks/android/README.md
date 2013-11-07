<div id="doc_api">
<h1>Getting Started: Using the Android SDK</h1>

<h2>Download the SDK</h2>

Grab the ACS Android SDK from <a href="https://github.com/cocoafish/cocoafish-android-sdk" target="_blank">https://github.com/cocoafish/cocoafish-android-sdk</a>. See the <a href="https://github.com/cocoafish/cocoafish-android-sdk/tree/master/examples/Demo" target="_blank">demo application</a> for examples of how to store and retrieve data with the SDK.

<h2>Adding ACS to your Android Project</h2>

<p>Create an ACS app from the <a href="/apps" target="_blank">Apps page</a>.&nbsp;&nbsp;Then in eclipse(assuming you are using eclipse as developing IDE), create an Android project and add the <a href="https://github.com/cocoafish/cocoafish-android-sdk/blob/master/cocoafish/bin/cocoafish-1.0.jar" target="_blank">cocoafish-1.0.jar</a> from <code>cocoafish-android-sdk/cocoafish/bin/</code> to the lib folder of your project, then set it as a referenced in the build path.</p>
<p>The SDK also depends on HttpClient and OAuth libraries, so you need to also download the followling jars and set them all into the project build classpath:</p>
<a href="https://github.com/cocoafish/cocoafish-android-sdk/blob/master/examples/Demo/libs/apache-mime4j-0.6.jar" target="_blank">apache-mime4j-0.6.jar</a><br/>
<a href="https://github.com/cocoafish/cocoafish-android-sdk/blob/master/examples/Demo/libs/httpmime-4.0.1.jar" target="_blank">httpmime-4.0.1.jar</a><br/>
<a href="https://github.com/cocoafish/cocoafish-android-sdk/blob/master/examples/Demo/libs/signpost-core-1.2.1.1.jar" target="_blank">signpost-core-1.2.1.1.jar</a><br/>
<a href="https://github.com/cocoafish/cocoafish-android-sdk/blob/master/examples/Demo/libs/signpost-commonshttp4-1.2.1.1.jar" target="_blank">signpost-commonshttp4-1.2.1.1.jar</a><br/>

<h2>Initialization & Authorization</h2>

<p>The class <code>com.appcelerator.cloud.sdk.Cocoafish</code> is the main class to be used for making API calls, it needs to be imported in your code before using it:</p>

<pre class="prettyprint">
import com.appcelerator.cloud.sdk.Cocoafish;
</pre>

<p>If you choose to use oauth consumer key/secret to authenticate your app with ACS, initialize SDK instance with the key/secret:</p>

<pre class="prettyprint">
Cocoafish sdk = new Cocoafish("&lt;OAuth consumer key&gt;", "&lt;OAuth secret&gt;");
</pre>

<p>Or, if you choose to use app key to authenticate your app, initialize SDK instance with the app key:</p>

<pre class="prettyprint">
Cocoafish sdk = new Cocoafish("&lt;app key&gt;");
</pre>

<p>The ACS Android SDK also provides the capability of storing user session into the device's local storage, this will allow the application to auto-restore last time session when it is closed and then restarted.</p>

<p>To enable this feature, an instance of the <code>android.content.Context</code> should be provided when creating the <code>Cocoafish</code> instance:</p>

<pre class="prettyprint">
Cocoafish sdk = new Cocoafish("&lt;OAuth consumer key&gt;", "&lt;OAuth secret&gt;", "&lt;app. context&gt;");
</pre>

<p>or</p>

<pre class="prettyprint">
Cocoafish sdk = new Cocoafish("&lt;app key&gt;", "&lt;app. context&gt;");
</pre>

<p>To get the application context, you could use the method <code>getApplicationContext()</code> in the <code>Application</code> class.</p>

<h2>Session Management</h2>

<p>Just as the above section described, the SDK provides the capability to store your application's session status into device's local storage.</p>

<p>And also, the SDK holds an instance of <code>com.appcelerator.cloud.sdk.CCUser</code> which contains currently logged in user's information. Here is the <code>CCUser</code> class definition:</p>

<pre class="prettyprint">
public class CCResponse {
  public String getObjectId();  //id
  public Date getCreatedDate(); //created date
  public Date getUpdatedDate(); //updated date
  public String getFirst();     //first name
  public String getLast();      //last name
  public String getEmail();     //email
  public String getUserName();  //user name
}
</pre>

<p>You could get this instance by calling <code>getCurrentUser()</code> method of the class <code>Cocoafish</code>, if there is no logged in session or "logout" is called, the return value will be <code>null</code>.</p>

<h2>Making API Calls</h2>

The ACS Android SDK provides the <code>sendRequest</code> method to make synchronized REST calls to the ACS server easier.

<p>The method's signature:</p>

<pre class="prettyprint">
public CCResponse sendRequest(String url, CCRequestMethod method, Map&lt;String, Object&gt; data, boolean useSecure) throws CocoafishError
</pre>

<h3><code>url</code></h3>
If the request API url is:

<pre class="prettyprint">
http://api.cloud.appcelerator.com/v1/users/create.json
</pre>

Then the "url" here is:

<pre class="prettyprint">
users/create.json
</pre>

<h3><code>method</code></h3>

<p>The possible values are <code>CCRequestMethod.GET</code>, <code>CCRequestMethod.POST</code>, <code>CCRequestMethod.PUT</code> or <code>CCRequestMethod.DELETE</code></p>

<p>This parameter is restricted to accept only one of the following four objects from class <code>com.appcelerator.cloud.sdk.CCRequestMethod</code> as its value:</p>

<pre class="prettyprint">
CCRequestMethod.GET
CCRequestMethod.POST
CCRequestMethod.PUT
CCRequestMethod.DELETE
</pre>

<h3><code>data</code></h3>

An instance of <code>Map&lt;String, Object&gt;</code> which contains parameters to pass. The key is the name of the passing parameter, and the value is the value of the passing parameter.
For example:

For the user login API:
<pre class="prettyprint">
Map&lt;String, Object&gt; data = new HashMap&lt;String, Object&gt;();
data.put("login", "test@appcelerator.com");
data.put("password", "test");
</pre>

<h3><code>useSecure</code></h3>

<p>Indicates whether to use SSL. </p>
<code>true</code> for using SSL, <code>false</code> for not using SSL.

<h2>Handling Server Response</h2>

<p>The server response will be contained in an instance of <code>com.appcelerator.cloud.sdk.CCResponse</code> which will be returned by <code>sendRequest</code> method.</p>
<p>Here is the CCResponse's class definition:</p>

<pre class="prettyprint">
public class CCResponse {
  public CCMeta getMeta();
  public JSONObject getResponseData();
}
</pre>

<p>The <code>getMeta</code> method returns an instance of class <code>com.appcelerator.cloud.sdk.CCMeta</code> which contains all meta data returned by server. Here is the CCMeta's class definition:</p>
<pre class="prettyprint">
public class CCMeta {
  public String getStatus();
  public int getCode();
  public String getMessage();
  public String getMethod();
}
</pre>

<p>The <code>getResponseData</code> method returns an instance of class <code>org.json.JSONObject</code> which contains all of the response data returned by server.</p>
<p>The ACS Android SDK is using standard <code>JSONObject</code> to wrap the returned json data, for more information of how to use <code>JSONObject</code>, please refer to <a href="https://www.json.org/javadoc/org/json/JSONObject.html" target="_blank">JSONObject API doc</a>.</p>

<h3>Example of accessing response object</h3>

If the API call is expected to return an array of Users, you can:
<pre class="prettyprint">
CCResponse response = sdk.sendRequest("users/search.json", CCRequestMethod.GET, null, false);
JSONObject responseJSON = response.getResponseData();
JSONArray users = responseJSON.getJSONArray("users");
for (int i=0;i&lt;users.length();i++) {
  JSONObject user = usersArr.getJSONObject(i);
  System.out.println("User: " + user);
}
</pre>

<h2>Push Notifications</h2>

<p>
ACS supports two protocols to send push notifications to Android devices:</p>

<ul>
<li><a href="http://developer.android.com/google/gcm/index.html">Google Cloud Messaging</a> (GCM)</li>
<li><a href="http://www.ibm.com/developerworks/webservices/library/ws-mqtt/index.html">Message Queuing Telemetry Transport</a> (MQTT)</li>
</ul>

<p class="note">As of August 2013, MQTT has been 
  <a href="http://www.appcelerator.com/blog/2013/08/android-push-notification-deprecating-mqtt-in-favor-of-gcm/">deprecated</a> 
  in favor of GCM and is no longer available for Enterprise use. MQTT will continue to be available to Community users.</p>

<h3>Obtaining a Google API key and GCM sender ID</h3>

<p>
To use GCM in your Android application, you need to create a Google API project, enable its GCM service, 
and obtain the API project's Google API key and GCM sender ID. For steps on obtaining these items 
see <a href="http://developer.android.com/google/gcm/gs.html" target="_">Getting Started with GCM</a>. 
Follow the steps found there for <i>Creating a Google API Project</i>, <i>Enabling the GCM Service</i> 
and <i>Obtaining an API Key</i>. When you create a new server key, per those instructions, you will be 
asked to provide a list of IP addresses the server will accept requests from. Leave this list empty to 
accept requests from all IP addresses.
</p>

<h3>Configuring your app for push notifications</h3>

<p>To configure your application for push notifications you use the Dashboard (Enterprise applications) or My App (Community applications).</p>

<p><b>To configure your app for push notifications (Enterprise developers): </b></p>
<ol>
  <li>Open <a href="https://dashboard.appcelerator.com">Dashboard.</a> 
  <li>Select your application from the drop-down list.</a> 
  <li>Select the <b>Cloud</b> tab.</a> 
  <li>Click <b>Settings & Configuration</b> from the left-side navigation.</li>
  <li>Select the <b>Android Push</b> tab.</li>
  <li>Enter your Google API key in the <b>GCM API Key</b> field and GCM sender ID in the <b>GCM Sender ID</b> field.
    {@img android_push_dashboard.png}
  </li>
  <li>Click <b>Save Changes</b>.</li>
  </ul>
</li>
</ol>

<p><b>To configure your app for push notifications (Community developers): </b></p>

<ol>
  <li>Open <a href="https://cloud.appcelerator.com/apps">My Apps</a>.</li>
  <li>Find your application in the list of apps and click the <b>Manage ACS</b> link.</li>
  <li>In the <b>Android Push Configuration</b> section, configure either GCM or MQTT:
      <ul>
        <li>For GCM, enter your Google API key in the <b>Google Cloud Messaging (GCM) API Key</b> field and your GCM sender ID in the <b>Google Cloud Messaging (GCM) Sender ID</b> field.</li>
        <li>For MQTT, enter your Android application's package name in the <b>Application Package (MQTT)</b> field.
      </li>
      </ul>
    </li>
      {@img android_push.png}
      <li>Click <b>Save Android Push Configuration Changes</b>.</li>
  </li>
</ol>

	
<h3>Setup Android Project</h3>

<p>In project's AndroidManifest.xml:</p>

<p>1. Add following to the <code>&lt;application&gt;</code> section:</p>
<pre class="prettyprint">
&lt;service android:name="com.appcelerator.cloud.push.PushService" /&gt;
</pre>

<p>2. Add following to the <code>&lt;manifest&gt;</code> section:</p>
<pre class="prettyprint">
&lt;uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" /&gt;
&lt;uses-permission android:name="android.permission.READ_PHONE_STATE" /&gt;
&lt;uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /&gt;
&lt;uses-permission android:name="android.permission.INTERNET" /&gt;
&lt;uses-permission android:name="android.permission.VIBRATE" /&gt;
&lt;uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /&gt;
</pre>

<h3>Device Token</h3>

<p>The device token is a unique identifier for an Android device, with having it, the push notification server can locate and push the desired notifications to the right device.</p>
<p>Device token is generated by Appcelecator Cloud Services push notification server, it is necessary to request a device token in your app to enable the push notification on Android device. To acquire a device token, you can simply call one of following methods from class <code>com.appcelerator.cloud.push.CCPushService</code>:</p>

<pre class="prettyprint">
public static String getDeviceToken(final Context androidContext, final String appKey);
public static void getDeviceTokenAsnyc(final Context androidContext, final String appKey, final DeviceTokenCallback callback);
</pre>

<span style="font-weight: bold">androidContext</span> - The instance of <code>android.context.Context</code> from your app <br/>
<span style="font-weight: bold">appKey</span> - The app's key of your Appcelerator Cloud Services app <br/>
<span style="font-weight: bold">callback</span> - An instance of <code>com.appcelerator.cloud.push.DeviceTokenCallback</code> for which whenever a device token is available, its <code>receivedDeviceToken</code> will be called <br/>


<p>The difference between these two methods is the <code>getDeviceToken</code> sends request and get device token synchronously, where the <code>getDeviceTokenAsnyc</code> does it asynchronously.</p>

<p>Once you get the device token, you may proceed to subscribe the device by using the {@link PushNotifications#subscribe} API. This starts the push notification service and gets the Android device ready to receive push notifications.</p>

<p>Note: once device token is successfully acquired, it will be stored on the device's local storage, and next time when getting device token, it will return from reading local storage instead of communicating with server. So it is safe to request device token multiple times if necessary.</p>

<h3>Push Notification Service</h3>

<p>The push notification service is a standard android service that keeps a persistent connection to the push notification server. Once the service is started, the device is ready to receive push notifications. The service will be running as a background process continuously even your app is not actively running.</p>

<p>The class <code>com.appcelerator.cloud.push.CCPushService</code> is the utility for controlling push notification service to start and stop.</p>

<p>To start or stop the push notification service, just simply do as following:</p>

<pre class="prettyprint">
CCPushService.getInstance().startService(context);
CCPushService.getInstance().stopService(context);
</pre>

<p>The <code>context</code> is the instance of <code>android.content.Context</code> which belongs to your android app.</p>

<p>Please be noted that you need to get device token before starting the push notification service on your device, otherwise, there will be an exception thrown when trying to start push notification service without having a valid device token.</p>

<h3>Receive Push Notifications</h3>

<p>Once you got the device token and started push notification service, your device is ready for receiving push notifications. When a push notification arrives, there will be an app wide broadcast with payload being sent out.

<p>In order to receive the push notification for further processing, you need to implement an android receiver to receive the payload. The payload is a string and is passed to your receiver as an extra data field in the <code>Intent</code>. Here is an example of receiver:</p>

<pre class="prettyprint">
import com.appcelerator.cloud.push.PushService;

public class CustomReceiver extends BroadcastReceiver {
  @Override
  public void onReceive(Context context, Intent intent) {
    if(intent == null || context == null)
      return;	
    if (intent.getAction().equals(PushService.ACTION_MSG_ARRIVAL)) {
      String payloadString = intent.getStringExtra("payload");
      // Covert payload from String to JSONObject
      JSONObject payload = null;
      try {
        payload = new JSONObject(payloadString);
      } catch (JSONException ex) {
        //error
      }
      ...
    }
  }
}
</pre>

<p>Then you need to register this receiver into AndroidManifest.xml to <code>&lt;application&gt;</code> section:</p>

<pre class="prettyprint">
&lt;receiver android:name="com.your.app.CustomReceiver" &gt;
  &lt;intent-filter&gt;
    &lt;action android:name="com.appcelerator.cloud.push.PushService.MSG_ARRIVAL" /&gt;
    &lt;category android:name="android.intent.category.HOME" /&gt;
  &lt;/intent-filter&gt;
&lt;/receiver&gt;
</pre>

<p>Other than creating your own receiver, there is already a fully-featured receiver being shipped with Appcelerator Cloud Services android sdk. You can always use this receiver for handling received notification instead of building one from scratch.</p>

<p>This receiver can do the following things for you when a push notification arrives at device:</p>

<ul>
	<li>Show custom alert</li>
	<li>Display custom title</li>
	<li>Display custom icon</li>
	<li>Display custom badge</li>
	<li>Play a custom sound</li>
	<li>Vibrate device</li>
</ul>

<p>All of these features can be done easily by just using default notification receiver and setting specific fields in the payload json, here are the details of how it works:</p>

<p>1. Register the default notification receiver into your app, in AndroidManifest.xml file, <code>&lt;application&gt;</code> section:</p>

<pre class="prettyprint">
&lt;receiver android:name="com.appcelerator.cloud.push.PushBroadcastReceiver" &gt;
  &lt;intent-filter&gt;
    &lt;action android:name="android.intent.action.BOOT_COMPLETED" /&gt;
    &lt;action android:name="android.intent.action.USER_PRESENT" /&gt;
    &lt;action android:name="com.appcelerator.cloud.push.PushService.MSG_ARRIVAL" /&gt;
    &lt;category android:name="android.intent.category.HOME" /&gt;
  &lt;/intent-filter&gt;
  &lt;meta-data 
    android:name="com.appcelerator.cloud.push.BroadcastReceiver.ArrivalActivity"
    android:value="com.cocoafish.pushnotifications.ArrivalActivity" /&gt;
&lt;/receiver&gt;
</pre>

<p>
You may have noticed there is a <code>&lt;meta-data&gt;</code> section in the receiver, it is for registering a custom <code>Activity</code>. Whenever a push notification arrives at device and have been processed by the default receiver, the sdk needs an <code>Activity</code> from your app to hand over the processing flow control, so in this case, you need to register your activity class in here for letting the receiver know which activity it should turn to.
Please make sure the name of <code>&lt;meta-data&gt;</code> should be "<span style="font-weight:bold">com.appcelerator.cloud.push.BroadcastReceiver.ArrivalActivity</span>", otherwise, the receiver won't be able to find your activity and hand over control. 
</p>

<p>The complete payload will still be passed to your activity, so that you still can do further processing on the payload, such as updating your app data, etc. The following is an example of the activity in your app, you can get the idea of how get push notification's payload:</p>

<pre class="prettyprint">
public class ArrivalActivity extends Activity {
  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.arrival);
    Intent intent = getIntent();
    String payload = intent.getExtras().getString("payload");
    ...
  }
}
</pre>

<p>2. Send push notification with json payload which contains reserved keywords for certern displaying behavior on the device. The reserved keywords are defined as following:</p>

<table class="doc-table">
	<tr>
		<th>Key</th>
		<th nowrap>Value type</th>
		<th>Comments</th>
	</tr>
	<tr>
		<td><code>alert</code></td>
		<td>String</td>
		<td>Content of the notification item to be displayed in notification center.</td>
	</tr>
	<tr>
      <td><code>title</code></td>
      <td>String</td>
      <td>Title of the notification item to be displayed in notification center.</td>
    </tr>
	<tr>
		<td><code>icon</code></td>
		<td>String</td>
		<td>The icon's file name without extension. The file should be located under app's "<code>res/drawable</code>" directory.<br/>This icon will be used to show in notification bar and be used as icon of notification item in the notification center. If no icon is provided or the provided one is unreachable, the app's icon will be used by default.</td>
	</tr>
	<tr>
		<td><code>badge</code></td>
		<td>Number</td>
		<td>The number to display as the badge of the application icon.</td>
	</tr>
	<tr>
		<td><code>sound</code></td>
		<td>String</td>
		<td>The sound's file name. The file should be located under app's "<code>assets/sound</code>" directory.<br/>If the sound file is not reachable, no sound will be played.</td>
	</tr>
	<tr>
		<td><code>vibrate</code></td>
		<td>Boolean</td>
		<td>If the value is true, then the device will vibrate for 1 second.</td>
	</tr>
</table>

<p>Here is an example of the payload json including all of the reserved keywords as well as custom contents:</p>

<pre class="prettyprint">
{
  "title": "Example",
  "alert": "Sample alert",
  "icon": "little_star",
  "badge": 3,
  "sound": "door_bell.wav",
  "vibrate": true,
  "score": 51,
  "custom_field": {
    "headlines": "Appcelerator Cloud Services Rocks!"
  }
}
</pre>

<p>Note: For iOS device, only <code>alert</code>, <code>sound</code> and <code>badge</code> can be recoginzed. The <code>icon</code>, <code>vibrate</code> and <code>title</code> can only work on Android device, but you can still receive them in your iOS app, you can use them like other custom fields.</p>

<p>Another important thing is that it is recommanded to just use one push notification receiver at a time, try to register multiple receivers at the same time may cause conflicts on processing received notifications.</p>

<h3>Leveraging ACS Push Notification Receiver</h3>

<p>Just as described above, the default receiver that comes with SDK provides lots of great features that are ready for use, but sometimes it is still not enough for meeting your app's requirement. So what should we do if we want to use the features provided by default receiver plus our own implementations? <br/>The answer is quite easy, just create your own receiver with extending the default receiver, then in the <code>onReceive</code> method, get the payload and call <code>showNotification</code> method to handle the message/icon displaying or sound playing.</p>

<p>There are two <code>showNotification</code> methods available for you to use:</p>

<pre class="prettyprint">
protected void showNotification(Context context, JSONObject payload);
protected void showNotification(Context context, JSONObject payload, int notificationId);
</pre>

<p>
The <code>context</code> is the instance of <code>android.content.Context</code> which belongs to your android app;<br/>
The <code>payload</code> is an instance of <code>JSONObject</code> which is the payload in json format;<br/>
The <code>notificationId</code> a desired integer which will be the identifier of the android notification shows in notification center; by setting it or not, means you can control whether or not to merge multiple notifications into one item or multiple items in the android notification center.
</p>

<p>Again, once you registered your own receiver in your app, please make sure to remove the default receiver from AndroidManifest.xml file.</p>

<h2>Photo Uploads</h2>

<p>To upload photo with Android SDK is easy, all you have to do is to create an instance of <code>java.io.File</code>, then pass the instance as an item of the <code>data</code> to the <code>sendRequest</code> to upload the photo.

<p>Note: the File instance has to be initialized with an existing file.</p>

Here is an example of uploading a local image file to ACS server through Android SDK:

<p>
1. Create a File instance:
<pre class="prettyprint">
File file = new File("/photos/profile.gif");
</pre>
</p>

<p>
2. Upload the image file by calling <code>sendRequest</code>:
<pre class="prettyprint">
Cocoafish sdk = new Cocoafish('vw1G7wq6KTKd52m76XwjvoiIhxeHxeXG');
Map&lt;String, Object&gt; data = new HashMap&lt;String, Object&gt;();
data.put("photo", file);
sdk.sendRequest("photos/create.json", CCRequestMethod.POST, data, false);
</pre>
</p>

Note:It is the client code's responsibility to make sure the instance of <code>File</code> is initialized with an existing local image file before passing to SDK, otherwise, the upload won't be succeed.

<h2>Example</h2>

<p>Here is an example of creating user by using the ACS Android SDK. 
This example will create a user with a profile photo(Note the "photo" item of passed in data parameter).</p>

<p>
1. Prepare the parameters for creating the new user
<pre class="prettyprint">
//the user's parameters
Map&lt;String, Object&gt; data = new HashMap&lt;String, Object&gt;()
data.put("email", "test@appcelerator.com");
data.put("first_name", "test_firstname");
data.put("last_name", "test_lastname");
data.put("password", "test_password");
data.put("password_confirmation", "test_password");

File file = new File("/photos/profile.gif");  //The instance of File with local image file loaded
data.put("photo", file);
</pre>
</p>

<p>
2. Create SDK instance and send API request
<pre class="prettyprint">
Cocoafish sdk = new Cocoafish('vw1G7wq6KTKd52m76XwjvoiIhxeHxeXG');
CCResponse response = sdk.sendRequest("users/create.json", URLRequestMethod.POST, data, false);
</pre>
</p>

<p>
3. Accessing server response
<pre class="prettyprint">
JSONObject responseJSON = response.getResponseData();  //CCResponse response
CCMeta meta = response.getMeta();
if("ok".equals(meta.getStatus()) 
    && meta.getCode() == 200 
    && "createUser".equals(meta.getMethod())) {
  JSONArray users = responseJSON.getJSONArray("users");
  JSONObject user = users.getJSONObject(0);
  
  StringBuffer sb = new StringBuffer();
  sb.append("Create user successful!\n");
  sb.append("id:" + user.getString("id") + "\n");
  sb.append("first name:" + user.getString("first_name") + "\n");
  sb.append("last name:" + user.getString("last_name") + "\n");
  sb.append("email:" + user.getString("email") + "\n");
  System.out.println(sb.toString());
}
</pre>
</p>

<h2>Sample Android Application</h2>
<p>Here are the instructions of how to run the sample app. on your own host:</p>

<p>The `examples/Demo` folder contains a <a href="https://github.com/cocoafish/cocoafish-android-sdk/tree/master/examples/Demo" target="_blank">sample Android application</a> that demonstrates how to use the ACS Android SDK. 
To build and run it yourself, import it into your eclipse workspace:
<p>
1. Select File -> Import -> Existing Projects into Workspace -> Next -> Browsing to the demo's directory -> select project, then "Finish"<br />
2. Create an Android AVD:<br />
Open "Android SDK & AVD Manager -> Virtual devices -> new -> input name and select Google APIs - API Level 13 -> Create AVD"<br />
3. Android Configuration:<br />
"File -> Properties -> Android -> Project Build Target", select "Google APIs API Level 13" -> apply <br />
"Run -> Run Configurations... -> Android Application (right click) -> new -> Project Browse -> cocoafish-android-example -> Target -> select an AVD", then apply the changes.<br />
4. Set up the Google Map API debuging key<br />
See <a href="https://code.google.com/intl/zh-CN/android/add-ons/google-apis/mapkey.html" target="_blank">http://code.google.com/intl/zh-CN/android/add-ons/google-apis/mapkey.html</a> and follow the steps to get a google map debuging api key.
open file "examples/Demo/res/layout/main.xml" with a text editor, update the line 12 [android:apiKey="01JhK0bOMyGs-xmcTAL3B1h6J7F8_RiSpUoYkbA"] with your new key.
<p>Then build the project, start the AVD and run the app.<br /><br />


<h2>3-Legged OAuth</h2>

Since 2.1.1, Android SDK supports interactions with Authorization Server. It provides APIs for Android application developers to sign in/sign up/sign out users with Authorization Server. For signing-in and signing-up the SDK uses a webview to load pages from Authorization Server.

<h3>1. Create a Cocoafish object</h3>
<i>com.appcelerator.cloud.sdk.Cocoafish</i> has been enhanced to support the new authorization flows.

To create a Cocoafish object use one of the following constructors:

<pre class="prettyprint">
Cocoafish sdk = new Cocoafish(appConsumerKey);
Cocoafish sdk = new Cocoafish(appConsumerKey, appContext);
Cocoafish sdk = new Cocoafish(appConsumerKey, appContext, APIhost);
Cocoafish sdk = new Cocoafish(appConsumerKey, appConsumerSecret);
Cocoafish sdk = new Cocoafish(appConsumerKey, appConsumerSecret, appContext);
Cocoafish sdk = new Cocoafish(appConsumerKey, appConsumerSecret, appContext, APIhost);
</pre>
If <i>appConsumerSecret</i> is not passed in the SDK will fail to sign requests. <i>appContext</i> is an android.content.Context object. <i>APIhost</i> is used to specify the ACS API server. The default is api.cloud.appcelerator.com/v1/.

<p>To use 3-Legged OAuth you need to call the following method of the sdk object after it's created.</p>

<pre class="prettyprint">
sdk.useThreeLegged(true);
</pre>
Once get the sdk object you may call the following method to set the Authorization Server host other than the default.

<pre class="prettyprint">
sdk.setAuthHost("&lt;AUTH HOST OTHER THAN DEFAULT&gt;");
</pre>
<h3>2. Check Session Status</h3>
<p>The SDK doesn't take care of saving token information. Application Developers need to take care of saving token information somewhere and set it (and check its validity) to the sdk object upon application restart.</p>

<h3>3. Sign in</h3>
<p>Use one of the following methods to sign an user in.</p>

<pre class="prettyprint">
sdk.authorize(Activity activity, String action, final DialogListener listener);
sdk.authorize(Activity activity, String action, final DialogListener listener, boolean useSecure);
</pre>
<b>activity</b>: (android.app.Activity) The Android activity relevant.<br/>
<b>action</b>: (String) Should be <i>Cocoafish.ACTION_LOGIN</i>.<br/>
<b>useSecure</b>: (Boolean) Specify if HTTPS should be used for sending request. If not specified default to false.<br/>
<b>listener</b>: (com.appcelerator.cloud.sdk.oauth2.DialogListener) The listener object is used to provide various callbacks to the signing-in process. Please refer to the Listener for more detail. The most significant callback method is <i>onComplete(Bundle values)</i> where you can get token information by calling the following methods and save them as you want.

<pre class="prettyprint">
sdk.getAccessToken();
sdk.getAccessExpires();
</pre>
<p>The following code from the demo application shows a call to this method.</p>

<pre class="prettyprint">
sdk.authorize(UserView.this, Cocoafish.ACTION_LOGIN, new LoginDialogListener(), false);
</pre>
<h3>4. Sign up</h3>
<p>Use one of the following methods to sign an user up.</p>

<pre class="prettyprint">
sdk.authorize(Activity activity, String action, final DialogListener listener);
sdk.authorize(Activity activity, String action, final DialogListener listener, boolean useSecure);
</pre>
<b>activity</b>: (android.app.Activity) The Android activity relevant.<br/>
<b>action</b>: (String) Should be <i>Cocoafish.ACTION_SINGUP</i>.<br/>
<b>useSecure</b>: (Boolean) Specify if HTTPS should be used for sending request. If not specified default to false.<br/>
<b>listener</b>: (com.appcelerator.cloud.sdk.oauth2.DialogListener) The listener object is used to provide various callbacks to the signing-up process. Please refer to the Listenr class for more detail. The most significant callback method is <i>onComplete(Bundle values)</i> where you can get token information by calling the following methods and save them as you want.

<pre class="prettyprint">
sdk.getAccessToken();
sdk.getAccessExpires();
</pre>
<p>The following code from the demo application shows a call to this method.</p>

<pre class="prettyprint">
sdk.authorize(UserView.this, Cocoafish.ACTION_SINGUP, new LoginDialogListener());
</pre>
<h3>5. Sign out</h3>
<p>Signing-out should be done the same way as before. That is calling sdk.sendRequest to send a request to <i>users/logout.json</i>.
</p>

<h3>6. Login to API Server directly</h3>
To use the new authorization flow, you need to configure your app on <a href="/apps">Apps page</a>. If an app is configured to use Authorization Server for user authentication, it's not possible to log-in/sign-up to API server directly.

<h3>7. Customize webview</h3>
The webview is used to show pages loaded from Authorization Server. It's possible to customize it. The SDK has the following method to accept a com.appcelerator.cloud.sdk.oauth2.DlgCustomizer object to support customization.

<pre class="prettyprint">
sdk.setDlgCustomizer(new MyDlgCustomizer());
</pre>
For example, the following code snippet from the demo application implements a DlgCustomizer named MyDlgCustomizer.

<pre class="prettyprint">
public class MyDlgCustomizer implements DlgCustomizer {

    static final int FB_BLUE = 0xFF6D84B4;
    static final int MARGIN = 4;
    static final int PADDING = 2;

    public float[] getPortraitDimensions() {
        return new float[]{320, 420};
    }

    public float[] getLandscapeDimensions() {
        return new float[]{460, 260};
    }

    public TextView setUpTitle(Context context) {
        Drawable icon = context.getResources().getDrawable(R.drawable.cocoafish_icon);
        TextView title = new TextView(context);
        title.setText("ACS - To be customized");
        title.setTextColor(Color.WHITE);
        title.setTypeface(Typeface.DEFAULT_BOLD);
        title.setBackgroundColor(FB_BLUE);
        title.setPadding(MARGIN + PADDING, MARGIN, MARGIN, MARGIN);
        title.setCompoundDrawablePadding(MARGIN + PADDING);
        title.setCompoundDrawablesWithIntrinsicBounds(icon, null, null, null);
        return title;
    }

}
</pre>


Have Fun!

</div>
