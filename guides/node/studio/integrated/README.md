# Integrated Projects

An integrated project consists of both Titanium mobile client code _and_ Node.ACS server code in the
same project, or they can be developed as two separate projects.

First, create a cloud-enabled mobile project, then either create a new Node.ACS service in your mobile
project or connect your mobile application to an existing standalone Node.ACS service using a
bindings file.

## Creating A New Project

To create a mobile client project, either a classic Titanium or Alloy application:

  1. From the menu bar, select **File > New > Mobile Project** to open the **New Project** wizard.
  2. Follow the wizard directions and fill out the fields.
  3. Enable cloud services for your application:

     a. For Titanium Studio, make sure **Cloud-enable this application** is enabled.
     b. For Appcelerator Studio, make sure **Enable Appcelerator Services** is enabled.

  4. Click **Finish**.

Studio creates a mobile project with cloud services enabled.

## Creating a New Service

If you have an existing standalone Node.ACS project you want to connect to your mobile application,
skip these directions and go to the next section or import your standalone Node.ACS project into the
mobile client project under an `acs` folder.

To create a new Node.ACS service in your mobile project:

  1. Select your project in the **App Explorer** or **Project Explorer** view.
  2. Right-click on the project and select **New > Node.ACS Service**.
  3. Give the service a name.

Studio creates a new Node.ACS service, using the MVC framework, in the
`<project>/acs/<service_name>` folder, and adds the bindings file,
`Resources/ti.cloud.<project_name>.js`.

You can add additional methods to your service and publish the service using the same procedures as 
for a standalone project. See [Standalone Project](#!/guide/node_studio_standalone) for more information.

Once you have finished creating your service, you need to regenerate your bindings file if you make
changes to your `acs/<service_name>/config.json` file, as described in the next section.

## Generating a Bindings File for Your Service

To create a bindings file to connect your application to your Node.ACS service:

  1. Select your project in the **App Explorer** or **Project Explorer** view.
  2. Right-click on the project and select **Node.ACS > Import Node.ACS Bindings**
  3. Select a project from the list of available Node.ACS projects. Remote third-party services are
     not yet supported.
  4. Click **OK**.

A bindings file, called `Resources/ti.cloud.<project_name>.js`, is a CommonJS module used 
to access the Node.ACS service. The bindings file abstracts HTTP requests to access your Node.ACS
service with JavaScript API calls.

Studio also injects a base URL key for your service in to your mobile client's `tiapp.xml` file
called `acs-service-baseurl-<service_name>`.  This property key needs to be updated when you publish your
service.

If you change the `config.json` file in the Node.ACS project, you need to follow the same procedure to
update the bindings file.

**Note:** You may need to modify the bindings file to fully support your cloud service.
Currently, the bindings file does not include a callback for error handling or handles route parameters.

For Alloy projects, Alloy may process the bindings file, such as removing comments.  To avoid this,
copy the bindings file to the `app/lib` folder and edit the file there.  The file will be copied
to the `Resources` folder by Alloy during compilation.

The `Resources` folder may be hidden in the **App Explorer** and **Project Explorer** views.
If your `Resources` folder is hidden, click the **View Menu** button (white
triangle pointing down) and select **Customize View...**, then the **Available Customizations** dialog
appears. In the **Filters** tab, uncheck the **Titanium Resources Folder** checkbox, then click **OK**.

## Connecting Your Client Application to Your Node.ACS Service

In your client application, require in the bindings file and call the exported functions to access the
Node.ACS service.  For example, the code below shows a snippet of a bindings file and how to invoke
it in your mobile client project.

`Resources/ti.cloud.FooBar.js`:

    // ...bunch of generated code...
    exports.application_createFoo = function(data, cb){
        InvokeService("/foobar", "POST", data, cb);
    }

`Resources/app.js`:

    var cloud_service = require('ti.cloud.FooBar');)
    // The default generated bindings file allows you to send payload data and a success callback.
    cloud_service.application_createFoo({'foo':'foobar'}, function(r, e){
        Ti.API.info(JSON.stringify(r));
    });

In your `tiapp.xml` file, the `acs-service-baseurl-<service_name>` property tag needs to contain the URL of
where to access your service.

`tiapp.xml`:

    <property name="acs-service-baseurl-FooBar">http://localhost:12345</property>

## Running Your Project Locally

First, start your Node.ACS service.  If you are using a standalone Node.ACS project, first select the
project in the **App Explorer** or **Project Explorer** view.
Click the **Run** button and select **Local Node.ACS Server** to start your service.

If you want to run your client on a device, you need to modify your `tiapp.xml` file to use an IP
address rather than `localhost` as the base URL.  Your computer and device must be on the same network.

  1. Open your `tiapp.xml` file.
  2. Locate the `acs-service-baseurl-<service_name>` property tag.
  3. Change `localhost` to your computer's IP address.
  4. Save and close the file.

Next, start your mobile client.  Click the **Run** button and select one of the deployment options.

Your client application should be able to communicate with your service.

## Publish Your Service

Publish your Node.ACS service. If you are using a standalone Node.ACS project, select the project in
the **App Explorer** or **Project Explorer** view, then click the **Publish** button and select **Deploy
App**.  If your project is part of the mobile application project, click the **Publish** button and
select **Publish Node.ACS Service**.

When your sevice is published, a dialog appears providing you with the URL to access the service.
You can optionally set a custom domain name, using the `acs cname` command.
Before deploying your app, modify your `tiapp.xml` file to point to the published URL.
Follow the directions from the previous section except replace the entire URL with your published URL.

You can run your client project to test the service, then publish it to a mobile market place.

## Separate Server and Client Workflows 

If the project workflow uses two separate development teams--one creating the Node.ACS service and
another creating the client application, the two teams can collaborate on a project by following one
of the procedures.

*Method 1:*

The team working on the Node.ACS service:

  1. Creates and publishes the service.
  2. Creates an empty mobile client project and generates a bindings file.
  3. Gives the bindings files and published URL to the client application team.

The team working on the client application:

  1. Imports the bindings file in to the client project.
  2. Adds the `acs-service-baseurl-<service_name>` property tag with the published URL to the `tiapp.xml` file.


*Method 2:*

The team working on the Node.ACS service creates and publishes the service, then gives the Node.ACS
project and published URL to the client application team.

The team working on the client application imports the Node.ACS project in to the client project,
generates the bindings file, and updates the `acs-service-baseurl-<service_name>` property tag with the
published URL.

