#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""

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
    q = "SELECT * FROM states where name LIKE '{:s}' \
      order by id asc".format(argv[4])
    c.execute(q)
    lines = c.fetchall()

    for line in lines:
        print(line)

    c.close()
    db.close()
