__author__ = 'mmo7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.conf import settings
from models import ODFile

def printAllFiles():
    query = ODFile.objects.filter()
    files = query.values_list()
    for f in files:
        print f[1]
        #print f[1] + "     " + f[2]

def printUserFiles(user):
    query = ODFile.objects.filter(name = user)
    if query.isEmpty():
        print "No files for given user or user does not exist.\n"
    files = query.values_list()
    for f in files:
        print f[1]

def main():
    action = raw_input("Enter 0 to see files.\n")
    if action == "0":
        action2 = raw_input("Enter 0 to see all files or 1 to see files owned by a certain user.\n")
        if action2 == "0":
            printAllFiles()
        if action2 == "1":
            uname = raw_input("Enter the name of the user.\n")
            printUserFiles(uname)

if __name__ == "__main__":
    main()
