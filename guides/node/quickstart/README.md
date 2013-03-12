
# Node.ACS Quickstart

Appcelerator Node.ACS enables you to develop and publish Node.js applications
to the cloud. Node.ACS includes a simple command-line-interface and an MVC
framework that makes it easy for both novice and experienced node.js
developers to create apps and services. With Node.ACS, you can:

  * Build custom services to extend the existing Appcelerator Cloud Services (ACS)
  * Host your existing node.js app/service on the Appcelerator Cloud
  * Create Node.ACS apps directly from Titanium Studio
  * Develop a Node.ACS service for your Titanium apps using the same development language (Javascript)

This quickstart will guide you through the process of creating a simple Chat
Room Node.ACS app using the built-in [MVC framework](#!/guide/mvc). It is a
simple tutorial to help you get started with Node.ACS.

If you just want to deploy an existing node.js app, see [Standard Node Applications](#!/guide/standard).

**Note:** Node.ACS is currently in Developer Preview state, so users may experience some instability.

  

## Getting Ready

1.  Node.js & npm

2.  Node.ACS CLI Install

    *   Download and install [Node.js](http://nodejs.org) (min. version 0.8.13). To check
        if you have Node installed, run the following command: 
            
            node -v

        This should return the current Node version, if Node is installed.

    *   Install npm: As of version 0.6.3, npm is installed automatically. If you still need npm go to [npm](https://github.com/isaacs/npm/).

        The Node.ACS CLI is the command-line utility for creating and administering
        Node.ACS based applications and services. To install it using **npm** run the
        following command:  
    
            $ sudo npm install -g acs

Done. It's that easy!

## First Node.ACS App   Build and publish an app in a minute

**1\. Login with appcelerator credentials**  
Run command `$ acs login` and follow the prompt to login to Node.ACS with your
appcelerator account. If you do not have an Appcelerator account, create one
[here](https://my.appcelerator.com/auth/signup).



**2\. Create a new application**  
Run command `$ acs new MyFirstApp` to create a new app using the Node.ACS MVC
framework by default.



**3\. Publish application to cloud**  
Change working directory to the "MyFirstApp" directory(the app's root
directory), and run command `$ acs publish` to publish the app to the cloud.



Congratulations! Now you've successfully published your first Node.ACS app to
the cloud!  
Open a web browser and enter the URL you get from step #3, you'll get a big
welcome from Node.ACS!

  

## The Chat Room App   Let's build something real

Let's add more features to the app to make it a public chat room. The app will
be built with [Node.ACS MVC framework](/guides/mvc) and will use built-in
websocket for establishing a connection between client(web browser) and
server, so that each post message will be "pushed" to all connecting clients.
You can just copy and paste the code snippets below in the corresponding
project files.

**Enough talking, let's start coding!**

### Controller

The controller code is invoked whenever a certain http request comes in. All
controller files should be placed in "controllers" directory in the app's
project.

  
**/controllers/application.js**
    
    
    // render 'chatroom.ejs'
    function chatroom(req, res) {
        res.render('chatroom');
    }
    

This controller will be configured(in `config.json`) to respond to the http
GET request with URL "/", and will return the chatroom web page.

### Websocket event handler

Websocket event handler is the function which will be invoked whenever a
certain websocket event is emitted by client. All websocket event handler
files should be placed in "websockets" directory in the app's project.

  
**/websockets/chatroom.js**
    
    
    // broadcast incoming message to all clients
    function receiveMessage(data, socket) {
      socket.broadcast.emit('message', data);
    }
    

This event handler will be configured(in `config.json`) to respond to a
certain event to broadcast received chat message from a client to all other
chat clients.

### config.json

`config.json` contains all configurations of route mappings, filters and
websocket event handlers.  
It is the key configuration file of the application for binding requests to
handlers(functions).

  
**/config.json**
    
    
    {
      "routes":
      [
        {"path":"/", "method":"get", "callback":"application#chatroom"}
      ],
      "websockets":
      [
        {"event": "newChatMsg", "callback": "chatroom#receiveMessage"}
      ]
    }
    

This `config.json` defines the URL "/" for GET method routes to function
`chatroom` in `application.js` file; it also defines the function
`receiveMessage` in `chatroom.js` to listen on "newChatMsg" event that emitted
by clients.

### Views

Views are where your user interface (UI) is defined. All views files reside in
"views" directory in the app project. Node.ACS uses EJS as view engine by
default.

**/views/chatroom.ejs**
    
    
    <html>
      <head>
        <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen" />
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script src="/socket.io/socket.io.js"></script>
        <script>
          //establish websocket connection with server
          var iosocket = io.connect('http://localhost:8080');
          iosocket.on('connect', function () {
          $('#incomingChatMessages').append($('<li class="alert">Connected</li>'));
          
          //when received message from server
          iosocket.on('message', function(data) {
            var icm = $('<li class="active"></li>');
            $('#incomingChatMessages').append(icm.text(data.message));
            setTimeout(function() { icm.removeClass('active') }, 1500);
            $('#chat-ctnr').scrollTop($('#incomingChatMessages').height() + 100 );
          });
          iosocket.on('disconnect', function() {
            iosocket.on('message', null);
              $('#incomingChatMessages').append('<li class="alert">Disconnected</li>');
            });
          });
    
          //send new chat message
          function sendMsg() {
            iosocket.emit('newChatMsg', {message: $('#outgoingChatMessage').val()});
            var ocm = $('<li class="active"></li>');
            $('#incomingChatMessages').append(ocm.text($('#outgoingChatMessage').val()));
            $('#chat-ctnr').scrollTop($('#incomingChatMessages').height() + 100 );
            setTimeout(function() { ocm.removeClass('active') }, 1500);
            $('#outgoingChatMessage').val('');
          }
        </script>
      </head>
      <body>
        <div id="ic">Incoming Chat:</div>
        <div id="chat-ctnr">
          <ul id="incomingChatMessages"></ul>
        </div>
        <input type="text" id="outgoingChatMessage"><input id="sendMessageButton" type="button" value="send" onclick='sendMsg()'>
      </body>
    </html>
    

### Static Files

A Node.ACS application uses the "public" directory as the static file's root,
you can put all your static files(such as stylesheets, image assets and
scripts) in that directory with any dir depth/structure you'd like.

  
**/public/style.css**
    
    
    * { font: 400 14px/24px "helvetica neue", arial, sans-serif; }
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
        padding: 0; margin: 0; list-style: none; 
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
        width: 255px;
    }
    #outgoingChatMessage:focus {
        border: 1px solid #1c94c4;
    }
    #sendMessageButton {
        margin: 5px 0 5px 5px;
        padding: 3px;
        outline: none;
        border: 1px solid #ccc;
        width: 60px;
        cursor: hand;
    }
    

**You're done! Now let's run it and publish to the cloud!**

Change the working directory to the app's directory, run command `$ acs run`
to start the server locally.  
Open a web browser and visit http://localhost:8080 to start chatting. Open a
different browser window and type a random message and hit “send”. You will
see the message showing up in the first window!

Now let's publish the app to Node.ACS cloud!  
  
First, replace the 'http://localhost:8080' in file `/views/chatroom.ejs` on
line 8 with your app's URL that returned by 'acs publish' command
previously(e.g. http://xxxx.cloudapp.appcelerator.com). This will set the chat
client connection to the server running in the cloud instead of your local
machine.  
Second, since you have already published this app before (step #3), this time
you have to use the `\--force` option to overwrite the previous deployment.  
Run the command `$ acs publish --force`, open web browser and visit the app in
the cloud with the URL the command returns.  

**That's it! You made it! Enjoy!**

