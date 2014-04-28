__author__ = 'ta3fh', 'csh7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.Server.settings")
import requests
import sys
sys.path.append("..")
import constants
import json
# from Server.DJServer.views import *


class Synchronization:

    def __init__(self, t, un, s):  # Initialized in main.py to authenticate checking the server for files
        self.token = t
        self.username = un
        self.sync = s

    def list_files(self):
        header = {}
        header['Authorization']= 'Token '+ self.token
        header['content-type']='application/json'
        response = requests.get(constants.server_url + '/ListFiles/' + self.username, headers=header)
        return response.content

    def upload_file(self, full_path):
        header = {
            'Authorization': 'Token ' + self.token
        }
        path = {
            'path': full_path[:full_path.rfind('/') + 1]
        }
        files = {
            'file': open('../Server/Files/' + full_path, 'rb')
        }
        response = requests.post(constants.server_url + '/UploadFile/', headers=header, files=files, data=path)
        print response.content

    def download_file(self, filename):
        requests.get(constants.server_url + '/GetFile/' + self.username + '/' + filename)

    def delete_file(self, full_path):
        #TODO: access deletion endpoint
        header = {
            'Authorization': 'Token ' + self.token
        }
        path = {
            'path': full_path[:full_path.rfind('/') + 1]
        }
        files = {
            'file': open('../Server/Files/' + full_path, 'rb')
        }
        response = requests.delete(constants.server_url + '/DeleteFile/', headers= header, files=files, data=path)
        print response.content

    def check_server(self):
        server_files = self.list_files()
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "clientLog.json"))
        client_files = open(filepath, "r")
        # For each server file, whatever the client doesn't have the client should pull from the server
        # For each client file, whatever the server doesn't have the client should push to the server
        for line in client_files:
            if line[2] == "deleted":
                self.delete_file(line[1])
            else:
                self.upload_file(line[1])


if __name__ == '__main__':
    pass