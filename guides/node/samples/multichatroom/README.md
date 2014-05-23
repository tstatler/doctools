# Multi-Chat Room Sample

This sample is an extension of the chatroom example in the
[Node.ACS Quickstart guide](#!/guide/node_quickstart). This sample demonstrates how to integrate ACS
into a Node.ACS application and use the socket.io object for web socket handling.

In this sample, users need to sign up for an account to use the application.  A list of available
chatrooms is displayed, and they can either choose to join an existing chatroom or create a new one.

This tutorial assumes you know how to create, run and publish a Node.ACS service.  These topics are
covered in the [Node.ACS Quickstart guide](#!/guide/node_quickstart).

## Application Setup 

The app will be built using the [Node.ACS MVC framework](#!/guide/node_mvc).
By default a new Node.ACS application is enabled to use the MVC framework.

You need to create an ACS application as described in the
[ACS Quickstart guide](#!/guide/acs_quickstart) to generate an API key for the Node.ACS application
to use.

You can just copy and paste the code snippets below into the corresponding
project files.


## Main File

The `start` method of the `app.js` main file sets up the application to use the ACS library and
allows the application to use the `socket.io` throughout the controllers.

Modify the code below by replacing `<API_KEY>` with your ACS application API key.

**/app.js**

    var ACS = require('acs').ACS;
    var logger = require('acs').logger;

    // initialize app (setup ACS library and logger)
    function start(app, express, io) {
        // Replace <API_KEY> with your ACS API key
        ACS.init('<API_KEY>');
        logger.setLevel('DEBUG');
        
        //use connect.session
        app.use(express.cookieParser());
        app.use(express.session({ key: 'node.acs', secret: "my secret" }));
        
        //set favicon
        app.use(express.favicon(__dirname + '/public/images/favicon.ico'));
    
        //save the socket.io io object to app so that it can be access via req.app.io
        app.io = io;
    }
    
    // release resources
    function stop() {

    }

## Configuration File

This configuration file binds requests to various handlers in the controllers and filters.
Web socket handling is performed using the socket.io instance in the `application.js` controller as
demonstrated in the `openNewRoom` function, rather than using the `websockets` event routing in this file.

**/config.json**

    {
      "routes":
      [
        { "path": "/", "callback": "application#index" },
        { "path": "/login", "method": "get", "callback": "application#login" },
        { "path": "/login", "method": "post", "callback": "session#login" },
        { "path": "/logout", "method": "get", "callback": "session#logout" },
        { "path": "/signup", "method": "get", "callback": "application#signup" },
        { "path": "/signup", "method": "post", "callback": "user#signup" },
        { "path": "/chatroom/:name", "method": "get", "callback": "application#chatroom" }
      ],
      "filters":
      [
           { "path": "/chatroom", "callback": "session_filter#checkSession" }
      ],
      "websockets":
      [
      ]
    }


## Controllers

This sample contains three controllers:

  * `application.js`: handles application flow and chatrooms
  * `session.js`: handles user sessions
  * `user.js`: handles user login and logout

The controller code is invoked whenever a corresponding HTTP request comes in. All
controller files should be placed in `controllers` directory in the app's
project.

**/controllers/application.js**

    var logger = require('acs').logger;

    // Render the home page which will either ask user to login or display a list of available
    // rooms.
    function index(req, res) {
        var rooms = getRoom(req);
        res.render('index', {user: req.session.user, rooms: rooms});
    }
    
    // Render login page
    function login(req, res) {
        res.render('login');
    }
    
    // Render signup page
    function signup(req, res) {
        res.render('signup');
    }
    
    // Get in a chat room. Will first open the room if it doesn't exist.
    function chatroom(req, res) {
        var room = req.param('name');
        var nameToSearch = room == 'default'?'':room;
        var rooms = getRoom(req);
        if(rooms.indexOf(nameToSearch) == -1)
            openNewRoom(req, room);
        res.render('chatroom', {user: req.session.user, room: room});
    }

    // Get available rooms currently
    function getRoom(req) {
        var rooms = [];
        for(room in req.app.io.rooms) {
            if(room.indexOf('/') == 0)
                room = room.substring(1);
            rooms.push(room);
        }
        return rooms;
    }

    // Start listening on a new path (room)
    function openNewRoom(req, room) {
    
        if(room == 'default') {
            logger.warn('Open default room');
            req.app.io.on('connection', handleConnection);
        } else {
            logger.warn('Open room: ' + room);
            req.app.io.of('/' + room).on('connection', handleConnection);
        }
    
        function handleConnection(socket) {
            if (!socket) {
                var msg = 'Error in socket connection.';
                logger.error(msg);
                throw msg;
            }
    
            socket.on('msg', function(data) {
                socket.broadcast.emit('message', data);
            });
        }
    }

**/controllers/session.js**

    var ACS = require('acs').ACS;
    var logger = require('acs').logger;

    //do ACS user login
    function login(req, res) {
        var un = req.body.username;
        var pw = req.body.password;
        ACS.Users.login({login: un, password: pw}, function(data) {
            if(data.success) {
                var user = data.users[0];
                if(user.first_name && user.last_name) {
                    user.name = user.first_name + ' ' + user.last_name;
                } else {
                    user.name = user.username;
                }
                req.session.user = user;
                res.redirect('/');
                logger.info('User logged in: ' + user.name);
            } else {
                res.render('login', {message: data.message});
            }
        });
    }

    function logout(req, res) {
        delete req.session.user;
        res.redirect('/');
    }

**/controllers/users.js**

    var ACS = require('acs').ACS;
    var logger = require('acs').logger;

    function signup(req, res) {
        var data = {
            first_name: req.body.first_name,
            last_name: req.body.last_name,
            email: req.body.email,
            password: req.body.password,
            password_confirmation: req.body.password_confirmation
        };
        
        ACS.Users.create(data, function(data) {
            if(data.success) {
                var user = data.users[0];
                if(user.first_name && user.last_name) {
                    user.name = user.first_name + ' ' + user.last_name;
                } else {
                    user.name = user.username;
                }
                req.session.user = user;
                res.redirect('/');
                logger.info('Created user: ' + user.name);
            } else {
                res.render('signup', {message: data.message});
            }
        });
    }

## Filters

Filters intercept requests before being evaluated by the controller.  The following filter makes
sure the user is logged in before proceeding to the view that lists all of the chatrooms.

All filter files reside in `filters` directory in the application's project directory.

**/filters/session_filter.js**

    function checkSession(req, res, next) {
        if(!req.session.user) {
            res.render('login', {message: 'Please login first.'});
            return;
        }
        next();
    }


## Views

This sample contains four views:

  * `chatroom.ejs`: presents the chatroom where the user can chat
  * `index.ejs`: presents the chatroom selection where the user creates or picks a chatroom
  * `login.ejs`: presents the application login
  * `signup.ejs`: presents the account sign-up form

All view files reside in `views` directory in the application's project directory.

**/views/chatroom.ejs**


    <html>
        <head>
            <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen" />
            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
            <!-- include socket.io client js -->
            <script src="/socket.io/socket.io.js"></script>
            <script>
            $(function(){
                //establish websocket connection with server
                var iosocket = io.connect('/<%= (room=='default'?'':room)%>');
                iosocket.on('connect', function () {
                $('#incomingChatMessages').append($('<li class="alert">Connected</li>'));

                //when received message from server
                iosocket.on('message', function(data) {
                    var icm = $('<li class="active"></li>');
                    $('#incomingChatMessages').append(icm.text(data.user + ': ' + data.message));
                    setTimeout(function() { icm.removeClass('active') }, 1500);
                    $('#chat-ctnr').scrollTop($('#incomingChatMessages').height() + 100 );
                });

                //when received message from server
                iosocket.on('message', function(data) {
                    var icm = $('<li class="active"></li>');
                    $('#incomingChatMessages').append(icm.text(data.user + ': ' + data.message));
                    setTimeout(function() { icm.removeClass('active') }, 1500);
                    $('#chat-ctnr').scrollTop($('#incomingChatMessages').height() + 100 );
                });

                iosocket.on('disconnect', function() {
                    iosocket.on('message', null);
                    $('#incomingChatMessages').append('<li class="alert">Disconnected</li>');
                });
                });

                $('#outgoingChatMessage').keypress(function(event) {
                    if(event.which == 13) {
                        event.preventDefault();
                        
                        //check for empty string.
                        if($(this).val() === "") {
                            alert("Please type in chat message"); 
                            return false;
                        }

                        //send message to chat server
                        iosocket.emit('msg', { user: '<%=user.name%>', message: $('#outgoingChatMessage').val()});
                        var ocm = $('<li class="active"></li>');
                        $('#incomingChatMessages').append(ocm.text('<%=user.name%>: ' + $('#outgoingChatMessage').val()));
                        $('#chat-ctnr').scrollTop($('#incomingChatMessages').height() + 100 );
                        setTimeout(function() { ocm.removeClass('active') }, 1500);

                        $('#outgoingChatMessage').val('');
                     }
                });
            });
            </script>
        </head>
        <body>
            <div class="alert">Welcome <%= user.name%> to room: <%= room%> </div>
            <div id="ic">Incoming Chat:</div>
            <div id="chat-ctnr">
                <ul id="incomingChatMessages"></ul>
            </div>
            <input type="text" id="outgoingChatMessage">
            <br/>
            <a href="/logout">logout</a>
        </body>
    </html>

**/views/index.ejs**

    <html>
    <head>
        <script language="JavaScript">
            function newRoom() {
                var link = document.getElementById('newRoomLink');
                var name = document.getElementById('newRoomName').value;
                var room = name?name:'default';
                link.href = "/chatroom/" + room;
            }
        </script>
    </head>
    <body>
    <% if(user) {%>
        <div>Welcome, <%= user.name %>!    <a href="/logout">logout</a></div>

        <br/><br/>
        <% if(rooms.length > 0) {%>
        <div><b>Available chat rooms:</b></div>
        <div>
            <% for(var i = 0; i < rooms.length; i++) { %>
            <%= rooms[i]? rooms[i]: 'default' %>&nbsp;&nbsp;<a href="/chatroom/<%=(rooms[i]?rooms[i]:'default')%>">Join</a><br/>
            <% } %>
        </div>
        <% } else { %>
        <div><b>No chat room available!</b></div>

        <% } %>
        <br/><br/>
        <div>
            <div><b>Open a new room: (click Go directly to open the default room listening on /)</b></div><br/>
            <div>Room name: <input type="text" id="newRoomName" name="roomname"/>&nbsp;&nbsp;<a href="" id="newRoomLink" onclick="newRoom()">Go</a></div>
        </div>

    <% } else {%>
        <%- include login %>
    <% } %>
    </body>
    </html>


**/views/login.ejs**

    <% var message; 
        if(message) { %>
        <%= message %>
    <% } %>

    <form action="/login" method="post">
    <div><input name="username" placeholder="user name" title="username" required/></div>
    <div><input name="password" placeholder="password" type="password" title="password" required/></div>
    <div><input type="submit" value="login"/></div>
    </form>
    <div><a href="/signup">signup</div>

**/views/signup.ejs**

    <% var message; 
        if(message) { %>
        <%= message %>
    <% } %>

    <form action="signup" method="post">
    <div><input name="email" placeholder="email" title="email" required/></div>
    <div><input name="first_name" placeholder="first name" title="first name" required/></div>
    <div><input name="last_name" placeholder="last name" title="last name" required/></div>
    <div><input name="password" placeholder="password" type="password" title="password" required/></div>
    <div><input name="password_confirmation" placeholder="password confirmation" type="password" title="password confirmation" required/></div>
    <div><input type="submit" value="signup"/></div>
    </form>
    <div><a href="/login">login</div>


## Static Files

A Node.ACS application uses the `public` directory as the root for static files.
You can place static files such as stylesheets, image assets and
client-side scripts in that directory. You can create any directory structure you need to
under the `public` directory.

**/public/css/style.css**

    * {
        font: 400 14px/24px "helvetica neue", arial, sans-serif;
    }
    #ic {
        width: 300px;
        padding: 5px 10px;
        border: 1px solid #ccc;
        border-bottom: 0;
    }
    #chat-ctnr {
        width: 300px;
        height: 500px;
        overflow: auto;
        padding: 10px;
        border: 1px solid #ccc;
    }
    #incomingChatMessages {
        padding: 0;
        margin: 0;
        list-style: none;
    }
    #incomingChatMessages li {
        display: block;
        height: 24px;
        border: 1px solid #ccc;
        -webkit-border-radius: 3px;
        -moz-border-radius: 3px;
        border-radius: 3px;
        background: #fff;
        margin: 2px 0;
        padding: 3px;
        transition: all .3s;
        -moz-transition: all .3s;
        -webkit-transition: all .3s;
        -o-transition: all .3s;
    }
    #incomingChatMessages li.alert {
        font-weight: bold;
    }
    #incomingChatMessages li.active {
        background: #ddffdd;
    }
    #outgoingChatMessage {
        margin: 5px 0;
        padding: 5px;
        outline: none;
        border: 1px solid #ccc;
        width: 322px;
    }
    #outgoingChatMessage:focus {
        border: 1px solid #1c94c4;
    }    

## Run or Publish the Application

After creating, copying and pasting the required files in to the application, you are ready to run or
publish the service.

To test your service, in a browser:

  1. Navigate to your service's URL.
  2. Click the **signup** link to create a new account.
  3. Fill out the form, then click **signup**.
  4. Click **Go**. You are directed to the  default chatroom.
  5. In another browser, repeat the previous steps except when you are presented with the list of
     chatrooms, click **default** to enter the same chatroom as the first browser.

Both browser will be communicating to the same chatroom.  Start typing in one browser and the
message appears in the other.
