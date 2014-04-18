__author__ = 'csh7kd'

import requests
import constants

def checkAuth():
    un = raw_input('username: ')
    pw = raw_input('password: ')
    response = requests.post(constants.server_url + '/AuthTest/', {'username': un, 'password': pw})
    print response.content

def getToken():
    response = requests.post(constants.server_url + '/api-token-auth/', {'username': 'evan', 'password' : 'password'})
    print response.content

def testToken():
    header = {}
    header['Authorization']= 'Token 93bedfe2392599773a4a55610defbc0357b26f64'
    header['content-type']='application/json'
    response = requests.get(constants.server_url + '/LoggedIn/',headers = header)
    print response.content

def TestListFilesNoAuth():
     response = requests.get(constants.server_url + '/ListFiles/evan')
     print response.content
def TestListFilesEvan():
    response = requests.post(constants.server_url + '/api-token-auth/', {'username': 'evan', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token
    header['content-type']='application/json'
    response = requests.get(constants.server_url + '/ListFiles/evan', headers=header)
    print response.content
def TestListFilesTanya():
    response = requests.post(constants.server_url + '/api-token-auth/', {'username': 'tanya', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token
    header['content-type']='application/json'
    response = requests.get(constants.server_url + '/ListFiles/tanya', headers=header)
    print response.content
if __name__ == '__main__':
    print "ListFiles with no auth: "
    TestListFilesNoAuth()
    print "ListFiles for user=evan:"
    TestListFilesEvan()
    print "ListFiles for user=tanya:"
    TestListFilesTanya()

