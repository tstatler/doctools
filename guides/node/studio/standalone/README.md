# Standalone Projects

A standalone project consists of just the Node.ACS code. In Studio, you can create a new project,
code your service, then test your service locally.  Once you are done testing your service,
you can publish it to the cloud, where it can be accessed by multiple mobile clients.

## Creating a New Service

  1. In the menu bar, select **File > New > Node.ACS Project**.
  2. Give the project a name. You can have a period ('.') in the middle of the name,
     just not at the beginning or end.
  3. Click **Finish**.

Studio creates a new Node.ACS MVC project.

## Adding Additional Methods to Your Service

  1. Select your project in the **App Explorer** or **Project Explorer** view.
  2. Right-click on the project and choose **New > Node.ACS Method**.
  3. Give the method a name.
  4. Click **OK**.

Studio creates the method and adds it to the `services.js` file.

## Publishing Your Service

  1. Select your project in the **App Explorer** or **Project Explorer** view.
  2. Click on the **Publish** button, then select **Deploy App**.
  3. Once your application is deployed, a dialog appears providing you information about the
     endpoint URL for the application.

By default, the service URL will be `http://<app_id>.cloudapp.appcelerator.com` or
`http://<app_id>.cloudapp-enterprise.appcelerator.com`, where <app_id> is the
generated ID for your application. It may take a few minutes for the application to be available.

To retrieve the service URL later, select **Publish > View Node.ACS Service**, which opens the
service in your default web browser.

## Unpublishing Your Service

To unpublish a specific version of the application, make sure your project is selected in the **App
Explorer** or **Project Explorer** view, then select **Publish > Unpublish Node.ACS Service**.

## Testing Your Service Locally

  1. Select your project in the **App Explorer** or **Project Explorer** view.
  2. Click on the **Run** button and choose **Local Node.ACS Server**.
  3. Once the service starts, the local port number assigned to the service is displayed 
     in the **Console** view. 
  4. Use your computer's IP address or http://localhost, with the port number to
     access the running service with a browser or console command, such as `curl` or `wget`.

To manage and stop the server, from the menu bar, select **Windows > Show Views > Other**, to open
the **Show View** dialog.  Select **Studio > Servers** to open the **Servers** view.

