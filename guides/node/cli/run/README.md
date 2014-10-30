# run -- Start a Node.ACS Application Locally

## Description

Start a Node.ACS application locally for development and testing purposes.  
The command needs to be run from the application's root directory, or you must specify the
application's directory with **-d** or **--dir** options.

## Usage

`$ acs run` [ _options_ ]

**Login Required:** No

## Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>-p</code>, <code>--port</code> <em>Port</em></td>
            <td>Start the application on a specific port. If omitted, port '8080' is used.  
                This option only takes effect for applications using the [Node.ACS MVC framework](#!/guide/node_mvc).</td>
        </tr>
        <tr>
            <td><code>--random</code></td>
            <td>Start application with a random port.  
                This option only takes effect for applications using the [Node.ACS MVC framework](#!/guide/node_mvc).</td>
        </tr>
        <tr>
            <td><code>-h,</code>, <code>--help</code></td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

The following runs the Node.ACS application in the current working directory on port 3000.

    $ acs run --port 3000
    
    [INFO]  No dependencies detected
    [INFO]  socket.io started
    [INFO]  ACS started on port 3000
    
