# Troubleshooting Guide

## Titanium SDK and Studio

### Error enabling Cloud service for project

If you receive a message similar to "Error enabling Cloud service for project" in Studio when trying
to enable Cloud services for your project, the ACS server may be down or Studio is unable to connect
to the ACS server.  Try to enable Cloud services later.

If you are still receiving this error when trying to enable Cloud services, check to see if your
application was created in either [https://my.appcelerator.com/apps](https://my.appcelerator.com/apps)
(for an application created in Titanium Studio) or [https://dashboard.appcelerator.com/](https://dashboard.appcelerator.com/)
(for an application created in Appcelerator Studio).

If the application was created, check to see if ACS keys were created for the application. To find your ACS keys:

  * If you are using Titanium Studio (free, community version), go to
    [https://my.appcelerator.com/apps](https://my.appcelerator.com/apps)
    and click on the **Manage ACS** link below your application. You should see items for **APP KEY**, **OAuth Consumer
    Key** and **OAuth Secret**.  Note that you need both the Development and Production version of these
    items.  You can switch between the two by pressing the **Development** and **Production** buttons in the
    top-right corner of the web page. <br/><br/>
 
  * If you are using Appcelerator Studio (paid, enterprise version), go to
    [https://dashboard.appcelerator.com/](https://dashboard.appcelerator.com/),
    select your application from the **Apps** drop-down list, click the
    **Cloud** tab, then click **Settings & Configuration**.  You should see items for **App Key**, **OAuth Consumer
    Key** and **OAuth Secret**.  Click the **Show** link to expand these items.  Note that you need both the
    Development and Production version of these items.  You can switch between the two by clicking the
    drop-down box in the top-right corner that displays either **Development** or **Production**.

If you do *not* have ACS keys, try to enable Cloud services again at a later time.

If you do have ACS keys, manually enter the ACS key information in the `tiapp.xml` file.
To manually enter this information:

  1. Double-click your `tiapp.xml` file to open it in the **Editor**.
  2. Click the **tiapp.xml** tab in the lower-left corner of the **Editor**.
  3. Insert the following ACS property keys as children of the `ti:app` parent tag and replace with the
     application's ACS keys found earlier: 

        <?xml version="1.0" encoding="UTF-8"?>
        <ti:app xmlns:ti="http://ti.appcelerator.org">
            <!-- Add these six tags and replace with your application's ACS keys -->
            <property name="acs-oauth-secret-development" type="string">OAUTH_CONSUMER_SECRET_DEV</property>
            <property name="acs-oauth-key-development" type="string">OAUTH_CONSUMER_KEY_DEV</property>
            <property name="acs-api-key-development" type="string">APP_KEY_DEV</property>
            <property name="acs-oauth-secret-production" type="string">OAUTH_CONSUMER_SECRET_PROD</property>
            <property name="acs-oauth-key-production" type="string">OAUTH_CONSUMER_KEY_PROD</property>
            <property name="acs-api-key-production" type="string">APP_KEY_PROD</property>
            <!-- Add these two tags if you are using Appcelerator Studio -->
            <property name="acs-authbase-url" type="string">https://secure-identity.cloud.appcelerator.com</property>
            <property name="acs-base-url" type="string">https://api.cloud.appcelerator.com</property>
            ...
        </ti:app>

  4. Save and close your `tiapp.xml` file.
  5. Reopen your `tiapp.xml` file.  In the **Overview** tab, it should show that Cloud services is enabled.

