
# Atomic Increment Operator

ACS supports the Mongo `$inc` atomic increment operator.

## `$inc`

ACS supports the use of the `$inc` atomic increment operator in `update`
api calls. You can use `$inc` to increment a custom field by the specified value
in a single operation. The `$inc` operator can only can be applied to a single
field per method call.  
  
`$inc` is specified in the Update api with the following form:  

    "_fieldName_": { $inc: _value_}  
  
Where _fieldName_ is the name of the field to increment and _value_ is the
value to increment by (_value_ can be positive or negative).  
  
Here are 2 examples:
    
    $ curl -b c.txt -c c.txt -X PUT -F "id=511117915554f74313000009" -F "fields={"favorite":"play xbox 360", "pet":"shark" ,"score":{$inc:10}}" "https://api.cloud.appcelerator.com/v1/objects/family/update.json?key=TENIhpXtjFbkBbztvfZMwnciOjE9aHjd"
    {
      "meta": {
        "code": 200,
        "status": "ok",
        "method_name": "updateCustomObject"
      },
      "response": {
        "family": [
          {
            "family_name": "ACS",
            "score": 10,
            "age": 40,
            "cars": 1,
            "favorite": "play xbox 360",
            "pet": "shark",
            "id": "511117915554f74313000009",
            "created_at": "2013-02-05T14:30:41+0000",
            "updated_at": "2013-02-05T14:30:41+0000",
            "user": {
              "id": "511117905554f74313000003",
              "first_name": "Alice",
              "last_name": "Gal",
              "created_at": "2013-02-05T14:30:40+0000",
              "updated_at": "2013-02-05T14:30:41+0000",
              "external_accounts": [
    
              ],
              "confirmed_at": "2013-02-05T14:30:40+0000",
              "username": "alice",
              "email": "alice@gal.com",
              "admin": "false"
            }
          }
        ]
      }
    }
    
    $ curl -b c.txt -c c.txt -X PUT -F "checkin_id=511111945554f742d300000b" -F "custom_fields={"favorite":"play xbox 360", "pet":"shark" ,"score":{$inc:10}}" "https://api.cloud.appcelerator.com/v1/checkins/update.json?key=TENIhpXtjFbkBbztvfZMwnciOjE9aHjd"
    {
      "meta": {
        "code": 200,
        "status": "ok",
        "method_name": "updateCheckin"
      },
      "response": {
        "checkins": [
          {
            "id": "511111945554f742d300000b",
            "created_at": "2013-02-05T14:05:08+0000",
            "updated_at": "2013-02-05T14:05:08+0000",
            "place": {
              "id": "511111935554f742d3000009",
              "name": "Maya Restaurant",
              "created_at": "2013-02-05T14:05:07+0000",
              "updated_at": "2013-02-05T14:05:07+0000",
              "address": "303 2nd Street",
              "city": "San Francisco",
              "state": "CA",
              "country": "United States",
              "phone_number": "(415) 543-2928",
              "latitude": 37.784732,
              "longitude": -122.395441,
              "google_cid": "7106049823222705125",
              "user": {
                "id": "511111925554f742d3000003",
                "first_name": "Alice",
                "last_name": "Gal",
                "created_at": "2013-02-05T14:05:06+0000",
                "updated_at": "2013-02-05T14:05:08+0000",
                "external_accounts": [
    
                ],
                "confirmed_at": "2013-02-05T14:05:06+0000",
                "username": "alice",
                "email": "alice@gal.com",
                "admin": "false"
              }
            },
            "user": {
              "id": "511111925554f742d3000003",
              "first_name": "Alice",
              "last_name": "Gal",
              "created_at": "2013-02-05T14:05:06+0000",
              "updated_at": "2013-02-05T14:05:08+0000",
              "external_accounts": [
    
              ],
              "confirmed_at": "2013-02-05T14:05:06+0000",
              "username": "alice",
              "email": "alice@gal.com",
              "admin": "false"
            },
            "custom_fields": {
              "family_name": "ACS",
              "score": 10,
              "age": 40,
              "cars": 1,
              "favorite": "play xbox 360",
              "pet": "shark"
            }
          }
        ]
      }
    }
    

  
If you apply $inc to multiple fields in one Update call, you will get error:

    
    
    $ curl -b c.txt -c c.txt -X PUT -F "checkin_id=511111945554f742d300000b" -F "custom_fields={"favorite":"play xbox 360", "pet":"shark" ,"score":{$inc:10}, "age":{$inc:10}}" "http://api.cloud.appcelerator.com/v1/checkins/update.json?key=HSejkGE9ghavAelMJv7bZYNM5HyMhqYq"
    {
      "meta": {
        "status": "fail",
        "code": 400,
        "message": "$inc operation only support to increase one field once.",
        "method_name": "updateCheckin"
      }
    }
    

The following ACS methods support the `$inc` operator:

  * {@link Checkins#update}
  * {@link Collections#update}
  * {@link Events#update}
  * {@link Files#update}
  * {@link CustomObjects#update}
  * {@link Photos#update}
  * {@link Places#update}
  * {@link Posts#update}
  * {@link Reviews#update}
  * {@link Statuses#update}
  * {@link Users#update}

