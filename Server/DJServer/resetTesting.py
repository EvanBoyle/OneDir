__author__ = 'csh7kd'

import csv
import datetime
import sqlite3 as lite
import sys
#from django.contrib.auth.models import User

try:
    con = lite.connect('db.sqlite3')

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS DJServer_file")

    #NOTE: this database's creation was copied from the automated Django generation and should not be
    #modified unless the File model under DJServer.model.py is changed.
    cur.execute("CREATE TABLE \"DJServer_file\" (" +
                "\"id\" integer NOT NULL PRIMARY KEY, " +
                "\"fileName\" varchar(500) NOT NULL, " +
                "\"name_id\" integer NOT NULL REFERENCES \"auth_user\" (\"id\"), " +
                "\"fileHash\" varchar(256) NOT NULL, " +
                "\"timestamp\" time NOT NULL" +
                ")")
    cur.execute("CREATE INDEX \"DJServer_file_4da47e07\" ON \"DJServer_file\" (\"name_id\")")
    con.commit()

    #TODO: user creation is currently not working due to an exception when trying to import User.

    #######################
    #Create new test if they don't already exist
    #######################
    #if not User.objects.filter(username='testUser1').count():
    #    User.objects.create_user('testUser1', 'test1@gmail.com', 'password')
    #if not User.objects.filter(username='testUser2').count():
    #    User.objects.create_user('testUser2', 'test2@gmail.com', 'password')

    #######################
    #Insert files into database
    #######################
    now = datetime.datetime.now()
    #User ID increments from 1. 1 should be your superuser, so for now all are assigned to user ID 2, which should be
    #the first user created by admin.
    test_files = [(1, 'file1', 3, 1, now), (2, 'filetest', 2, 2, now), (3, 'file3', 4, 3, now) ]
    cur.executemany('INSERT INTO DJServer_file VALUES (?,?,?,?,?)', test_files)
    con.commit()
    cur.execute("Select * from DJServer_file")
    while True:
        row = cur.fetchone()

        if row == None:
            break

        print row


except lite.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()