__authors__ = 'csh7kd', 'ta3fh', 'mmo7kd'

import sys
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./Server.settings")
import json
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileMovedEvent

# class FileHandler(FileSystemEventHandler):
#     """
#     Watches for events (creation, deletion, and modification of files), then prints the event type and path.
#     """
#
#     def process(self, event):
#         size = -1
#         time = datetime.datetime.utcnow()
#         file_time = time.strftime("%y-%m-%dT%H:%M:%S.%f")
#         file_time = file_time[:-3] + "Z" #weird formatting to match Django
#         if os.path.isfile(event.src_path):
#             if event.event_type == "created" or event.event_type == "modified" or event.event_type == "moved":
#                 filename = event.src_path.replace("\\\\", "\\")
#                 size = os.stat(filename).st_size
#         # print event.src_path + ": " + str(size) + " " + event.event_type
#         logfilepath = "./clientLog.json"
#         if not os.path.exists(logfilepath):
#             open(logfilepath, "w")
#         # gets path relative to ~/onedir. This means users are not allowed to create directories called onedir!
#         filepath = event.src_path[event.src_path.rfind('onedir')+7:]
#
#         # if '___' not in event.src_path and (size != -1 or event.event_type == "deleted"):
#         #     f = open(logfilepath, "a")
#         #     f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
#         #     f.writelines("\n")
#
#         f = open(logfilepath, "a")
#         f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
#         f.writelines("\n")
#
#     def on_any_event(self, event):
#         self.process(event)
#
#     def on_moved(self, event):
#         moved_event = FileMovedEvent(event)
#         logfilepath = "./clientLog.json"
#         f = open(logfilepath, "a")
#         f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
#         f.writelines("\n")

class LoggingEventHandler(FileSystemEventHandler):
    """
    Watches for events (creation, deletion, and modification of files), then prints the event type and path.
    """

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
        logfilepath = "./clientLog.json"
        if not os.path.exists(logfilepath):
            open(logfilepath, "w")
        # gets path relative to ~/onedir. This means users are not allowed to create directories called onedir!
        filepath = event.src_path[event.src_path.rfind('onedir')+7:]

        # if '___' not in event.src_path and (size != -1 or event.event_type == "deleted"):
        #     f = open(logfilepath, "a")
        #     f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
        #     f.writelines("\n")

        if event.event_type != "moved":
            f = open(logfilepath, "a")
            f.writelines(json.dumps({'file': filepath, 'size': size, 'event': event.event_type, 'time': file_time}, sort_keys=True))
            f.writelines("\n")

    def on_any_event(self, event):
        self.process(event)

    def on_moved(self, event):
        size = -1
        time = datetime.datetime.utcnow()
        file_time = time.strftime("%y-%m-%dT%H:%M:%S.%f")
        file_time = file_time[:-3] + "Z" #weird formatting to match Django
        filepath = event.dest_path[event.dest_path.rfind('onedir')+7:]
        filename = event.dest_path.replace("\\\\", "\\")
        size = os.stat(filename).st_size
        old_filepath = event.src_path[event.dest_path.rfind('onedir')+7:]
        old_filename = event.src_path.replace("\\\\", "\\")
        logfilepath = "./clientLog.json"
        f = open(logfilepath, "a")
        f.writelines(json.dumps({'file': old_filepath, 'size': -1, 'event': 'deleted', 'time': file_time}, sort_keys=True))
        f.writelines("\n")
        f.writelines(json.dumps({'file': filepath, 'size': size, 'event': 'created', 'time': file_time}, sort_keys=True))
        f.writelines("\n")


if __name__ == '__main__':
    path_name = os.getenv("HOME") + '/onedir'
    # print os.path.exists(os.path.dirname(path_name))
    observer = Observer()
    observer.schedule(LoggingEventHandler(), path=path_name, recursive=True)
    observer.start()

    try:
        # print("Watching for changes...")
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

