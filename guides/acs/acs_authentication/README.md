# Authentication

## App Key over SSL

Your app must prove that it is allowed to talk to ACS. This keeps your data secure by preventing anyone from making requests to ACS that impersonate your app. The easiest way to authenticate API requests to ACS is to supply an ACS app key with each request as a URL parameter:

<pre class="prettyprint">GET https://api.cloud.appcelerator.com/v1/places/search.json?<b>key=<span class="display_key">&lt;YOUR_APP_KEY&gt;</span></b></pre>

ACS defaults to App key over SSL for better security. 

## 2-Legged OAuth

If for some reason SSL is not available, ACS also provides secure authentication via 2-Legged OAuth. This is a process by which a key and secret are used to sign each request made by your app. When the ACS server receives your request, the secret is used along with the data sent in the request to calculate another signature. If sent signature and calculated signature match, the request will be processed.

Here is an example of an OAuth HTTP header added to an API request:

<pre class="prettyprint">
Authorization: OAuth oauth_consumer_key="0685bd9184jfhq22",
        oauth_token="",
        oauth_signature_method="HMAC-SHA1",
        oauth_signature="wOJIO9A2W5mFwDgiDvZbTSMK%2FPY%3D",
        oauth_timestamp="137131200",
        oauth_nonce="4572616e48616d6d65724c61686176",
        oauth_version="1.0"
</pre>

This authentication method is the safer over http since the secret used to generate the signature is known only by the app and the ACS server. It is never sent over the network. The OAuth consumer key and secret for an app can be found by going to the <a href="/apps">Apps page</a> and clicking on the name of the app.

The following is an example of making a 2-Legged OAuth request using Ruby:

<pre class="prettyprint">
require 'rubygems'
require 'oauth'

# make the consumer out of your secret and key
consumer_key = "OlosyCTFQpI7foZVFnynFCJvW60Tnqbr"
consumer_secret = "5mP2yiOKSHOQkvrFMmgUJS9zd0OtTZIe"
consumer = OAuth::Consumer.new(consumer_key, consumer_secret, :site => "http://api.cloud.appcelerator.com")

# make the access token from your consumer
access_token = OAuth::AccessToken.new consumer

# make a signed request!
response = access_token.get("/v1/places/search.json")

# show the response
puts response.body
</pre>

Almost any OAuth library that supports 3-Legged OAuth (used by Facebook, Twitter, Foursquare, and others) can also support 2-legged OAuth. Provide your ACS OAuth key and secret as the consumer key and secret. Use an empty string ("") as both the Access Token and Secret.

## 3-Legged OAuth

<p>Since there is the possibility that mobile apps could reveal its secret ACS also supports OAuth 2.0 implicit authorization flow.
(OAuth 2.0 implicit authorization flow is suitable for clients incapable of maintaining their client credentials confidential such as client applications residing
  in a user-agent, typically implemented in a browser using a scripting language such as JavaScript, or native applications.)
Using implicit authorization flow a mobile app receives the access token as the result of the authorization request. The mobile app can then use the
access token to make API calls on behalf of the user.</p>

<p>To enable 3-Legged OAuth for your app please go to <a href="/apps">Apps page</a> and click on the name of the app, then go to Settings page. You should see the
following section there. Select Authorization Server for User Authentication Scheme and specify the valid time for access tokens (defaults to 1 hour).</p>

{@img app_setting_as.png}

<p>With 3-Legged OAuth, user log-in and sign-up will be done on Authorization Server. According to OAuth 2.0 implicit authorization flow only OAuth key
is needed. However, as iOS and Android applications are safer than javascript applications OAuth secret can still be provided for them.</p>

<p>Here is an example of an request sent to Authorization Server for signing-in:</p>

<pre class="prettyprint">
http://secure-identity.cloud.appcelerator.com/oauth/authorize?client_id=VGJSVgFHs7FaOcgcvMWMAGe6bwNpHBfq&response_type=token&redirect_uri=acsconnect://success
</pre>

<p>Here is an example of an request sent to Authorization Server for signing-up:</p>

<pre class="prettyprint">
http://secure-identity.cloud.appcelerator.com/users/sign_up?client_id=VGJSVgFHs7FaOcgcvMWMAGe6bwNpHBfq&redirect_uri=acsconnect://success
</pre>

<p>The existing logout API can still be used to log an user out. Here is an example of an request sent to API server for signing-out:</p>

<pre class="prettyprint">
http://api.cloud.appcelerator.com/v1/users/logout.json?oauth_consumer_key=VGJSVgFHs7FaOcgcvMWMAGe6bwNpHBfq&access_token=eMdbgRgmsUwUnljJSrlkCOuZnKNVCdsRp9EVFCzp
</pre>

<p>Android and Javascript SDKs now support this new authorization flow. For details please refer to the corresponding pages.</p>

<a href="/docs/javascript">Javascript SDK</a><br/>
<a href="/docs/android">Android SDK</a>

## Access Control Lists (ACLs)

Access Control Lists (ACLs) provide several APIs to implement access control lists for ACS objects. An access control list controls read and write access to ACS objects it's attached to. Please refer to <a href="/docs/api/v1/acls/info">Access Control List</a> for more information.
