
# Using MongoHQ in Node.ACS App

For the application that needs to use MongoHQ as backend data store, it might
do so in Node.ACS without any problem. Here are some sample code snippets
illustrate how to use the `mongodb` Node module to access MongoHQ service in a
Node.ACS application.

## Setup Module Dependency

Before using the MongoDB module, we need to add it as a dependency in the
application's `package.json` file.
    
    "dependencies": {
        "mongodb": ">=1.1.6"
    }
    

## Open a Database Connection

    
    
    var mongodb = require("mongodb"),
        mongoserver = new mongodb.Server(host, port, server_options),
        db_connector = new mongodb.Db('database name', mongoserver, db_options);
    
    db_connector.open(function(err, myDB) {
        if (!err) {
            // work with database
        } else {
            // handle error
        }
    });
    

## Insert a Record

    
    
    myDB.collection('collection name', function(err, collection) {
        if (err) {
            callback(err);
            return;
        }
    
        collection.insert(insertingJSON, {
            safe : true
        }, function(err, result) {
            if (err) {
                callback(err);
            }
            if (result) {
                callback(null, true);
            } else {
                callback(null, false);
            }
        });
    });
    

## Query a Record

    
    
    myDB.collection('collection name', function(err, collection) {
        if (err) {
            callback(err);
            return;
        }
        var cursor = collection.find({
            'tokens' : {
                '$in' : deviceTokens
            }
        });
        cursor.each(function(err, doc) {
            if (err) {
                callback(err);
                return;
            }
            if (doc) {
                var deviceToken = doc.device_token;
                var pushDeviceTokenId = doc._id;
                var pushHostAlias = doc.push_host_alias;
                var pushHostExpiration = doc.push_host_expiration;
                callback(null, true, {
                    id : pushDeviceTokenId,
                    push_host_alias : pushHostAlias,
                    push_host_expiration : pushHostExpiration
                });
            } else {
                callback(null, false);
            }
        });
    });
    

