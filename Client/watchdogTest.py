__author__ = 'ta3fh'
# Run this while running filemonitor

import os
import shutil

def createFile(name):
    file = open(name, 'w')

def deleteFile(name):
    os.remove(name)

def editFile(name):
    file = open(name, 'w')
    file.write("Edit \n")

def moveFile(name, dir):
    shutil.move(name, dir)

def renameFile(name, newName):
    os.rename(name, newName)

if __name__=='__main__':
# test.txt created, test.txt modified, test.txt modified again, test_rename.txt deleted, new_test.txt created,
# testdir created, new_test.txt deleted, new_test.txt created, testdir modified, new_test.txt deleted
    createFile("test.txt")
    editFile("test.txt")
    renameFile("test.txt", "test_rename.txt")
    deleteFile("test_rename.txt")
    createFile("new_test.txt")
    if not os.path.exists("testdir"):
        os.mkdir("testdir")
    moveFile("new_test.txt", "testdir")
    os.chdir("testdir")
    deleteFile("new_test.txt")
