__authors__ = 'ta3fh', 'mmo7kd'

import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """
    
    dataDict = {}
    def process(self, event):
	self.dataDict[event.src_path] = event.event_type
        print event.event_type + ": " + event.src_path

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
