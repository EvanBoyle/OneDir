__authors__ = 'ta3fh', 'mmo7kd'

import sys
import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

class FileHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """
    
    # dataDict = {}
    def process(self, event):
        size = -1
        if os.path.isfile(event.src_path):
            if event.event_type == "created" or event.event_type == "modified":
                filename = event.src_path.replace("\\\\", "\\")
                print filename
                size = os.stat(filename).st_size
        # print event.src_path + ": " + str(size) + " " + event.event_type
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "clientLog.json"))
        f = open(filepath, "a")
        f.writelines(json.dumps({'file': event.src_path, 'size': size, 'event': event.event_type}, sort_keys=True))
        f.writelines("\n")
        check_local()
        check_server()

    def on_any_event(self, event):
        self.process(event)


def check_local():
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "clientLog.json"))
    f = open(filepath, "r")
    for line in f:
        if line[2] == "created":
            UploadFile(line)
            #I know I need to change the line to a request and then send that to UploadFile, but I'm not sure how
        if line[2] == "deleted":
            #Here is where the code for deleting a file locally will go
        if line[2] == "modified":
            #Here is where the code for deleting a file locally will go
            UploadFile(line)


def check_server():
    change_files = ListFiles()
    for line in change_files:
        if line[2] == "created":
            UploadFile(line)
            #I know I need to change the line to a request and then send that to UploadFile, but I'm not sure how
        if line[2] == "deleted":
            #Here is where the code for deleting a file will go
        if line[2] == "modified":
            #Here is where the code for deleting a file will go
            UploadFile(line)



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        path_name = '.'
    else:
        path_name = sys.argv[1]
        if not os.path.exists(os.path.dirname(path_name)):
            print("Path name does not exist. Default to current directory.")
            path_name = '.'

    observer = Observer()
    observer.schedule(FileHandler(), path=path_name, recursive=True)
    observer.start()

    try:
        print("Watching for changes...")
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

