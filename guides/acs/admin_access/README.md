# Admin Access

ACS admin access allows application admin users to execute some batch
operations and make ACS API calls on behalf of another user.

## Create an Admin User

The process of creating an admin user differs based on whether you are using the Appcelerator
Platform (enterprise version of ACS) or the community version of ACS.

### Appcelerator Dashboard (Enterprise)

Before creating an admin user, log in to the Appcelerator Dashboard and select your application.

  1. Log in to [https://dashboard.appcelerator.com](https://dashboard.appcelerator.com).
  2. Select an application from the **Apps** drop-down list.
  3. Click the **Cloud** tab.

Then, either create a new admin user or add admin access to an existing user.

#### Create a New Admin User (Enterprise)

  1. In the left navigation bar, click **Manage Data**.
  2. In the main pane, click **Users**.
  3. Click **+ New User**. A dialog appears.
  4. Under the **Admin** section, click the **Yes** radio button.
  5. At mininum, enter a username, password and confirm password.
  6. Click **Save**.

{@img admin_appc1.png}

ACS creates a new user with admin access.

#### Add Admin Access to an Existing User (Enterprise)

  1. In the left navigation bar, click **Manage Data**.
  2. In the main pane, click **Users**.
  3. Locate the user you want to give admin access to and click the pencil icon in the same row to
     edit the user.
  4. Locate the **Admin** section and click the **Yes** radio button.
  5. Scroll down and click **Save Changes**.

This user now has admin access.  To disable access, follow the same steps except click the **No**
radio button.

### Manage ACS Web Console (Community)

Before creating an admin user, log in to the Manage ACS web console and select your application.

  1. Log in to [http://cloud.appcelerator.com/apps](http://cloud.appcelerator.com/apps).
  2. Locate your application and click **Manage ACS**.

Then, either create a new admin user or add admin access to an existing user.

#### Create a New Admin User (Community)

  1. Click **Users**.
  2. Click the **Admin User** tab.
  3. Click **Create an Admin User**. A dialog appears.
  4. At minimum, enter a username, password and confirm password.
  5. Click **Submit**.

ACS creates a new user with admin access.

#### Add Admin Access to an Existing User (Community)

  1. Click **Users**.
  2. Locate the user you want to give admin access to and click the plus icon in the same row to
     edit the user.
  3. Click **Set User as Admin User**.

This user now has admin access.  To disable access, follow the same steps except click **Set User as Regular User**.

{@img admin_acs1.png}

## Perform ACS API Calls on Behalf of Another User

An admin user can perform ACS API calls on behalf of another user.  For example, when you
specify the `user_id` parameter to an ID of another user as part of the create method,
the admin user creates an object on behalf of that user. The `user` parameter for the object
will be reported as the other user not the admin user.

This admin operation is supported on any create, update and delete method, plus the following methods:

 * {@link KeyValues#append}
 * {@link KeyValues#incrby}
 * {@link KeyValues#set}
 * {@link PhotoCollections#update}
 * {@link PushNotifications#subscribe}

For example, the following curl command creates a new status for the specified user:

    curl -b cookies.txt -c cookies.txt -F "user_id=520289441e1ef70b1a0236d2" -F "message=Hola, Mundo\!" "https://api.cloud.appcelerator.com/v1/statuses/create.json?key=APP_API_KEY"
    {
      "meta": {
        "code": 200,
        "status": "ok",
        "method_name": "createStatus"
      },
      "response": {
        "statuses": [
          {
            "id": "5202c1ed87173a0afc024524",
            "message": "Hola, Mundo\\!",
            "created_at": "2013-08-07T21:53:49+0000",
            "updated_at": "2013-08-07T21:53:49+0000",
            "user": {
              "id": "520289441e1ef70b1a0236d2",
              "created_at": "2013-08-07T17:52:04+0000",
              "updated_at": "2013-08-07T17:52:04+0000",
              "external_accounts": [

              ],
              "confirmed_at": "2013-08-07T17:52:04+0000",
              "username": "not_an_admin",
              "admin": "false"
            }
          }
        ]
      }
    }


To verify that the other user created this status and not the admin user, run the following curl
command and compare the user IDs:

    curl -b cookies.txt -c cookies.txt "https://api.cloud.appcelerator.com/v1/statuses/show.json?key=APP_API_KEY&status_id=5202c1ed87173a0afc024524"
    {
      "meta": {
        "code": 200,
        "status": "ok",
        "method_name": "showStatus"
      },
      "response": {
        "statuses": [
          {
            "id": "5202c1ed87173a0afc024524",
            "message": "Hola, Mundo\\!",
            "created_at": "2013-08-07T21:53:49+0000",
            "updated_at": "2013-08-07T21:53:49+0000",
            "user": {
              "id": "520289441e1ef70b1a0236d2",
              "created_at": "2013-08-07T17:52:04+0000",
              "updated_at": "2013-08-07T17:52:04+0000",
              "external_accounts": [

              ],
              "confirmed_at": "2013-08-07T17:52:04+0000",
              "username": "not_an_admin",
              "admin": "false",
              "stats": {
                "photos": {
                  "total_count": 0
                },
                "storage": {
                  "used": 0
                }
              }
            }
          }
        ]
      }
    }

<!-- 

## Admin Batch Delete

Admin Batch Delete allow admin users to delete multiple ACS objects in one
delete operation. ACS provides an API end point named
`admin_batch_delete` for application admin users. When calling the `admin_batch_delete`
method, the admin user provides a query condition to select the objects to
delete. The query condition is provided by passing the `where` parameter. If
`where` is omitted, all objects are deleted.  
  
For example:
    
     $curl -b cookies.txt -c cookies.txt -X DELETE -F "where={\"favorite_color\":\"blue\"}" https://api.cloud.appcelerator.com/v1/users/admin_batch_delete.json?key=xBzAKXWFl36S4MAD7KNt2jw30EKM4Kxn 	
     {
      "meta": {
        "status": "ok",
        "code": 200,
        "method_name": "adminBatchDelete"
      }
    }
     

The following ACS objects allow admins to perform batch
delete operations:

  * {@link Checkins}
  * {@link PhotoCollections}
  * {@link Events}
  * {@link Files}
  * {@link CustomObjects}
  * {@link Photos}
  * {@link Places}
  * {@link Posts}
  * {@link Statuses}
  * {@link Users}

-->

## Admin Drop Custom Collection

An application admin user can also drop a Custom Object collection using 
`admin_drop_collection` method. When calling the `admin_drop_collection` method, 
the admin user must specify a class name to indicate which custom collection to drop.  
  
For example:

    $ curl -b c.txt -c c.txt -X DELETE "https://api.cloud.appcelerator.com/v1/objects/car/admin_drop_collection.json?key=hPkMYgNozXR8xegNvWjqBVTcWK8P5fIX"
    {
      "meta": {
        "status": "ok",
        "code": 200,
        "method_name": "dropCollection"
      }
    }
     
The above example drops a car collection. Only Custom Objects support the drop
custom collection method.

