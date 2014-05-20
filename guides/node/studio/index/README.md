# Creating Node.ACS projects in Studio

You can use Appcelerator or Titanium Studio to create, run, manage and debug Node.ACS services.
The `acs` command-line utility needs to be installed to manage Node.ACS projects with Studio.

If you are an [Appcelerator Platform](http://www.appcelerator.com/platform) subscriber, each Node.ACS 
application is bound to a Appcelerator Platform [organization](/platform/latest/#!/guide/Managing_Organizations). 
You can view analytics, metrics and other data about your service in [Appcelerator Dashboard](https://dashboard.appcelerator.com).

## Managing Node.ACS Projects

There are two kinds of custom cloud projects you can manage with Studio:

* **Standalone projects** only contain code for your Node.ACS service. See [Standalone Projects](#!/guide/node_studio_standalone).
* **Integrated projects** contains both a Node.ACS service and mobile client application. See 
[Integrated Projects](#!/guide/node_studio_integrated).

You can also debug Node.ACS projects in Studio, similarly to how you debug Titanium applications. You can set breakpoints in
your code, start a debug session and make HTTP requests to your service using a web browser,
`curl` or other utility. See [Debugging Node.ACS Services](#!/guide/node_studio_debugging).

## Installing or Updating Node.ACS

By default, Studio prompts you to install or update Node.ACS if it needs updating each time
Studio starts. To manually check for an update, from the menu bar, select **Help** > **Check for Appcelerator
Updates** or **Check for Titanium Updates**.
