__author__ = 'mmo7kd'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.conf import settings
from django.contrib.auth.models import User
from models import ODFile
import requests
import constants

def printAllFiles():
    query = ODFile.objects.filter()
    files = query.values_list()
    print "\nUser ID  %-10s %s" % ("File Size", "File Name")
    print "============================="
    fileNumber = 0
    totalSize = 0
    for f in files:
        print "%-8s %-10s %s" % (f[2], f[4], f[1])
        fileNumber += 1
        totalSize += f[4]
    print "Total Number of files: %d \n" % (fileNumber)
    print "Size of all files: %d \n" % (totalSize)

def DeleteUser(uname):
    response = requests.post(constants.server_url + '/api-token-auth/', {'username': 'admin', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token
    response = requests.delete(constants.server_url + '/DeleteUser/%s', headers= header) % (uname)
    return response

def printUserFiles(user):
    fileNumber = 0
    totalSize = 0
    query = ODFile.objects.filter(name = user)
    if query.isEmpty():
        print "No files for given user or user does not exist.\n"
    else:
        print "\nFile Size  File Name"
        print "===================="
        files = query.values_list()
        for f in files:
            fileNumber += 1
            totalSize += f[4]
            print "%-9s  %s" % (f[4], f[1])
        print "\nTotal number of files: %d" % (fileNumber)
        print "Size of all files: %d \n" % (totalSize)

def changePassword(uname, newPassword):
    u = User.objects.get(username__exact=uname)
    u.set_password(newPassword)
    u.save()

def main():
    action = raw_input("Enter 0 to see files, 1 to delete a user, or 2 to change a user's password.\n")
    if action == "0":
        action2 = raw_input("Enter 0 to see all files or 1 to see files owned by a certain user.\n")
        if action2 == "0":
            printAllFiles()
        if action2 == "1":
            user_name = raw_input("Enter the user ID.\n")
            printUserFiles(user_name)
    if action == "1":
        action2 = raw_input("Enter the user name.\n")
        response = DeleteUser(action2)
        print response.content()
    if action == "2":
        userName = raw_input("Enter the name of the user whose password you want to change.\n")
        newPassword = raw_input("Enter the new password for this user.\n")
        changePassword(userName, newPassword)
    else:
        print "Not a valid response. Please try again. \n"

if __name__ == "__main__":
    main()
