
# Node.ACS Quickstart

Appcelerator Node.ACS enables you to develop and publish Node.js applications
to the cloud. Node.ACS includes a simple command-line interface and an MVC
framework that makes it easy for both novice and experienced Node.js
developers to create apps and services. With Node.ACS, you can:

  * Build custom services to extend the existing Appcelerator Cloud Services (ACS)
  * Host your existing Node.js application or service in the Appcelerator Cloud
  * Create Node.ACS apps directly from Titanium Studio
  * Develop a Node.ACS service for your Titanium apps using the same development language (JavaScript)

This quickstart will guide you through the process of creating a simple Chat
Room Node.ACS app using the built-in [MVC framework](#!/guide/node_mvc). It is a
simple tutorial to help you get started with Node.ACS.

If you just want to deploy an existing Node.js app, see [Standard Node Applications](#!/guide/node_standard).


## Getting Ready

To use Node.ACS, you'll need to install Node.js and the Node.ACS command-line interface,
**acs**. If you are using Studio, it should guide you through the process of installing
these components.

If you are not using Studio, or want to install the components manually, follow these
steps to install Node and **acs**:

1.  Download and install Node and npm.  To check if you have Node installed, run the following command: 

        node -v

    This should return the current Node version, if Node is installed. The Node.ACS CLI requires
    Node version 0.8.13 or later.

    If you need to install Node, follow the instructions on the [Node.js web site](http://nodejs.org).

    As of Node version 0.6.3, npm is installed automatically. Should you need to install
    it, get it from the [npm github repo](https://github.com/isaacs/npm/).

2.  Use **npm** to install the **acs** command:

        sudo npm install -g acs

    The Node.ACS CLI is the command-line utility for creating and administering
    Node.ACS based applications and services. 
        
Done. It's that easy!

## Create Your First Node.ACS App   

### Using Studio

**1\. Start Studio and create a new application**

From the menubar, select **File > New > Node.ACS Project**. The **New Node.ACS Project**
wizard appears.  Enter `MyFirstApp` as the name for your project, then click **Finish**.

This creates a new application in the `MyFirstApp` folder. By default, the new application
is configured to use the Node.ACS MVC framework.

**2\. Publish your application to the cloud**

In the **App Explorer** or **Project Explorer** view, make sure your application is selected, then
click the **Publish** button and select **Deploy App**.  Once your application is deployed to the cloud,
a dialog appears with the URL to access your Node.ACS application.

Click the **Publish** button again and select **View Node.ACS Service** to open your application in
your default web browser.

### Using the CLI

**1\. Login with Appcelerator credentials**  

To work with Node.ACS applications, you must authenticate yourself with the ACS cloud. Run
the following command:

    acs login

Follow the prompts to login to Node.ACS with your
Appcelerator account. If you do not have an Appcelerator account, you can 
[sign up for a free account](https://my.appcelerator.com/auth/signup).

**2\. Create a new application**  

To create an application: 

    acs new MyFirstApp
    
This creates a new application in the MyFirstApp folder. By default, the new application
is configured to use the Node.ACS MVC framework.

**3\. Publish your application to the cloud**  

Change working directory to the `MyFirstApp` directory (the app's root
directory), and run the **acs publish** command to publish the app to the cloud:

    cd MyFirstApp
    acs publish

Congratulations! Now you've successfully published your first Node.ACS app to
the cloud!  

Open a web browser and enter the URL you get from step #3. You'll get a big
welcome from Node.ACS!


## The Chat Room App 

Let's add more features to the app to make it a public chat room. The app will
be built using the [Node.ACS MVC framework](#!/guide/node_mvc) and use the built-in
websocket server for establishing a connection between the client (web browser) and
server, so that each post message can be pushed to all connected clients.

You can just copy and paste the code snippets below into the corresponding
project files.

**Enough talking, let's start coding!**

### Controller

The controller code is invoked whenever a corresponding HTTP request comes in. All
controller files should be placed in `controllers` directory in the app's
project.
  
**/controllers/application.js**
    
    // render 'chatroom.ejs'
    function chatroom(req, res) {
        res.render('chatroom');
    }
    

This controller will be configured (in `config.json`) to respond to an HTTP
GET request with URL "/", and will return the chatroom web page.

### Websocket event handler

The websocket event handler is invoked whenever matching websocket events are received
from a client.  All websocket event handler files should be placed in the `websockets`
directory inside the application directory.

  
**/websockets/chatroom.js**
    
    
    // broadcast incoming message to all clients
    function receiveMessage(data, socket) {
      socket.broadcast.emit('message', data);
    }
    
This event handler will be configured (in `config.json`) to respond to a
certain event to broadcast a received chat message from a client to all other
chat clients.

### config.json

`config.json` contains configuration sections for route mappings, filters and
websocket event handlers. This configuration file binds requests to
handlers (functions).

  
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
    

In this case, `config.json` defines a route for the GET method on path "/", and binds
this route to the function `chatroom` in `application.js`; it also defines the function
`receiveMessage` in `chatroom.js` to be invoked whenever a `newChatMsg` event is received
from a client.

### Views

Views are where your user interface (UI) is defined. All views files reside in
`views` directory in the application's project directory. Node.ACS uses EJS as view engine by
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

A Node.ACS application uses the `public` directory as the root for static files.
You can place static files such as stylesheets, image assets and
client-side scripts in that directory. You can create any directory structure you need to
under the `public` directory.

  
**/public/css/style.css**
    
    
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
    

**You're done! Now let's run it!**


#### Using Studio

  1. Select your project in the **Project Explorer** view.
  2. Select **Run** from the **Launch Modes** drop-down list.
  3. Make sure **Local Node.ACS Server** is selected in the **Target** drop-down list.
  4. Click the **Launch** button.
  5. Once the service starts, the local port number assigned to the service is displayed
     in the **Console** view. Use the port number to acces your service.

Open a web browser and visit http://localhost:<port_number> to start chatting.

#### Using the CLI

Change to the the working directory to the app's directory and use the **acs run** command
to start the server locally:

    acs run

Open a web browser and visit http://localhost:8080 to start chatting. Open a
different browser window and type a random message and click **send**. You will
see the message show up in the first window!

**Now let's publish the app to Node.ACS cloud!**
  
First, replace the 'http://localhost:8080' in file `/views/chatroom.ejs` on
line 8 with your app's URL as returned by 'acs publish' command
(for example, <code>http://<i>&ltApp_ID&gt;</i>.cloudapp.appcelerator.com</code>). This will set the chat
client connection to the server running in the cloud instead of your local
machine.  

Second, since you have already published this app before (step #3), 
you need to republish your application.


#### Using Studio

In the **Project Explorer** view, right-click on the project and choose **Publish** > **Deploy App**.
A dialog appears informing you that the application already exists. Click the **Overwrite** button
to replace the existing version.

Once your application is deployed to the cloud, a dialog appears with the URL to access your
Node.ACS application.

#### Using the CLI

Use the `--force` option with the `publish` command to overwrite the previous deployment:

    acs publish --force

Once again, the **acs publish** command returns the URL for your application.
Open a web browser and enter the application's URL to visit the app in the cloud.

**That's it! You made it! Enjoy!**

