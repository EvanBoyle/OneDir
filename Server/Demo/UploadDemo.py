__author__ = 'hodor'

import requests

def UploadDemo():
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', {'username': 'evan', 'password' : 'password'})
    token = response.json()['token']
    header = {}
    header['Authorization']= 'Token '+ token

    files = {'file': open('/home/hodor/OneDir/OneDir/Server/Demo/lol.txt', 'rb')}
    response = requests.post('http://127.0.0.1:8000/UploadFile/', headers=header, files=files)
    print response.content

if __name__ == '__main__':
    UploadDemo()