OneDir
======

OneDir project for CS3240

/Server

  User management: localhost:8000/admin
  
  Get a user's list of files: GET localhost:8000/ListFiles/user
  
  Download a specific file for a user: GETlocalhost:8000/user/filename
  
  Get a token for a user:  POST localhost:8000/api-token-auth username=u password=p
  
  AuthTest.py: demonstrates making a ListFiles request with and without token

  resetTesting.py: demonstrates adding files with sql obtained from command "python manage.py sqlall DJServer"

  
  Summary:  Token based authentication is implemented and ready to be integrated in the client.  Endpoints are set up to list a user's files, and download a specific file for a user.
  
  TODO: 
  
    create endpoints for the following:
    
      upload a file
      
      compare user's files with server's files
      
    create scripts that call the manager to reset and populate the database
    
    create scripts to set up directory for user and populate with test files
    
      
  
/Client

  Watchdog client for file monitoring, fetching, and pushing.

  watchdog.py: watches and outputs creation, deletion, and modification of files

  watchdogTest.py: script to create, modify, delete, and move files in local directory for testing

  TODO:

    store values (such as path and type of change) in data structure

    integrate token based authentication
