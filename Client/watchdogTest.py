__author__ = 'ta3fh'
# Run this while running filemonitor

import os
import shutil
import time

def createFile(name):
    file = open(os.getenv("HOME") + "/onedir/" + name, 'w')

def deleteFile(name):
    os.remove(os.getenv("HOME") + "/onedir/" + name)

def editFile(name, stuff):
    file = open(os.getenv("HOME") + "/onedir/" + name, 'w')
    file.write(stuff)

def makeDir(dirname):
    #mkdir only creates a directory if it does not already exist
    try:
        os.mkdir(os.getenv("HOME") + "/onedir/" + dirname)
    except OSError:
        pass

def moveFile(name, dir):
    shutil.move(os.getenv("HOME") + "/onedir/" + name, os.getenv("HOME") + "/onedir/" + dir)

def renameFile(name, newName):
    os.rename(os.getenv("HOME") + "/onedir/" + name, os.getenv("HOME") + "/onedir/" + newName)

if __name__=='__main__':

    # createFile("test8.txt")
    time.sleep(2)
    # editFile("test2.txt", "yayyyy download works")
    # renameFile("test2.txt", "test_rename.txt")
    # deleteFile("test_rename4.txt")
    time.sleep(2)
    # makeDir("testdir")
    time.sleep(2)
    # moveFile("test4.txt", "testdir")