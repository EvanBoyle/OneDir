__author__ = 'csh7kd'

import csv
import datetime
import sqlite3 as lite
import sys
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
from django.contrib.auth.models import User
from django.core import management


### RESET DATABASE ###

management.call_command('syncdb', verbosity=1)
management.call_command('flush', verbosity=0, interactive=False) #delete database

### CREATE TEST USERS ###
User.objects.create_user('testuser1', 'test1@gmail.com', 'testpassword1').save()
User.objects.create_user('testuser2', 'test2@gmail.com', 'testpassword2').save()