# Admin Access

ACS admin access allows application admin users to execute some batch
operations.

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

