__author__ = 'mmo7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.conf import settings
from models import ODFile

def printAllFiles():
    query = ODFile.objects.filter()
    files = query.values_list()
    print "User ID  %-10s %s \n" % ("File Size", "File Name")
    fileNumber = 0
    totalSize = 0
    for f in files:
        print "%-9s %-10s %s" (f[2], f[4], f[1])
        fileNumber += 1
        totalSize += f[4]
    print "Total Number of files: %d \n" (fileNumber)
    print "Size of all files: %d \n" (totalSize)

def printUserFiles(user):
    fileNumber = 0
    totalSize = 0
    query = ODFile.objects.filter(name = user)
    if query.isEmpty():
        print "No files for given user or user does not exist.\n"
    else:
        print "File Size  File Name \n" ("File Name")
        files = query.values_list()
        for f in files:
            fileNumber += 1
            totalSize += f[4]
            print "%-11d  %d" (f[4], f[1])
        print "Total Number of files: %d \n" (fileNumber)
        print "Size of all files: %d \n" (totalSize)

def main():
    action = raw_input("Enter 0 to see stored files.\n")
    if action == "0":
        action2 = raw_input("Enter 0 to see all files or 1 to see files owned by a certain user.\n")
        if action2 == "0":
            printAllFiles()
        if action2 == "1":
            user_name = raw_input("Enter the user ID.\n")
            printUserFiles(user_name)
    else:
        print "Not a valid response. Please try again. \n"

if __name__ == "__main__":
    main()