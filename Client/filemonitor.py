__authors__ = 'ta3fh', 'mmo7kd'

import sys
import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

    def on_any_event(self, event):
        self.process(event)

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
