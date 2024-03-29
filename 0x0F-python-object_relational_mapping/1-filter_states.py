#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
"""
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
    c.execute("SELECT * FROM states WHERE\
               name LIKE 'N%' ORDER BY states.id ASC")
    lines = c.fetchall()

    for line in lines:
        if line[1][0] == 'N':
            print(line)

    c.close()
    db.close()
