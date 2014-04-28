__author__ = 'ta3fh', 'csh7kd'
# NOTE: Run this on command prompt because password prompts don't work in IDE.

import requests
import json
import getpass
import time
import synchronization
import filemonitor
from watchdog.observers import Observer
import sys
import constants
import getopt
import os
import subprocess
token = ''
sync = False

def syncOn():
    global sync
    sync = True

def syncOff():
    global sync
    sync = False

def getSync():
    return sync


def getToken(username, password):
    response = requests.post(constants.server_url + '/api-token-auth/', {'username': username, 'password' : password})
    # response.content["token"]
    global token
    if 'token' in json.loads(response.text):
        token = json.loads(response.text)['token']
    else:
        token = 'Error'

def isLogged(token):
    header = {}
    header['Authorization']= 'Token ' + token
    header['content-type']='application/json'
    response = requests.get(constants.server_url + '/LoggedIn/',headers = header)
    return response.content.startswith(constants.h_loggedIn_true)

def login(username, password):
    getToken(username, password)
    return token != 'Error'

def register(username, email, password):
    response = requests.post(constants.server_url + '/CreateUser/', {'username': username, 'email': email,
                                                                   'password': password})
    if response.content == constants.h_createUser_success:
        login(username, password)
        return True
    return False

def passwordchange(old_pw, new_pw, un):
    header = {}
    header['Authorization']= 'Token '+ token
    response = requests.post(constants.server_url + '/ChangePassword/', {'oldPass': old_pw, 'newPass': new_pw},
                  headers=header)
    if response.content == constants.h_changePassword_success:
        print constants.indent(constants.h_changePassword_success)
    else:
        print constants.indent(constants.h_changePassword_fail)

def listfiles(un):
    header = {}
    header['Authorization']= 'Token '+ token
    response = requests.get('http://127.0.0.1:8000/ListFiles/' + un, headers=header)
    if response.content == constants.h_listFiles_fail:
        print constants.indent(constants.p_listFiles_fail)
    else:
        json_data = json.loads(response.content)
        if len(json_data) == 0:
            print constants.indent(constants.p_listFiles_nofiles)
        else:
            print constants.indent(constants.p_listFiles_success)
            i = 0
            while i < len(json_data):
                print 'File name: ' + json_data[i][0] +  ' | File size: ' + str(json_data[i][1]) + ' | Last updated: ' + json_data[i][3]
                i += 1


if __name__ == '__main__':

    mySync = None

    #make ~/onedir if it doesn't exist
    try:
        os.makedirs(os.getenv("HOME") + '/onedir')
    except OSError as e:
        pass

    #start filemonitor in the background
    subprocess.call("python filemonitor.py &", shell=True)

    if len(sys.argv) <= 1:
        print '*auto synchronization = 0 or 1: main.py <sync>'
    else:
        if sys.argv[1] == 0:
            print 'Auto synchronization off.'
        if sys.argv[1] == 1:
            print 'Auto synchronization on.'
            syncOn()
            # mySync = synchronization.Synchronization(t, username, sync)
            # Synchronization needs username, how would we start syncing before login?


    try:
        print constants.p_welcome
        input = raw_input('Enter 1 to login or 2 to register: ')

	# Check for exit
        if input == '0':
	    print constants.p_goodbye
            exit()

        while input != '1' and input != '2':
            print constants.indent(constants.p_incorrect_input)
            input = raw_input('Enter 1 to login or 2 to register: ')


        # Login
        if input == '1':
            while True:
                un = raw_input('Username: ')
                pw = getpass.getpass()
                if login(un, pw):
                    print constants.indent(constants.p_login_success)
                    mySync = synchronization.Synchronization(token, un, sync) # This authenticates checking the server for files
                    break
                print constants.indent(constants.p_login_fail)

        # Register. Run main.py on command prompt because password prompts don't work in IDE.
        if input == '2':
            while True:
                un = raw_input('Username: ')
                email = raw_input('Email: ')
                pw = getpass.getpass()
                confirm = getpass.getpass('Confirm password: ')
                if confirm == pw:
                    if register(un, email, pw):
                        print constants.indent(constants.p_register_success)
                        break
                    else:
                        print constants.indent(constants.p_register_fail) #username is already in use
                else:
                    print constants.indent(constants.p_passwords_dont_match)

        while (True):
            input2 = raw_input('Enter 1 to view files, 2 to change password, or 3 to turn auto sync on/off: ')
            while input2 != '0' and input2 != '1' and input2 != '2' and input2 != '3' and input2 != '8' and input2 != '9':
                print constants.indent(constants.p_incorrect_input)
                input2 = raw_input('Enter 1 to view files, 2 to change password, or 3 to turn auto sync on/off: ')

            # Check for exit
            if input2 == '0':
                print constants.p_goodbye
                exit()

            # View files
            if input2 == '1':
                listfiles(un)

            # Change password
            if input2 == '2':
                old_pw = getpass.getpass('Enter old password: ')
                while old_pw != pw:
                    print constants.indent(constants.p_incorrect_password)
                    old_pw = getpass.getpass('Enter old password: ')
                new_pw = getpass.getpass('Enter new password: ')
                new_pw2 = getpass.getpass('Confirm new password: ')
                while new_pw2 != new_pw:
                    print constants.indent(constants.p_passwords_dont_match)
                    new_pw = getpass.getpass('Enter new password: ')
                    new_pw2 = getpass.getpass('Confirm new password: ')
                passwordchange(old_pw, new_pw, un)

            # Auto sync
            if input2 == '3':
                if sync:
                    print 'Auto synchronization off.'
                    syncOff()
                else:
                    print 'Auto synchronization on.'
                    syncOn()
                    mySync.start()

        if input2 == '9':
            mySync.upload_file('anivia2.mp3')

    except KeyboardInterrupt:
        print constants.p_goodbye
