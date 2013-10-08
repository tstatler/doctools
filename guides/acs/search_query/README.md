# Search and Query

Appcelerator Cloud Services provides both search and query APIs for all
predefined objects. The difference is that search is predefined full text
search using Appcelerator Cloud Services search engine, query is for advanced
custom DB style search.

## Email Field

For security, when retrieiving results for users, the email field is not returned in the User
object unless you have admin access.

## Search Overview

Each Appcelerator Cloud Services predefined object provides a search API. It
takes a parameter q for keywords. It will perform a case insensitive full text
search of the given keywords on a list of predefined fields. Please refer to
the individual predefined object's API document for a list of searchable
fields. For example, if you want to search places with "Seafood", it will
match all places with keyword "seafood" in place's name or tags. Search API is
prefixed, if you wish to perform your own custom search, please use query API.

## Query Overview

Query provides an interface to apply DB query constrains on predefined fields
as well as [custom fields](#!/guide/customfields). When no parameters are
provided, query will simply return all objects with default pagination. The
following is a list of parameters supported:

  * page
  * per_page
  * skip and limit
  * where
  * geo query
  * order
  * sel
  * unsel

### page

Request page number starting from 1. Default is 1

### per_page

Number of results per page. Default is 10

### skip and limit

Instead of using `page` and `per_page` for pagination, you can use `limit` and
`skip` to do your own pagination, `limit` is the number of records you want to
fetch, it cannot be greater than 1000. `skip` must be used together with
`limit` to skip a number of records.

### where

Constrains values for fields. `where` should be encoded JSON. Each value in the search query needs
to be less that 1024 bytes.  If the value is larger than 1024 bytes, the query does not return any
results.

For each type of object,
there is a set of predefined fields that can be queried using the `where` operator. (See the 
individual `query` methods for details.) 

In addition, you can query the custom fields on any object. Note, however, that you can only query
simple values, such as Strings, Dates, Numbers, or Booleans. If a custom field takes an array or object as a
value, you can't query any of the values stored inside the array or object.  For more information,
see the "Data Types" section in the [Custom Object and Data Fields guide](#!/guide/customfields).

Currently, ACS does not support case insensitive query. To perform case insensitive query 
on a field, save an additional normalized copy of the original field and perform the query on the
normalized field instead.

To perform an exact match on a field, for example, to  search for users with `first_name`
matching "joe", use:
    
    where={"first_name": "joe"}

You can add more search criteria by adding them together. For example, to search for
users with `first_name` matching "joe", `favorite_color` matching "blue" and `age` of
28, use the following query:

    where={"age": 28, "favorite_color": "blue", "first_name" : "joe"}
    
For non-exact matches, `where` supports these options:
    
<table class="doc-table">
    <tr>
        <th>Operator</th><th>Summary</th>
    </tr>
    <tr>
        <td><code>$lt</code></td>
        <td>Less than</td>
    </tr>
    <tr>
        <td><code>$lte</code></td>
        <td>Less than or equal to</td>
     </tr>
    <tr>
        <td><code>$gt</code></td>
        <td>Greater than</td>
     </tr>
    <tr>
        <td><code>$gte</code></td>
        <td>Greater than or equal to</td>
     </tr>
    <tr>
        <td><code>$ne</code></td>
        <td>Not equal to</td>
     </tr>
    <tr>
        <td><code>$in</code></td>
        <td>Contained in, allows you to specify an array of possible matches</td>
     </tr>
    <tr>
        <td><code>$nin</code></td>
        <td>Not contained in, it selects objects for which the specified field does not have any value in the specified array </td>
     </tr>
    <tr>
        <td><code>$or</code></td>
        <td>Use boolean or in a query ,an array of expressions, any of which can match</td>
     </tr>
    <tr>
        <td><code>$nor</code></td>
        <td>A boolean or expression to do queries, you give $nor a list of expressions, none of which can match the query </td>
     </tr>
    <tr>
        <td><code>$and</code></td>
        <td>Give $and an array of expressions, all of which must match the query </td>
     </tr>
    <tr>
        <td><code>$all</code></td>
        <td>The $all operator is similar to $in, but instead of matching any value in the specified array all values in the array must be matched </td>
     </tr>
    <tr>
        <td><code>$exists</code></td>
        <td>Check for existence of a field </td>
     </tr>
    <tr>
        <td><code>$regex</code></td>
        <td>Regex match on a string. Currently, only prefix matches are supported: the
        regular expression must begin with an anchor (^) followed by a letter or digit. For
        example, '^a', '^a.*', and '^a.*$' are allowed, but not '^.*a*'.</td>
    </tr>
</table>

For quering geographic coordinates, the following operators are supported:

<table class="doc-table">
    <tr>
        <th>Operator</th><th>Summary</th>
    </tr>
    <tr>
        <td><code>$nearSphere&nbsp&nbsp</code></td>
        <td>Search near geographic coordinates, format is <code>[longitude, latitude]</code></td>
    </tr>
    <tr>
        <td><code>$maxDistance</code></td>
        <td>used with $nearSphere to limit maximum search distance. All distances use radians. This allows you to easily multiply by the radius of the earth (about 6371 km or 3959 miles) to get the distance in your choice of units. Conversely, divide by the radius of the earth when doing queries</td>
    </tr>
</table>
    
You can combine any of the above to build a more complex query.
    
If you want to find users with age older than 28:

    where={"age": {"$gt":28}}

If you want to find users at age 28 or 38:
    
    where = {"age": {"$in":[28,38]}}
    
If you want to find users at age neither 28 nor 38:

    where = {"age": {"$nin":[28,38]}}
    
If you want to find a user whose email is "john@example.com" and type is User:

    where = where={"$and": [ {"email" : "john@example.com"}, { "_type" : "User" } ] }
    
If you want to find users who have options are 2,3
    
    where={"options": {"$all" : [2,3] } }
    
If you want to find users who have location information.
    
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
    
### order

Sort results by one or more fields. In general, you can sort based on any predefined field that you can query using
the `where` operator, as well as on custom fields. Any exceptions to this rule are noted in API reference for the 
individual `query` methods.

To reverse the sorting order, simply add `-` in front of a field. For example,
to sort results by first_name in ascending order then created_at in descending
order:
    
    order=first_name,-created_at

### sel

Selects which fields to return from the query. Do not use this parameter if you are using the
`unsel` parameter.

Assign an array of field names to filter to the `all` field to search all JSON fields including
fields in nested objects.  Currently, this is the only supported option.

If you want to display a field from the `custom_field` object, simply pass the field name of the
`custom_field` object.

If you want to display a field from a nested object, then both the name of the nested object and
field need to be specified.

For example, if you want to only return the `first_name` field:

    sel={"all":["first_name"]}

### unsel

Selects which fields to not return from the query. Do not use this parameter if you are using the
`sel` parameter.

Assign an array of field names to filter to the `all` field to search all JSON fields including
fields in nested objects.  Currently, this is the only supported option.

If you want to hide displaying a field from the `custom_field` object, simply pass the field name of the
`custom_field` object.

If you want to hide displaying a field from a nested object, then both the name of the nested object and
field need to be specified.

For example, if you want to return all fields except `first_name`:

    unsel={"all":["first_name"]}

## Availability

The following Appcelerator Cloud Services objects allow you to perform query:

  * {@link Chats}
  * {@link Checkins}
  * {@link Events}
  * {@link Photos}
  * {@link Places}
  * {@link Posts}
  * {@link Reviews}
  * {@link Statuses}
  * {@link Users}

## Queries Using the iOS SDK

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
    

