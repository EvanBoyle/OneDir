__author__ = 'ta3fh', 'csh7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.Server.settings")
import requests
import sys
import constants
import json
import time
import main
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
        print os.getenv("HOME")
        header = {
            'Authorization': 'Token ' + self.token
        }
        path = {
            'path': full_path[:full_path.rfind('/') + 1]
        }
        files = {
            'file': open(os.getenv("HOME") + '/onedir/' + full_path, 'rb')
        }
        response = requests.post(constants.server_url + '/UploadFile/', headers=header, files=files, data=path)
        print response.content

    def download_file(self, filename):
        requests.get(constants.server_url + '/GetFile/' + self.username + '/' + filename)

    def delete_file(self, full_path):
        header = {
            'Authorization': 'Token ' + self.token
        }
        response = requests.delete(constants.server_url + '/DeleteFile/' + self.username + '/' + full_path , headers= header)
        print response.content

    def check_server(self):
        server_files = self.list_files()
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "clientLog.json"))
        client_files = open(filepath, "r")
        # For each server file, whatever the client doesn't have the client should pull from the server
        # For each client file, whatever the server doesn't have the client should push to the server
        localNames = {} #filename to timestamp
        serverNames = {}

        for line in client_files: #get most recent timestamp events for each local file
            entry = json.loads(line)
            timestamp = time.mktime(time.strptime(entry["time"], '%y-%m-%dT%H:%M:%S.%fZ'))
            if entry["file"] not in localNames.keys() or timestamp > localNames[entry["file"]][0]:
                localNames[entry["file"]] = (timestamp, entry["event"])

        for line in self.list_files():
            name = line[4:line.find(',') - 1]
            timestamp = line[line.rfind(',') + 3:-3]
            if name not in serverNames.keys() or timestamp > serverNames[name]:
                serverNames[name] = timestamp

        for file in localNames.keys():
            if file not in serverNames.keys() or localNames[file][0] > serverNames[file]:
                if localNames[file][1] == "deleted":
                    self.delete_file(file)
                else:
                    self.upload_file(file)

        for file in serverNames.keys():
            if file not in localNames.keys() or serverNames[file] > localNames[file][0]:
                self.download_file(file)

        # for line in client_files:
        #     entry = json.loads(line)
        #     if entry["event"] == "deleted":
        #         self.delete_file(entry["file"])
        #     else:
        #         self.upload_file(entry["file"])


if __name__ == '__main__':
    pass
    # make new instance of synchronization!
    # while True:
        # check whether logged in
        # if sync is on, check server.
        # if main.getSync():

