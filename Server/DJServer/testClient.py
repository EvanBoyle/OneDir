__author__ = 'ta3fh'
import requests

user = """
{
    "username":tanya,
    "email":lol@gmail.com,
    "password":pass
}
"""

headers = {'content-type': 'application/json'}
url = "127.0.0.1:8000/CreateUser"
data = user;

r = requests.post(url, data=data, headers=headers)
print r.status_code
# try:
#     print r.json()
# except ValueError:
#     print "No JSON included in response"