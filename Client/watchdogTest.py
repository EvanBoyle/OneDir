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
# test.txt created, test.txt modified, test.txt modified again, test_rename.txt deleted, new_test.txt created,
# testdir created, new_test.txt deleted, new_test.txt created, testdir modified, new_test.txt deleted
    createFile("test.txt")
    time.sleep(2)
    editFile("test.txt", "hi")
    time.sleep(2)
    # deleteFile("test.txt")
    # deleteFile("test2.txt")
    # renameFile("test.txt", "test_rename.txt")
    # time.sleep(2)
    # deleteFile("test_rename.txt")
    # time.sleep(2)
    # if not os.path.exists("testdir"):
    #     os.mkdir("testdir")
    # time.sleep(2)
    # moveFile("new_test.txt", "testdir/new_test.txt")
    # time.sleep(2)
    # os.chdir("testdir")
    # time.sleep(2)
    # editFile("new_test.txt")
    # time.sleep(2)
    # deleteFile("new_test.txt")
    # time.sleep(10)
    # shutil.rmtree("/testdir")
