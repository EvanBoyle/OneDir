__author__ = 'csh7kd'

import requests

def checkAuth():
    un = raw_input('username: ')
    pw = raw_input('password: ')
    response = requests.post('http://127.0.0.1:8000/AuthTest/', {'username': un, 'password': pw})
    print response.content

def getToken():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', {'username': 'evan', 'password' : 'password'})
    print response.content

def testToken():
    header = {}
    header['Authorization']= 'Token 93bedfe2392599773a4a55610defbc0357b26f64'
    header['content-type']='application/json'
    response = requests.get('http://127.0.0.1:8000/LoggedIn/',headers = header)
    print response.content

if __name__ == '__main__':
    testToken()