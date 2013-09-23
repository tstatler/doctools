#  Custom Objects & Fields

##  Custom Objects and Custom Fields

Appcelerator Cloud Services provides many types of commonly used predefined
objects such as {@link Users} and {@link Photos}. However, there is likely to be
extra data types you would like to use or extra data fields you would like to
store together with predefined objects. That's where our Custom Objects and
Custom Data Fields can be used.

##  Create Custom Objects

If you would like to create custom objects with custom object type, please
refer to {@link CustomObjects} to get a list of API calls that can be used to create and access
custom objects.

##  Add Custom Fields to Predefined Objects

If you would like to store additional custom data into any predefined
Appcelerator Cloud Services objects, you can simply pass in JSON encoded
custom_fields. Any number of custom fields can be specified for an instance of
a predefined object.  
  
For example, if you are using the Users API and want to store the age and
favorite color of each user, simply include JSON encoding of custom_fields

    
    
    custom_fields='{
    	"age": 23,
    	"favorite_color": "blue"
    }'
    

For example, to associate the above custom fields in user create

    
    
    $ curl -b cookies.txt -c cookies.txt -X POST --data-urlencode "email=john.smith@company.com" --data-urlencode "role=teacher" --data-urlencode "first_name=John" --data-urlencode "last_name=Smith" --data-urlencode "password=pass" --data-urlencode "password_confirmation=pass" --data-urlencode 'custom_fields={"age":23, "favorite_color":"blue"}' https://api.cloud.appcelerator.com/v1/users/create.json?key=<YOUR APP APP KEY>
    {
      "meta": {
        "status": "ok",
        "code": 200,
        "method_name": "createUser",
        "session_id": "xdqCplQqcXBq8WW1ir9nzq5U4nE"
      },
      "response": {
        "users": [
          {
            "id": "4ec5907bd9ca72020c000005",
            "first_name": "John",
            "last_name": "Smith",
            "created_at": "2011-11-17T22:53:48+0000",
            "updated_at": "2011-11-17T22:53:48+0000",
            "external_accounts": [
    
            ],
            "role": "teacher",
            "email": "john.smith@company.com",
            "custom_fields": {
              "age": 23,
              "favorite_color": "blue"
            },
            "stats": {
              "photos": {
                "total_count": 0
              },
              "storage": {
                "used": 0
              }
            }
          }
        ]
      }
    }
    

Custom Data are returned in the `custom_fields` JSON response field in the
type that was specified. Attempting to define custom fields using invalid
types or an incorrect naming convention will be silently ignored.

##  Supported Data Types

<table class="doc-table">
	<tr><th>Type</th><th>Example</th>
	<tr>
		<td>Boolean&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>true or false</td>
	</tr>
	<tr>
		<td>String&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>"blue"</td>
	</tr>
	<tr>
		<td>Number&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>23 or 1.234</td>
	</tr>
	<tr>
		<td>Date&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>"2011-11-02 17:07:37 -0700". If a string value matches date format "yyyy-mm-dd hh:mm:ss +zzzz" or "yyyy-mm-ddThh:mm:ss+zzzz", it will be converted to Date type on the Appcelerator Cloud Services backend</td>
	</tr>
</table>

You could also store more complex data types such as Array and Hash. Hash and Array can be embedded into each other. Currently, data stored inside an Array or Hash is not queryable.
    
<table class="doc-table">
<tr><th>Type</th><th>Example</th>
<tr>
	<td>Hash&nbsp;&nbsp;</td>
	<td>{"age":23,"scores":{"math":90, "physics":100}, "my_favorite_colors":["blue","red"]}</td>
</tr>
<tr>
	<td>Array&nbsp;&nbsp;</td>
	<td>["nissan", "honda"] or [2006, 2008], [{"age":28}, {"color":"blue"}]</td>
</tr>
</table>
    	
    
    

##  Geographic Coordinates in Custom Fields

To enable geographical search, there is a predefined custom field,
`coordinates`, for optionally storing geographic coordinates. The `coordinates` field can
store a single location with format [longitude, latitude] or multiple
locations [[longitude1,latitude1], [longitude2, latitude2]...]. So for the
above example, to store location information about the user, we
might have:

    
    
    custom_fields = '{ "color": "blue",
    	  "age": 23,
    	  "coordinates": [-122.1, 37.1] }'
    

##  Remove a Field

If you wish to remove a custom field during update, simply set the field value
to null.  
    
    {
    	"age": null
    }
    

##  Querying Custom Fields

