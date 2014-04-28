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

# def moveFile(name, dir):
#     os.rename(os.getenv("HOME") + "/onedir/" + name, dir)

def renameFile(name, newName):
    os.rename(os.getenv("HOME") + "/onedir/" + name, newName)

if __name__=='__main__':

    # createFile("test6.txt")
    time.sleep(2)
    editFile("test2.txt", "yayyyy download works")
    time.sleep(2)
    # deleteFile("test4.txt")

