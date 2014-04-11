__author__ = 'ta3fh', 'csh7kd'
# NOTE: Run this on command prompt because password prompts don't work in IDE.

import requests
import json
import getpass

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
        global token
        token = getToken(username, password)

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