Data stored in custom fields other than Array and Hash can be queried together
with predefined fields. Please refer to [Query](#!/guide/search_query-section-2) 
for more information. If you define a
custom field name that is the same as one of predefined fields, you will be
able to store and retrieve it but you won't be able to query on it since the
query action would be performed on the predefined field instead. For example,
{@link Users} has a predefined field called `first_name`,
if you define a custom field also called `first_name`, when you try to query
first_name. it will only query against the predefined `first_name` field.

##  Availability

The following Appcelerator Cloud Services objects allow you to add one or more
extra data fields during `create` and `update` actions:

  * {@link Chats#create Chats.create}
  * {@link Checkins#create}
  * {@link PhotoCollections#create} and {@link PhotoCollections#update update}
  * {@link Events#create} and {@link Events#update update}
  * {@link Files#create} and {@link Files#update update}
  * {@link Messages#create}
  * {@link Photos#create} and {@link Photos#update update}
  * {@link Places#create} and {@link Places#update update} 
  * {@link Posts#create} and {@link Posts#update update}
  * {@link Reviews#create} and {@link Reviews#update update}
  * {@link Statuses#create}
  * {@link Users#create} and {@link Users#update update}

##  iOS

In iOS, you can simply create a NSDictionary to represent a predefined
object's custom fields. Here is the mapping of data types in iOS:

<table class="doc-table">
		<tr><th>Type</th><th>Example</th><th>iOS Class</th>
		<tr>
			<td>String&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>"blue"&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>NString</td>
		</tr>
		<tr>
			<td>Number&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>123 or 1.234</td>
			<td>[NSNumber numberWithInt:] or [NSNumber numberWithDouble:]&nbsp;&nbsp;&nbsp;&nbsp;</td>
		</tr>
		<tr>
			<td>Boolean&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>true or false</td>
			<td>[NSNumber numberWithBoo:]&nbsp;&nbsp;&nbsp;&nbsp;</td>
		</tr>
		<tr>
			<td>Date&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>"2011-11-02 17:07:37 -0700")&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>NSDate</td>
		</tr>
		<tr>
			<td>Hash&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>{"age": 23, "color": "blue"}&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>NSDictionary</td>
		</tr>
		<tr>
			<td>Array&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>[123, 234] or ["mike", "joe"]&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>NSArray</td>
		</tr>
		<tr>
			<td>Geo coordinates&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>[lng, lat], e.g. [122.33, 37.48]&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>CLLocation</td>
		</tr>
		<tr>
			<td>null&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>Set a value to null&nbsp;&nbsp;&nbsp;&nbsp;</td>
			<td>NSNull</td>
		</tr>
</table>
    

For example, if you want to create a user with custom fields such as
eye_color, enrolled_at, etc., you can put all the custom_fields in a
NSDictionary.
    
    NSMutableDictionary *fieldsDict = [NSMutableDictionary dictionaryWithCapacity:4];
    [fieldsDict setObject:@"brown" forKey:@"eye_color"]; - set a string
    [fieldsDict setObject:[NSDate date] forKey:@"enrolled_at"]; - set a date
    [fieldsDict setObject:[NSNumber numberWithInt:23] forKey:@"age"]; - set a number
    [fieldsDict setObject:[NSNumber numberWithBool:true] forKey:@"student"]; - set a boolean
    [fieldsDict setObject:[NSArray arrayWithObjects:@"hiking", @"reading", nil] forKey:@"hobby"]; // set an array
    [fieldsDict setObject:[NSDictionary dictionaryWithObjectsAndKeys:@"cookies", @"favorite", nil] forKey:@"others"]; - set a hash
    
    NSMutableDictionary *paramDict = [NSMutableDictionary dictionaryWithCapacity:4];
    [paramDict setObject:@"john@usc.com" forKey:@"email"];   
    [paramDict setObject:@"John" forKey:@"first_name"];   
    [paramDict setObject:@"Woo" forKey:@"last_name"];   
    [paramDict setObject:@"pass" forKey:@"password"];   
    [paramDict setObject:@"pass" forKey:@"password_confirmation"];
    [paramDict setObject:fieldsDict forKey:@custom_fields]; // add custom fields
    CCRequest *request = [[[CCRequest alloc] initWithDelegate:self httpMethod:@"POST" baseUrl:@"users/create.json" paramDict:paramDict] autorelease];
    [request startAsynchronous];
    
The returned user object will have customFields in user.customFields  
    
    -(void)ccrequest:(CCRequest *)request didSucceed:(CCResponse *)response
    {
    	NSArray *users = [response getObjectsOfType:[CCUser class]];
    	if ([users count] == 1) {
    		NSLog(@"Successfully registered user %@", user);
    		CCUser *user = [users objectAtIndex:0];
    		NSLog(@"custom fields are %@", user.customFields);
    	}
    }
    
If you would like to use your own custom data type, you need to provide the
`-(id)JSON` encode method in your object class.   
    
    @interface MyObject : NSObject {
    	NSString *color;
    	NSNumber *mileage;
    }
    @end
    
    @implementation MyObject
    /*!
     Provide custom and/or encodable object to parse to JSON string.
     @result Object encodable as JSON such as NSDictionary, NSArray, NSString, NSNumber, NSDate or NSNull
     */
    - (id)JSON
    {
    	return [NSDictionary dictionaryWithObjectsAndKeys:self.color, @"color", self.mileage, @mileage, nil];
    }
    @end
    
    MyObject *object = [[MyObject alloc] init];
    NSMutableDictionary *customFields = [NSMutableDictionary dictionaryWithCapacity:1];
    [customFields setObject:object forKey:@"MyObject"];
    

