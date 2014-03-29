__author__ = 'csh7kd'

import requests

if __name__ == '__main__':
    un = raw_input('username: ')
    pw = raw_input('password: ')
    response = requests.post('http://127.0.0.1:8000/AuthTest/', {'username': un, 'password': pw})
    print response.content