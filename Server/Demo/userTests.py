__author__ = 'csh7kd'

import requests

def TestUserCreation():
    response = requests.post('http://127.0.0.1:8000/CreateUser/', {'username': 'tanya2', 'email': 'lolz@gmail.com',
                                                                   'password': 'password'})
    print response.content

def TestCreateAndChange():
    requests.post('http://127.0.0.1:8000/CreateUser/', {'username': 'craig', 'email': 'lolzz@gmail.com',
                                                        'password': 'password'})
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', {'username': 'craig', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token
    response2 = requests.post('http://127.0.0.1:8000/ChangePassword/', {'oldPass': 'password', 'newPass': 'password1'},
                              headers=header)
    print response2.content

if __name__ == '__main__':
    TestCreateAndChange()