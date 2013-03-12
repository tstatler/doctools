# Release Notes

  * 31 Jan 2013
  * 21 Jan 2013

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
  * <https://github.com/cocoafish/cocoafish-android-sdk>. For more information on the SDK,
  * see [Getting Started: Using the Android SDK](#!/guide/android)

