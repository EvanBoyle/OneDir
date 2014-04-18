__author__ = 'ta3fh', 'csh7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.Server.settings")
import requests
import sys
sys.path.append("..")
import constants
import json
# from Server.DJServer.views import *

token = ''
username = ''

def initialize(t, un):  #Initialized in main.py to authenticate checking the server for files
    global token
    global username
    token = t
    username = un

def list_files():
    header = {}
    header['Authorization']= 'Token '+ token
    header['content-type']='application/json'
    response = requests.get(constants.server_url + '/ListFiles/' + username, headers=header)
    return response.content

def upload_file(path, file): #Haven't decided what parameters to pass
    header = {}
    header['Authorization']= 'Token '+ token
    payload = {}
    payload['path']= path
    files = {'file': open(file, 'rb')}
    response = requests.post(constants.server_url + '/UploadFile/', headers=header, files=files, data=payload)
    print response.content

def check_server():
    server_files = list_files()
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "clientLog.json"))
    client_files = open(filepath, "r")
    # For each server file, whatever the client doesn't have the client should pull from the server
    # For each client file, whatever the server doesn't have the client should push to the server
    for line in server_files:
        if line[2] == "created":
            pass
        if line[2] == "deleted":
            pass
        if line[2] == "modified":
            pass

if __name__ == '__main__':
    pass