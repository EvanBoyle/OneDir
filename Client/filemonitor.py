__authors__ = 'ta3fh', 'mmo7kd'

import sys
import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

change_list = []

class FileHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """

    def process(self, event):
        str1 = event.src_path
        str2 = str1[-10:]
        #print(str2)
        if str2 != "updates.js":
            print(event.src_path + ": " + event.event_type)
            add_to_file(event.src_path, event.event_type)

    def on_any_event(self, event):
        self.process(event)

#Adds file changes to a dictionary, which is then added to the master list change_list
def add_to_file(src_path, event_type):
    dataDict = {}
    dataDict[src_path] = event_type
    change_list.append(dataDict)

#Dumps everything into the json file updates.js
def json_dump(list_obj):
    j = json.dumps(list_obj)
    json_file = 'updates.js'
    f2 = open(json_file, 'w')
    print >> f2, j
    f2.close()

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
            time.sleep(1)   # set to 1 for testing purposes
            json_dump(change_list)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
