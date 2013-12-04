# Debugging Node.ACS Services

Studio can be used to debug Node.ACS projects similarly to mobile applications.  Set breakpoints in
your code, before starting or during a debug session, to have the debugger suspend your program
at that point.  Start a debug session and make HTTP requests to your service using a web browser,
`curl` or another utility.  When the debugger suspends execution of your code, you can inspect variables
and step through functions.  Once, you are done debugging, terminate your debug session.

For complete Studio debugger directions, review the 
[Debugging in Studio guide](http://docs.appcelerator.com/titanium/latest/#!/guide/Debugging_in_Studio).

## Starting a Debug Session

To start a debug session:

  1. Select your project in the **Project Explorer** view.
  2. Select **Debug** from the **Launch Modes** drop-down list.
  3. Make sure **Local Node.ACS Server** is selected in the **Target** drop-down list.
  4. Click the **Launch** button.

When prompted to switch to the **Debug** perspective, click **Yes**.

Studio first creates a temporary project called `Local Node.ACS Server - <project-name>`,
then it launches your service in debug mode.

## Terminating a Debug Session

When you are finished debugging, you can terminate the debug session by clicking the **Terminate** button
in the **Debug** view.

After your debug session, Studio removes the temporary project, `Local Node.ACS Server - <project-name>`.
If for some reason, you see a project with this name in your
**Project Explorer** view after you completed a debug session, you can safely delete this project.
If the temporary project is not removed, subsequent debug sessions may not start.

## Using Manual Breakpoints

You can use breakpoints in your Node.ACS JavaScript code the same way as with a mobile application.
In your JavsScript files, double-click to the left of the line number or right-click in the left
margin and select **Toggle Breakpoint...** to set a breakpoint to stop the execution of your code at
that point.

## Using JavaScript Exception Breakpoints

In the menu bar, under the **Run** menu, there is an option called **Add Node.ACS JavaScript Exception
Breakpoint**, which can be used to add a JavaScript exception breakpoint. Make sure you select the
option that contains **Node.ACS**.

Do not use the regular **Add JavaScript Exception Breakpoint** option.  This option only works for
mobile applications.

By default, the Node.ACS JavaScript exception breakpoint only handles uncaught exceptions.  To
handle caught exceptions, in the **Breakpoints** view:

  1. Right-click the **JS Exception** item and select **Breakpoint Properties...**. A dialog appears.
  2. Enable **Caught Exception**, then click **OK**.

**Note:** Enabling caught exception may cause some flickering in the **Debug** perspective upon
initialization.

## Inspecting Variables

When program execution is suspended by the debugger, you can inspect variables in your program
with the **Variables** view, which displays the current stack frame variables and their values.

## Stepping Through Code

When program execution is suspended by the debugger, you can step through code your code to examine
its execution step by step.  In the **Debug** view, use the **Step Into**, **Step Over** and **Step
Return** buttons to navigate through your code while it is suspended.  Click the **Resume** button
to resume execution normally once you are done examing your code.
