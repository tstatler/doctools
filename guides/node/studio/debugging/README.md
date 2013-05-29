# Debugging Node.ACS Services

Studio can be used to debug Node.ACS projects similarly to mobile applications.  First, set breakpoints in
your code to have the debugger suspend your program at that point.  Next, start a debug session and
make HTTP requests to your service using `curl` or another utility.  When the debugger suspends
execution of your code, you can inspect variables and step through functions.  Once, you are done
debugging, you need to terminate your service.

For complete Studio debugger directions, review the 
[Debugging in Studio guide](http://docs.appcelerator.com/titanium/latest/#!/guide/Debugging_in_Studio).

## Starting a Debug Session

To start a debug session, in the **App Explorer** or **Project Explorer** view, select your project,
then click on the **Debug** button and select **Local Node.ACS Server**.
When prompted to switch to the **Debug** perspective, click **Yes**.

Studio first creates a temporary project called `Local Node.ACS Server - <project-name>`,
which acts as a debug server to connect your projects to, then it launches your Node.ACS service in
debug mode.

## Terminating a Debug Session

When you are finished debugging, you need to terminate the service.  In the **Console View**,
click the **Terminate** button, or in the **Server** view, select your service and click the
**Stop Server** button. If you do not terminate the service, subsequent debug
sessions may not start.

If you receive the following error when running your service again, your previous service was not terminated:

    [WARN]  error raised: Error: listen EADDRINUSE

After your debug session, Studio removes the temporary project, `Local Node.ACS Server - <project-name>`.
If for some reason, you see a project with this name in your **App Explorer** or
**Project Explorer** view after you completed a debug session, you can safely delete this project.
If the temporary project is not removed, subsequent debug sessions may not start.

## Using Manual Breakpoints

You can use breakpoints in your Node.ACS JavaScript code the same way as with a mobile application.
In your JavsScript files, double-click to the left of the line number or right-click in the left
margin and select **Toggle Breakpoint...** to set a breakpoint to stop the execution of your code at
that point.

## Using JavaScript Exception Breakpoints

Currently, using JavaScript exception breakpoints in Node.ACS code is broken.

In the menu bar, under the **Run** menu, there is an option called **Add Node.ACS JavaScript Exception
Breakpoint**, which can be used to add a JavaScript exception breakpoint. Make sure you select the
option that contains **Node.ACS**.

Do not use the regular **Add JavaScript Exception Breakpoint** option.  This option only works for
mobile applications.

## Inspecting Variables

When program execution is suspended by the debugger, you can inspect variables in your program
with the **Variables** view, which displays the current stack frame variables and their values.

## Stepping Through Code

When program execution is suspended by the debugger, you can step through code your code to examine
its execution step by step.  In the **Debug** view, use the **Step Into**, **Step Over** and **Step
Return** buttons to navigate through your code while it is suspended.  Click the **Resume** button
to resume execution normally once you are done examing your code.
