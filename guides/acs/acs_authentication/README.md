# Authentication

## App Key over SSL

Your app must prove that it is allowed to talk to ACS. This keeps your data secure by preventing anyone from making requests to ACS that impersonate your app. The easiest way to authenticate API requests to ACS is to supply an ACS app key with each request as a URL parameter:

<pre class="prettyprint">GET https://api.cloud.appcelerator.com/v1/places/search.json?<b>key=<span class="display_key">&lt;YOUR_APP_KEY&gt;</span></b></pre>

ACS defaults to App key over SSL for better security. 

## Access Control Lists (ACLs)

Access Control Lists (ACLs) provide several APIs to implement access control lists for ACS
objects. An access control list controls read and write access to ACS objects it's
attached to. Please refer to {@link ACLs Access Control Lists} for more information.
