__author__ = 'ta3fh', 'csh7kd'
# NOTE: Run this on command prompt because password prompts don't work in IDE.

import requests
import json
import getpass
import synchronization
import sys
sys.path.append("..")
import constants
import sys
import getopt
token = ''
sync = False

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
    return response.startswith(constants.h_loggedIn_true)

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
    if len(sys.argv <= 1):
        print 'main.py <sync>'
    else:
        if sys.argv[1] == 0:
            print 'Auto synchronization off.'
        if sys.argv[1] == 1:
            print 'Auto synchronization on.'
            global sync
            sync = True

    try:
        print constants.p_welcome
        input = raw_input('Enter 0 to login or 1 to register: ')
        while input != '0' and input != '1':
            print constants.indent(constants.p_incorrect_input)
            input = raw_input('Enter 0 to login or 1 to register: ')

        # Login
        if input == '0':
            while True:
                un = raw_input('Username: ')
                pw = getpass.getpass()
                if login(un, pw):
                    print constants.indent(constants.p_login_success)
                    synchronization.initialize(token, un, sync) # This authenticates checking the server for files
                    break
                print constants.indent(constants.p_login_fail)

        # Register. Run main.py on command prompt because password prompts don't work in IDE.
        if input == '1':
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

        input2 = raw_input('Enter 0 to view files or 1 to change password: ')
        while input2 != '0' and input2 != '1':
            print constants.indent(constants.p_incorrect_input)
            input2 = raw_input('Enter 0 to view files or 1 to change password: ')

    # View files
        if input2 == '0':
            listfiles(un)

    # Change password
        if input2 == '1':
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

    except KeyboardInterrupt:
        print constants.p_goodbye
