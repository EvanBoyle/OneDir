OneDir
======

OneDir project for CS3240

  constants.py: Contains prompt responses and Httpresponses as fields to ensure that changes are global.
  
  clientLog.json: JSON dump of local file changes.

/Server

  User management: localhost:8000/admin
  
  Get a user's list of files: GET localhost:8000/ListFiles/user
  
  Download a specific file for a user: GETlocalhost:8000/user/filename
  
  Get a token for a user:  POST localhost:8000/api-token-auth username=u password=p
  
  Upload a file: POST localhost:8000/UploadFile with token and file set
  
  UploadDemo.py:  demo of how to call the upload file api
  
  AuthTest.py: demonstrates making a ListFiles request with and without token

  resetTesting.py: working on script to call the manager to reset and populate the database

  userTests.py: demonstrates user creation and password change
  
  Summary:  Token based authentication is implemented and ready to be integrated in the client.  Endpoints are set up to list a user's files, and download a specific file for a user.
  
  TODO: 
  
    create endpoints for the following:
    
      delete files
      
      compare user's files with server's files
      
    create scripts that call the manager to reset and populate the database
    
    create scripts to set up directory for user and populate with test files
    
      
  
/Client

  Watchdog client for file monitoring, fetching, and pushing.

  main.py: User login and registration. This needs to be run through command prompt or terminal because of the way password prompts work.

  filemonitor.py: watches creation, deletion, and modification of files, and logs the file path, file size, and type of event to a JSON file.
  
  synchronization.py: Gets list of server files, compares it to client files, pulls files from server, and pushes files to server.

  watchdogTest.py: script to create, modify, delete, and move files in local directory for testing. Each change is delayed by 2 seconds for testing purposes.

  TODO:

    compare local and server files and update client accordingly
    
