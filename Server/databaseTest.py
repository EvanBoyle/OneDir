__author__ = 'csh7kd'

import sqlite3 as lite
import json

if __name__ == '__main__':
    try:
        con = lite.connect('test.db')
        cur = con.cursor()
        config = open('testData.txt', 'r')
        data = json.load(config)
        users = data['users']
        files = data['files']
        cur.execute("DROP TABLE IF EXISTS testusers")
        cur.execute("CREATE TABLE testusers(username text, passwordHash text)")
        cur.execute("DROP TABLE IF EXISTS testfiles")
        cur.execute("CREATE TABLE testfiles(username text, filename text, fileHash text)")

        cur.executemany("INSERT INTO testusers VALUES(?, ?)", users)
        cur.executemany("INSERT INTO testfiles VALUES(?, ?, ?)", files)


        print "users: "
        cur.execute("SELECT * FROM testusers")
        while True:
            row = cur.fetchone()
            if row is None:
                break
            print str(row)

        print "files: "
        cur.execute("SELECT * FROM testfiles")
        while True:
            row = cur.fetchone()
            if row is None:
                break
            print str(row)

    except lite.Error, e:

        if con:
            con.rollback()

        print "Error %s:" % e.args[0]
    finally:

        if con:
            con.close()
