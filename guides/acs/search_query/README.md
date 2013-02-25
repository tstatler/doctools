## Search and Query

Appcelerator Cloud Services provides both search and query APIs for all
predefined objects. The difference is that search is predefined full text
search using Appcelerator Cloud Services search engine, query is for advanced
custom DB style search.

  * Search
  * Query
  * Availability
  * iOS

### Search

Each Appcelerator Cloud Services predefined object provides a search API. It
takes a parameter q for keywords. It will perform a case insensitive full text
search of the given keywords on a list of predefined fields. Please refer to
the individual predefined object's API document for a list of searchable
fields. For example, if you want to search places with "Seafood", it will
match all places with keyword "seafood" in place's name or tags. Search API is
prefixed, if you wish to perform your own custom search, please use query API.

### Query

Query provides an interface to apply DB query constrains on predefined fields
as well as [custom fields](/docs/customfields). When no parameters are
provided, query will simply return all objects with default pagination. The
following is a list of parameters supported.

  * page
  * per_page
  * skip and limit
  * where
  * geo query
  * order

#### page

Request page number starting from 1. Default is 1

#### per_page

Number of results per page. Default is 10

#### skip and limit

Instead of using `page` and `per_page` for pagination, you can use `limit` and
`skip` to do your own pagination, `limit` is the number of records you want to
fetch, it cannot be greater than 1000. `skip` must be used together with
`limit` to skip a number of records.

#### where

Constrains values for fields. `where` should be encoded JSON. Fields that can
be queried on are:

FieldsSummary

`Predefined Fields`

Please refer to individual Appcelerator Cloud Services Object's Query API
document

`[Custom Fields](/docs/customfields)`

Exemptions are fields with data type Array or Hash

Currently, our backend database does not support case insensitive query. If
you wish to perform case insensitive query on a field, you can save an
additional normalized copy of the original field and perform query on the
normalized field instead.

To perform an exact match on a field, e.g. search users with first_name
matching "joe"""

    
    
    where={"first_name": "joe"}
    

You could add more search criteria by adding them together, e.g. Search for
users with first_name matching "joe", favorite_color matching "blue" and age
28:

    
    
    where={"age": 28, "favorite_color": "blue", "first_name" : "joe"}
    

For non exact matches, `where` supports these options:

    
    
    
    
    
    	
    
    
    		OperatorSummary
    	
    	
    
    
    		
    $lt
    
    	    
    Less than
    
    	
    	
    
    
    		
    $lte
    
    	    
    Less than or equal to
    
    	 
    	
    
    
    		
    $gt
    
    	    
    Greater than
    
    	 
    	
    
    
    		
    $gte
    
    	    
    Greater than or equal to
    
    	 
    	
    
    
    		
    $ne
    
    	    
    Not equal to
    
    	 
    	
    
    
    		
    $in
    
    	    
    Contained in, allows you to specify an array of possible matches
    
    	 
    	
    
    
    		
    $nin
    
    	    
    Not contained in, it selects objects for which the specified field does not have any value in the specified array 
    
    	 
    	
    
    
    		
    $or
    
    	    
    Use boolean or in a query ,an array of expressions, any of which can match
    
    	 
    	
    
    
    		
    $nor
    
    	    
    A boolean or expression to do queries, you give $nor a list of expressions, none of which can match the query 
    
    	 
    	
    
    
    		
    $and
    
    	    
    Give $and an array of expressions, all of which must match the query 
    
    	 
    	
    
    
    		
    $all
    
    	    
    The $all operator is similar to $in, but instead of matching any value in the specified array all values in the array must be matched 
    
    	 
    	
    
    
    		
    $exists
    
    	    
    Check for existence of a field 
    
    	 
    	
    
    
    		
    $regex
    
    	    
    Regex match on a string, Currently, only prefix match is supported. For examples '^a', '^a.*', and '^a.*$'. This can be used to perform prefix wildcard search
    
    	
    
    
    
    #### geo query
    
    
    For query on geographic coordinates only:  
    
    
    
    
    	
    
    
    		OperatorSummary
    	
    	
    
    
    		
    $nearSphere  
    
    	    
    Search near geographic coordinates, format is [longitude, latitude]
    
    	
    	
    
    
    		
    $maxDistance
    
    	    
    used with $nearSphere to limit maximum search distance. All distances use radians. This allows you to easily multiply by the radius of the earth (about 6371 km or 3959 miles) to get the distance in your choice of units. Conversely, divide by the radius of the earth when doing queries
    
    	
    
    
    
    You can combine any of the above to build a more complex query.
    

If you want to find users with age older than 28:

    
    
    where={"age": {"$gt":28}}
    

