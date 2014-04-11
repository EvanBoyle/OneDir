__author__ = 'ta3fh', 'csh7kd'

import requests
import json
from Server.DJServer.views import *

token = ''
username = ''

def initialize(t, un):
    global token
    global username
    token = t
    username = un

def list_files():
    header = {}
    header['Authorization']= 'Token '+ token
    header['content-type']='application/json'
    response = requests.get('http://127.0.0.1:8000/ListFiles/' + username, headers=header)
    return response.content

def check_server():
    server_files = list_files()
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "clientLog.json"))
    client_files = open(filepath, "r")
    # For each server file, whatever the client doesn't have the client should pull from the server
    # For each client file, whatever the server doesn't have the client should push to the server
    for line in server_files:
        if line[2] == "created":
            UploadFile(line)
            #I know I need to change the line to a request and then send that to UploadFile, but I'm not sure how
        if line[2] == "deleted":
            #Here is where the code for deleting a file will go
            pass
        if line[2] == "modified":
            #Here is where the code for deleting a file will go
            UploadFile(line)

if __name__ == '__main__':
    pass