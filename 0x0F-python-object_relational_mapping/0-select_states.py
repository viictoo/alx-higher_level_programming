#!/usr/bin/python3
""" lists all states from the database"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host='localhost',
        port=3306)
    c = db.cursor()
    c.execute('SELECT * FROM states')
    lines = c.fetchall()

    for line in lines:
        print(line)
