# run -- Start a Node.ACS Application Locally

## Description

Start a Node.ACS application locally for developing and testing purpose.  
The command needs to be run in application's root directory, or specify the
application's directory with **-d** option.

## Usage

`$ acs run` [ _options_ ]

**Login Required:** No

## Optional Parameters

<table class="doc-table">
    <tbody>
        <tr>
            <th>Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>-p, --port</td>
            <td>Start application with a specific port. If omitted, port '8080' will be used.  
                This option only takes effect when app is running with MVC framework.</td>
        </tr>
        <tr>
            <td>--random</td>
            <td>Start application with a random port.  
                This option only takes effect when app is running with MVC framework.</td>
        </tr>
        <tr>
            <td>-h, --help</td>
            <td>Show help information for this command.</td>
        </tr>
    </tbody>
</table>

## Example

    $ acs run --port 3000
    
          _/_/      _/_/_/    _/_/_/ 
       _/    _/  _/        _/        
      _/_/_/_/  _/          _/_/     
     _/    _/  _/              _/    
    _/    _/    _/_/_/  _/_/_/       
    
    [INFO]  No dependencies detected
    [INFO]  The app is running locally, log file is: /home/user/MyProject/logs/MyProject.log
       info  - socket.io started
    [INFO]  ACS started on port 3000
    
