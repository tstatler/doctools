# ACS Release Notes

## 26 September 2013

This update includes the following bug fixes and enhancements:

  * The query methods support two new parameters: `sel` and `unsel`.  Use these parameters to
    specify which fields to return or not to return.  You cannot use these parameters together.

  * Website: Added new feature to unsubscribe devices from push noticifactions using
    the ACS web console.

  * Fixed an issue where the `$inc` operation was not autoincrementing a custom field.


## 1 August 2013

### Google Cloud Messaging for Android Push Notifications

ACS now supports Google Cloud Messaging (GCM) for push notifications on Android devices.

For instructions on setting up GCM, see the "Configure Your App For Enabling Push Notifications"
subsection under the "Push Notifications" section of the [Android SDK guide](#!/guide/android).

To send push notifications, refer to [PushNotifications](#!/api/PushNotifications).


## 10 June 2013

### Fixed Issues and Enhancements

This update includes the following bug fixes and enhancements:

  * Removed dependency between push notifications, and device and user registrations.
    Users are no longer required to have an ACS account to receive push notifications.

  * Fixed an issue where using special characters cause the query to fail.

  * Website: Fixed an issue viewing relational field objects.
    Relational field objects were being displayed as objects and not ID strings.

  * Website: Fixed an issue viewing custom objects.
    Some custom objects could not be viewed in the web interface.

  * Website: Fixed an issue with SMTP settings.
    If a TLS value was specified, it was not properly checked.

### Future Behavior Changes

In a future release, currently scheduled in a few months,
the following changes are being made to user sessions and geo query.

#### Application User Session Expiration

An application user session never expires today.  We are introducing a policy of expiring and
removing sessions that have been inactive for six months.

If your application logins a user and saves the `session_id`,
normally stored in a cookie, every time it makes a REST call to ACS using the same `session_id`, the
expiry clock is reset and the user gets another six months. As long as the ACS user is active using
the same `session_id` within six months, there is no impact on your application and currently logged in
user. If an application user is completely inactive for six months or more, this user session is
removed and any subsequent ACS call that requires user login such as `create.json`, `update.json` and
`remove.json` will get a 404 error. We recommend your application to handle an invalid user session
error and prompt a login screen to the user to login again.

#### Geo Query

ACS currently supports MongoDB’s
[$nearSphere](http://docs.mongodb.org/manual/reference/operator/nearSphere/) geo query.
Geo query requires a field to be indexed with a geo index.
The ACS fields you can perform `$nearSphere` on are `lnglat` (pre-defined location
data and only available in [Places](http://docs.appcelerator.com/cloud/latest/#!/api/Places)
and [Events](http://docs.appcelerator.com/cloud/latest/#!/api/Events)) and `coordinates`
(list of custom defined location data and available in all objects).
It implies that Places and Events have two geo indexes in the same
collection and that prevents us from supporting the
[$geoNear](http://docs.mongodb.org/manual/reference/command/geoNear/) operation that is more powerful than
`$nearSphere`.  We will consolidate the `lnglat` value with the `coordinates` values and remove geo index on
the `lnglat` field.

For Events and Places, even if you never explicitly copied
the `lnglat` value to `coordinates`, `lnglat` appears as the first element of `coordinates`.  Performing
`$nearSphere` on the `coordinates` field returns a match if it matches the `lnglat` value.  `$nearSphere`
query on `lnglat` or `coordinates` continues to work as before.

## 26 Apr 2013 

This update includes bug fixes and performance improvements.

## 19 Apr 2013 -- Session Expiration Policy Update

On May 15th, Appcelerator will start enforcing a new expiration policy for user sessions.
Previously, user sessions were never removed from the database, no matter how long 
they had been idle.

Starting May 15th, user login sessions will expire after they have been unused for a period of time.
By default, the expiration period is six months. You can configure the user session 
expiration period in the application management console.

## 11 Apr 2013

This update included the following bug fixes:

  * Fixed a regression causing user confirmation email requests to fail with an error ("400 Bad Request - Invalid app key").

  * When querying ACS objects, regular expressions are limited to those expressions that can be processed efficiently. To be processed efficiently, the regex must be _anchored_ at the beginning of the string with "^" followed by a letter or digit. The initial character must be case sensitive. For example, "^[aA]" and ".*Foo" are not allowed, but "^a.*Foo" is allowed.

  * Website: Fixed an issue with creating places. When creating an event from the website, the place ID was not added to the event, even though a place is selected.

  * Website: Fixed an issue with photo collections. If an error was encountered when browsing a subcollection on the photo collection page, it caused an infinite redirect loop.

## 28 Mar 2013

This update included a number of bug fixes and scalability improvements.
Notable fixes include:

  * Fixed an error that occurred when trying to create an event with the `recurring` field set. 

  * Fixed an issue that prevented editing of custom fields using the ACS web site.

  * Fixed an issue that prevented tags from being deleted using the ACS web site.

## 14 Mar 2013

Added support for iOS Newsstand `content-available` flag in push
notifications. Setting `content-available: 1` in the payload of a push
notification identifies it as a Newsstand push notification used to initiate
background download. Note that this feature is only supported by Newsstand
apps. For more information, see the [Apple Newsstand
FAQ](http://developer.apple.com/library/ios/#technotes/tn2280/_index.html) on
the iOS Developer Center.

## 14 Feb 2013

Added new admin operation:

  * Admin Drop Custom Collection allows admin users to drop a Custom Object collection.

For details, see [Admin Access](#!/guide/admin_access).

Added support for atomic increment operator, $inc. For details see [Atomic
Increment Operation](#!/guide/atomic_increment).

Fixed ACS website issues:

  * Places could not be added manually from the website.
  * Longitude and latitude fields were limited to 4 characters.
  * Custom field boolean could be interpreted as a string.

## 31 Jan 2013

Fixed an unhandled exception when a file was passed as the payload of a push
notification. For example, a `curl` command like this would cause an
exception:
    
    curl -b cookies.txt -c cookies.txt -F "channel=change_request" -F "to_ids=<ids>" 
    -F "payload=@photo2.jpg"
    https://api.cloud.appcelerator.com/v1/push_notification/notify.json?key=<api_key>
    

File payloads are not allowed. With the fix, ACS supplies an error message
instead of throwing an exception.

## 21 Jan 2013

The ACS service was updated today with a number of bug fixes and improvements.
Highlights include:

  * Updated API usage reporting to report number of pushes.
  * On the ACS website, added ability to add a record to an existing custom object without requiring the user to duplicate and recreate the object.
  * Fixed an issue where HTML tags were stripped from custom object fields when editing the fields in the ACS website.
  * When exporting data from the website, the mechanism for selecting date ranges is improved, and invalid date ranges are rejected.
  * Fixed an issue that prevented users from unsubscribing from push notifications when multiple users subscribe to push notifications from the same device.
  * A number of fixes to the ACS web administration console.
  * An update was made to the ACS Android SDK. You can download the latest version from
  * <https://github.com/cocoafish/cocoafish-android-sdk>. For more information on the SDK, see [Getting Started: Using the Android SDK](#!/guide/android).

