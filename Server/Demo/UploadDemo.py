__author__ = 'hodor'

import requests
import json

def UploadDemo():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', {'username': 'evan', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token
    payload = {}
    payload['path']= 'files/lulz/'

    files = {'file': open('/home/hodor/OneDir/OneDir/Server/Demo/lol.txt', 'rb')}
    response = requests.post('http://127.0.0.1:8000/UploadFile/', headers=header, files=files, data=payload)
    print response.content

if __name__ == '__main__':
    UploadDemo()