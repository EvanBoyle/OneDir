__authors__ = 'csh7kd', 'ta3fh', 'mmo7kd'

import sys
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.settings")
import json
import requests
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """

    # dataDict = {}
    def process(self, event):
        size = -1
        time = datetime.datetime.utcnow()
        file_time = time.strftime("%y-%m-%dT%H:%M:%S.%f")
        file_time = file_time[:-3] + "Z" #weird formatting to match Django
        if os.path.isfile(event.src_path):
            if event.event_type == "created" or event.event_type == "modified":
                filename = event.src_path.replace("\\\\", "\\")
                size = os.stat(filename).st_size
        # print event.src_path + ": " + str(size) + " " + event.event_type
        basepath = os.path.dirname(__file__)
        logfilepath = os.path.abspath(os.path.join(basepath, "..", "clientLog.json"))
        # gets path relative to OneDir/Server/Files/. This means users are not allowed to create directories called OneDir!
        filepath = event.src_path[event.src_path.rfind('OneDir')+20:]

        if '___' not in event.src_path and (size != -1 or event.event_type == "deleted"):
            f = open(logfilepath, "a")
            f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
            f.writelines("\n")
        #check_local()
        #check_server()

    def on_any_event(self, event):
        self.process(event)


if __name__ == '__main__':

    path_name = '../Server/Files'
    # print os.path.exists(os.path.dirname(path_name))
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

