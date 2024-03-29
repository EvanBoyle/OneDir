__author__ = 'ta3fh', 'csh7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.Server.settings")
import requests
import sys
import constants
import json
import time
import main
import urllib2
# from Server.DJServer.views import *


class Synchronization:

    def __init__(self, t, un, s):  # Initialized in main.py to authenticate checking the server for files
        self.token = t
        self.username = un
        file = open('.sync', 'r')
        self.sync = file.readline()

    def list_files(self):
        header = {}
        header['Authorization']= 'Token '+ self.token
        response = requests.get(constants.server_url + '/ListFiles/' + self.username, headers=header)
        return response.content

    def upload_file(self, full_path):
        # print os.getenv("HOME")
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
        # print response.content

    def download_file(self, filename):
        header = {
            'Authorization': 'Token ' + self.token
        }
        #requests.get(constants.server_url + '/GetFile/' + self.username + '/' + filename)
        # print constants.server_url + '/GetFile/' + self.username + '/' + filename
        req = urllib2.Request(constants.server_url + '/GetFile/' + self.username + '/' + filename, headers=header)
        file = urllib2.urlopen(req)
        local = open(os.getenv("HOME") + '/onedir/' + filename, 'w')
        local.write(file.read())
        local.close()

    def delete_file(self, full_path):
        header = {
            'Authorization': 'Token ' + self.token
        }
        response = requests.delete(constants.server_url + '/DeleteFile/' + self.username + '/' + full_path , headers= header)
        # print response.content

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

        server_json = json.loads(server_files)
        i = 0
        while i < len(server_json):
            name = server_json[i][0]
            timestamp_string = server_json[i][3]
            timestamp = time.mktime(time.strptime(str(server_json[i][3]), '%Y-%m-%dT%H:%M:%S.%fZ'))
            if name not in serverNames.keys() or timestamp > serverNames[name]:
                serverNames[name] = timestamp
            i += 1

        for file in localNames.keys():
            if file not in serverNames.keys() or localNames[file][0] > serverNames[file]:
                if localNames[file][1] == "deleted":
                    self.delete_file(file)
                else:
                    self.upload_file(file)

        for file in serverNames.keys():
            # print serverNames.keys()
            if file not in localNames.keys() or serverNames[file] > localNames[file][0]:
                self.download_file(file)

        # for line in client_files:
        #     entry = json.loads(line)
        #     if entry["event"] == "deleted":
        #         self.delete_file(entry["file"])
        #     else:
        #         self.upload_file(entry["file"])
        os.remove("clientLog.json")
        f = open("clientLog.json", 'w') #wipe clientLog after sync finishes
        f.close()


    # def start(self):
    #     print "sync " + str(self.sync)
    #     print "is logged in " + str(main.isLogged(self.token))
    #     if main.isLogged(self.token):
    #         if self.sync:
    #             mySync = Synchronization(self.token, self.username, self.sync)
    #             mySync.check_server()



if __name__ == '__main__':
    token = sys.argv[1]
    username = sys.argv[2]
    while True:
        file = open('.sync', 'r')
        sync = file.readline()
        # print "sync " + str(sync)
        # print "is logged in " + str(main.isLogged(token))
        if main.isLogged(token):
            if sync=='True':
                mySync = Synchronization(token, username, sync)
                mySync.check_server()
        time.sleep(60)

