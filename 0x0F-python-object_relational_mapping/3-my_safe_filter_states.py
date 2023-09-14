#!/usr/bin/python3
"""safe from MySQL injections"""
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
    c.execute("SELECT * FROM states where name = %s order by id asc",
              ((db.escape_string(argv[4]),)))
    lines = c.fetchall()

    for line in lines:
        print(line)
