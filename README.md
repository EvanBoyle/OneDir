OneDir
======

OneDir project for CS3240

/Server

  User management: localhost:8000/admin
  
  Get a user's list of files: GET localhost:8000/ListFiles/user
  
  Download a specific file for a user: GETlocalhost:8000/user/filename
  
  Get a token for a user:  POST localhost:8000/api-token-auth username=u password=p
  
  AuthTest.py: demonstrates making a ListFiles request with and without tolken
  
  
  Summary:  Token based authentication is implemented and ready to be integrated in the client.  Endpoints are set up to list a users files, and download a specific file for a user.
  
  TODO: 
  
    create endpoints for the following:
    
      upload a file
      
      compare users files with servers files
      
    create scripts that call the manager to reset and populate the database
    
    create scripts to set up directory for user and populate with test files
    
      
  
/Client
  Watchdog client for file monitoring, fetching, and pushing.
  Example will come shortly
