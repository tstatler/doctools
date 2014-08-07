# Query and Search APIs 

Appcelerator Cloud Services provides APIs for querying and searching ACS objects. 
The query APIs allow you to perform custom database-style searches, while search APIs perform a full text search using the ACS search engine.

## Query API Overview

The query API provides an interface for applying database-style query constraints on predefined objects 
and [custom fields](#!/guide/customfields). You can control pagination of queries, using either `page`
and `per_page` query parameters, or `skip` and `limit` for custom pagination. You can also control
the sort order of query results, and specify the fields you want to include (or exclude) from results.

When no query parameters are provided, all objects of the specified type are returned with default pagination. 

### Query API Availability

The following ACS object provide query methods: {@link ACLs#query ACLs}, {@link Chats#query Chats}, 
{@link Checkins#query Checkins}, {@link CustomObjects#query CustomObjects}, {@link Events#query Events}, 
{@link Files#query Files}, {@link GeoFences#query GeoFences}, 
{@link KeyValues#query KeyValues}, {@link Likes#query Likes}, {@link Logs}, 
{@link Messages#query Messages}, {@link Photos#query Photos}, {@link Places#query Places}, 
{@link Posts#query Posts}, {@link PushNotifications#query PushNotifications},
{@link PushSchedules#query PushSchedules}, {@link Reviews#query Reviews}, {@link Statuses#query Statuses},
 and {@link Users#query Users}.

### Query parameters

The following parameters are available for query operations:

  * `page`
  * `per_page`
  * `limit` and `skip`
  * `where`
  * `order`
  * `sel`
  * `unsel`

#### page

Request page number starting from 1. Default is 1. 

You can't use `skip` and `limit` together with `page` and `per_page` in the same query.

#### per_page

Number of results per page. Default is 10.

You can't use `skip` and `limit` together with `page` and `per_page` in the same query.

#### limit and skip

Instead of using `page` and `per_page` you can use `limit` and `skip` to do your own pagination. 

* `limit` -- The number of records to fetch. The value must be greater than 0, and no greater then 
1000, or an HTTP 400 (Bad Request) error will be returned.
* `skip` -- The number of records to skip. This parameter must be used together with `limit`. The value
must **not** be less than 0 or an HTTP 400 error will be returned.

You can't use `skip` and `limit` together with `page` and `per_page` in the same query.

#### where

Constrains values for fields. The value should be encoded JSON. Each value in the search query needs
to be less that 1024 bytes.  If the value is larger than 1024 bytes, the query does not return any
results.

Each type of ACS object has a set of predefined fields that can be queried with the `where` operator. 
See each object's individual `query` method for details. 

In addition, you can query the [custom fields](#!/guide/customfields) on any object. Note, however, 
that you can only query simple values, such as Strings, Dates, Numbers, or Booleans. 
If a custom field takes an array or object as a value, you can't query any of the values stored inside the array or object.  

For more information, see [Supported Data Types](#!/guide/customfields-section-supported-data-types).

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

For querying geographic coordinates, the following operators are supported:

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
    
#### order

Sort results by one or more fields. In general, you can sort based on any predefined field that you can query using
the `where` operator, as well as on custom fields. Any exceptions to this rule are noted in API reference for the 
individual `query` methods.

To reverse the sorting order, simply add `-` in front of a field. For example,
to sort results by first_name in ascending order then created_at in descending
order:
    
    order=first_name,-created_at

#### sel

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

#### unsel

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

## Search API Overview

Several ACS objects provides a search API that performs a case-insensitive, full-text
search of the given keywords on a list of predefined fields. Please refer to individual object's API
documentation for a list of searchable fields. For instance, the {@link Places#search} method will search 
within {@link Places#name} and {@link Places#tags}.

The Search API is fixed in terms of the searchable fields; use the [query](#!/guide/search_query-section-query-api-overview) 
API to perform more flexible searches.

### Search API Parameters

The following parameters are available for search operations:

  * `page`
  * `per_page`
  * `q`

#### page

Request page number starting from 1. Default is 1. 

#### per_page

Number of results per page. Default is 10.

#### q

The keyword or phrase to search for.

### Search API Availability

Search methods are available for the following pre-built ACS objects, as well as for custom fields.

* {@link Events#search Events}
* {@link Friends#search Friends}
* {@link PhotoCollections#search PhotoCollections}
* {@link Photos#search Photos}
* {@link Places#search Places}
* {@link Users#search Users}