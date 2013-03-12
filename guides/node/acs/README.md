# ACS Support in Node.ACS

Node.ACS has a built-in ACS library for seamlessly integrating ACS cloud
services in your Node.ACS application. The APIs provided by the library are
almost identical to the APIs provided by the Titanium Ti.cloud module.

It is trivial to adapt most of the examples from the [Ti.Cloud documentation](
http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) to use ACS
in a Node.ACS application.

## Setting Up The Library

1\. Import 'acs' Module

2\. Initialize ACS OAuth Credentials

Before using ACS cloud services, you need to import the 'acs' library into
your app:
    
    var ACS = require('acs').ACS

This module has been setup in the node environment for you by Node.ACS
already, you don't need to worry about the module's lookup path.

Initialize the 'acs' module with your ACS OAuth credentials.  
    
    ACS.init('<OAuth key>', '<OAuth secret>')

This only needs to be done once, and is typically done in the main `app.js` script
file.

## Using the ACS APIs

Now let's use ACS in a Node.ACS application, we'll query all available places
in the ACS app and return through response:
    
    var ACS = require('acs').ACS;
    ACS.init('<OAuth key>', '<OAuth secret>');
    
    function queryAllPlaces(req, res) {
        ACS.Places.query({
            page: 1,
            per_page: 20,
            where: {
                lnglat: { '$nearSphere': [-122.23, 37.12], '$maxDistance': 0.00126 }
            }
        }, function(data) {
            if(data.success) {
                res.send(data);
            } else {
                res.send(
                    'Error occured. Error code: ' + data.error + '. Message: ' + data.message);
            }
        });
    }
    
## User Login Session Management

Most of ACS APIs require a user to be logged in, so it is important to have a
way to manage user sessions in your Node.ACS application. Node.ACS provides
two ways of managing ACS login sessions in a Node.ACS application:

  * **Cookie-based**. With cookie-based session management, most of the management is done for you.
  * **Manual**. Allows you to manage your own login sessions.

These methods are described in the following sections.

### Cookie-Based Session Management

Cookies are frequently used by ACS applications to store session information
and pass it between client and server. ACS cookies can be used with Node.ACS
as well. To enable cookies to be passed through between the client and ACS,
pass in the HTTP request and response objects as parameters when making an ACS
API call. For example:

    function loginUser(req, res) {
        ACS.Users.login({
            login: 'test', 
            password: 'test'
        }, function(data) {
            res.send('User logged in!');
        }, req, res);
    }
    
The ACS library retrieves the session ID from the request's cookies. If a
`_session_id` cookie is present, it uses that session ID to make the ACS API
call. If not, it performs a regular API call without session information.

If a session ID is returned in the ACS API response (for example,
`users/login.json`), the session information is added into the response
object. Specifically, it adds a `Set-Cookie` header to pass back the Node.ACS
project's client.

**Important**

*   The ACS library sets the cookie header in the response object, which must be done _before_ sending any response data (for example, 
    by calling the response object's `send` method). If you send any response data _before_ the ACS API callback function is invoked, 
    the ACS library will throw an exception when it tries to set the cookie headers, with a message like, "Can't render headers after 
    they are sent to the client."

*   Session information is stored in a cookie named `_session_id`. You can also manually set this session ID cookie on the client side. 
    For example, if you are calling your Node.ACS service from a Titanium application that uses ACS directly, you can retrieve the active 
    session ID from the [Titanium.Cloud.sessionId](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud-property-sessionId) 
    property, and adding a `Set-Cookie` header when making a request to the Node.ACS service.

### Manual Session Management

An ACS user login session is identified by a `session_id` parameter in the
request or response data. When logging in to a user account or creating a new
user, the `session_id` is returned in the response data of the API calls. It
can be retrieved from the response data by using `data.meta.session_id`. For
example:
    
    function loginUser(req, res) {
        ACS.Users.login({
            login: 'test', 
            password: 'test'
        }, function(data) {
            res.send('Login session is: ' + data.meta.session_id);
        });
    }
    
To reuse this session for making other API calls, pass it in as part of the
request data (`session_id: _stored_session_id_`). This gives you full control
of the sessions, you can store the session in any ways and reuse them anytime
(as long as the session is not expired on ACS server) later for making API
calls. For example:
    
    function createPlace(req, res) {
        ACS.Places.create({ 
            name: 'test', 
            city: 'city_name', 
            session_id: '<stored session_id>'
        }, function(data) {
            res.send('New place created!');
        });
    }
    
