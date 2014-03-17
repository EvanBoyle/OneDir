__author__ = 'ta3fh'

import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """

    def process(self, event):
        print event.event_type + ": " + event.src_path

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

if __name__ == '__main__':

    # if no commandline argument, use current directory
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
    except KeyboardInterrupt:
        observer.stop()
    observer.join()