If you want to find users at age 28 or 38:

    
    
    where = {"age": {"$in":[28,38]}}
    

If you want to find users at age neither 28 nor 38:

    
    
    where = {"age": {"$nin":[28,38]}}
    

If you want to find user at email is john@testsite.com and type is User:

    
    
    where = where={"$and": [ {"email" : "john@testsite.com"}, { "_type" : "User" } ] }
    

If you want to find users who have options are 2,3

    
    
    where={"options": {"$all" : [2,3] } }
    

If you want to find users who have location information

    
    
    where={"location": {"$exists" : true} }
    

If you want to find users who haven't location information

    
    
    where={"location": {"$exists" : false} }
    

If you have assigned custom coordinates to your user objects, you can search
by users' coordinates. For example, if you want to find users named joe near
longitude -122.1 and latitude 37.1.

    
    
    where={"first_name":"joe", "coordinates":{"$nearSphere":[-122.1, 37.1]}}
    

To find users named joe near longitude -122.1 and latitude 37.1 with maximum
distance of 5 miles (convert 5 miles to radians, 5/3959 = 0.00126)

    
    
    where={"first_name":"joe", "coordinates":{"$nearSphere":[-122.1,37.1], "$maxDistance" : 0.00126}}
    

#### order

Sort results by one or more fields. Fields that can be sorted are:

    
    
    Predefined Fields - Please refer to individual Appcelerator Cloud Services Object's Query API document
    [Custom Fields](/docs/custom_fields) - Exemptions are fields with data type Array or Hash
    

For example, if you want to query users and sort them by first_name and
created_at:

    
    
    order=first_name,created_at
    

To reverse the sorting order, simply add `-` in front of a field. For example,
to sort results by first_name in ascending order then created_at in descending
order:

    
    
    order=first_name,-created_at
    

### Availability

The following Appcelerator Cloud Services objects allow you to perform query:

  * [Chats](/docs/api/v1/chats/query)
  * [Checkins](/docs/api/v1/checkins/query)
  * [Events](/docs/api/v1/events/query)
  * [Photos](/docs/api/v1/photos/query)
  * [Places](/docs/api/v1/places/query)
  * [Posts](/docs/api/v1/posts/query)
  * [Reviews](/docs/api/v1/reviews/query)
  * [Statuses](/docs/api/v1/statuses/query)
  * [Users](/docs/api/v1/users/query)

### iOS

Appcelerator Cloud Services iOS SDK provided a CCWhere class to build where
clause in query easily. First you need to instantiate a CCWhere object:

    
    
    CCWhere *where = [[[CCWhere alloc] init] autorelease];
    

Then you can add your query constrains by calling one of the following
methods:

    
    
    -(void)fieldName:(NSString *)fieldName lessThan:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName greaterThan:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName equalTo:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName notEqualTo:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName lessThanEqualTo:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName greaterThanEqualTo:(NSObject *)value;
    -(void)fieldName:(NSString *)fieldName containedIn:(NSArray *)values;
    -(void)fieldName:(NSString *)fieldName nearLat:(double)latitude nearLng:(double)longitude;
    -(void)fieldName:(NSString *)fieldName nearLat:(double)latitude nearLng:(double)longitude maxDistanceKm:(double)distanceKm;
    -(void)fieldName:(NSString *)fieldName nearLat:(double)latitude nearLng:(double)longitude maxDistanceMi:(double)distanceMi;
    

The first parameter is the name of the field you want to query on. Then set
the where object along with other query parameters in the paramDict for
CCRequest.

    
    
    paramDict = [NSDictionary dictionaryWithObjectsAndKeys:where, @"where", @"first_name,last_name", @"order", nil];
    

Here is a sample query on User's predefined and custom fields:

    
    
    CCWhere *where = [[[CCWhere alloc] init] autorelease];
    [where fieldName:@"first_name" equalTo:@"joe"]; - first_name is User object's predefined field
    [where fieldName:@"age" greaterThanEqualTo:[NSNumber numberWithInt:23]]; 
    [where fieldName:@"enrolled_at" lessThan:[NSDate date]];
    [where fieldName:@"coordinates" nearLat:37.1 nearLng:-122.1 maxDistanceMi:5.0]; - If you have assigned a location to the user
    
    paramDict = [NSDictionary dictionaryWithObjectsAndKeys:where, @"where", @"mileage,-purchased_at", @"order", nil];
    request = [[[CCRequest alloc] initWithDelegate:self httpMethod:@"GET" baseUrl:@"users/query.json" paramDict:paramDict] autorelease];
    [request startAsynchronous];
    

