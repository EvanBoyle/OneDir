__author__ = 'ta3fh', 'csh7kd'
# NOTE: Run this on command prompt because password prompts don't work in IDE.

import requests
import json
import getpass
import synchronization

token = ''

def getToken(username, password):
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', {'username': username, 'password' : password})
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
    response = requests.get('http://127.0.0.1:8000/LoggedIn/',headers = header)
    return response.startswith('User is currently logged in.')

def login(username, password):
    getToken(username, password)
    return token != 'Error'

# TODO: Check if username already exists
def register(username, email, password):
    response = requests.post('http://127.0.0.1:8000/CreateUser/', {'username': username, 'email': email,
                                                                   'password': password})
    if response.content == 'User has been created.':
        login(username, password)

def passwordchange(old_pw, new_pw, un):
    login(un, old_pw)
    header = {}
    header['Authorization']= 'Token '+ token
    response = requests.post('http://127.0.0.1:8000/ChangePassword/', {'oldPass': old_pw, 'newPass': new_pw},
                  headers=header)
    if response.content == 'User password changed successfully.':
        print ('   User password changed successfully.')
    else:
        print(' User password change was unsuccessful.')

if __name__ == '__main__':
    print 'Welcome to OneDir!'
    input = raw_input('Enter 0 to login or 1 to register: ')
    while input != '0' and input != '1':
        print '   Incorrect input.'
        input = raw_input('Enter 0 to login or 1 to register: ')

    # Login
    if input == '0':
        while True:
            un = raw_input('Username: ')
            pw = getpass.getpass()
            if login(un, pw):
                print '   Login successful.'
                synchronization.initialize(token, un) # This authenticates checking the server for files
                break
            print '   Login unsuccessful.'

    # Register. Run main.py on command prompt because password prompts don't work in IDE.
    if input == '1':
        while True:
            un = raw_input('Username: ')
            email = raw_input('Email: ')
            pw = getpass.getpass()
            confirm = getpass.getpass('Confirm password: ')
            if confirm == pw:
                register(un, email, pw)
                print '   Registration successful.'
                break
            print('   Passwords do not match.')

    input2 = raw_input('Enter 0 to view files or 1 to change password: ')
    while input2 != '0' and input2 != '1':
        print ('   Incorrect input.')
        input2 = raw_input('Enter 0 to view files or 1 to change password: ')

# View files
    if input2 == '0':
        print ('Your files on the server: ')
        #ListFiles

# Change password. Not working currently because getting a token is returning a None type.
    if input2 == '1':
        old_pw = getpass.getpass('Enter old password: ')
        while old_pw != pw:
            print('   Incorrect password.')
            old_pw = getpass.getpass('Enter old password: ')
        new_pw = getpass.getpass('Enter new password: ')
        new_pw2 = getpass.getpass('Confirm new password: ')
        while new_pw2 != new_pw:
            print('   Passwords do not match.')
            new_pw = getpass.getpass('Enter new password: ')
            new_pw2 = getpass.getpass('Confirm new password: ')
        passwordchange(old_pw, new_pw, un)
