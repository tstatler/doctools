# ACS Node SDK

The ACS Node SDK lets you easily integrate ACS cloud services with your Node application. The SDK
provides two APIs:

* A standard API that mirrors the one provided by the
  [Ti.cloud](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud) client-side module.
  The examples from the Ti.Cloud documentation can be easily adapted for use with the ACS Node SDK.
* An equivalent REST API.

## Installing

You install the ACS Node SDK using `npm`:

    [sudo] npm install acs-node

## Using the ACS APIs

To use the standard ACS APIs you first require the
`acs-node` module and call its `initACS()` method, passing it your ACS application key:

    var ACS = require('acs-node');
    ACS.initACS('<App Key>');

This only needs to be done once, typically in the main `app.js` script file.

Below is a more complete example that uses the standard ACS APIs to
login a user. It defines a custom `login()` function that takes the `username` and `password`
properties from the HTTP request body and, in turn, passes those values as input to the
[`Users.login()`](http://docs.appcelerator.com/cloud/latest/#!/api/Users- method-login) method. On
successful login, the user's information is displayed in the console or, in case of an error, the
error response is displayed.

    var ACS = require('acs-node');
    ACS.initACS('<App Key>');
    function login(req, res) {
        var data = {
            login: req.body.username,
            password: req.body.password
        };
        ACS.Users.login(data, function(response){
            if(response.success) {
                console.log("Successful to login.");
                console.log("UserInfo: " + JSON.stringify(response.users[0], null, 2))
            } else {
                console.log("Error to login: " + response.message);
            }
        }, req, res);
    }

A complete [sample project](https://github.com/appcelerator/acs-node-sdk/tree/master/examples/UserWithACSAPI) is available on GitHub.

### Using the REST APIs ###

To use the REST API you assign the return value of `ACS.initACS()` to a local object.
This object provides a `rest()` method you use to make REST requests directly to ACS. The `rest()`
method has the following signature:

<code>rest(<em>resource</em>, <em>action</em>, <em>action</em>, <em>callback</em>)</code>

* `resource` -- The URL of the REST resource to call.
* `method` -- The HTTP method to invoke on the resource.
* `data` -- The data object to pass to the resource.
* `callback` -- The function to callback when the request completes.

The following code demonstrates basic REST API usage:

    var ACS = require('acs-node');
    var sdk = ACS.initACS('<App Key>');
    var resource "users/login.json";
    var method = 'POST';
    var data = {username: 'joesmith', password: 'pwd'};
    function handleLogin(response) {
        // Handle response
        if(response) { ... }
    }
    sdk.rest(resource, method, data, callback);

Below is a more complete example using REST that's functionally equivalent to the [previous version](#usingtheacsapis)
that used the standard ACS API.

    var ACS = require('acs-node');
    var sdk = ACS.initACS('<App Key>');
    function login(req, res) {
        var data = {
            login: req.body.username,
            password: req.body.password
        };
        sdk.rest('users/login.json', 'POST', data, function(data){
            if(data && data.meta) {
                if(data.meta.status == 'ok') {
                    console.log("Successful to login.");
                    console.log("UserInfo: " + JSON.stringify(data.response.users[0], null, 2))
                } else {
                    console.log("Error to login: " + data.meta.message);
                }
            } else {
                console.log("Error to login, try again later.");
            }
        }, req, res);
    }

A complete REST [sample project](https://github.com/appcelerator/acs-node-sdk/tree/master/examples/UserWithREST) is available on GitHub.

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

*   The ACS library sets the cookie header in the response object, which must be done _before_
    sending any response data (for example, by calling the response object's `send` method). If you
    send any response data _before_ the ACS API callback function is invoked, the ACS library will
    throw an exception when it tries to set the cookie headers, with a message like, "Can't render
    headers after they are sent to the client."

*   Session information is stored in a cookie named `_session_id`. You can also manually set this
    session ID cookie on the client side. For example, if you are calling your Node.ACS service from
    a Titanium application that uses ACS directly, you can retrieve the active session ID from the
    [Titanium.Cloud.sessionId](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Cloud-
    property-sessionId) property, and adding a `Set-Cookie` header when making a request to the
    Node.ACS service.

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

