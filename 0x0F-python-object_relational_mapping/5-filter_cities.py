#!/usr/bin/python3
"""takes in the name of a state as an argument
and lists all cities of that state
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
    c.execute("select cities.name from cities, states where \
              cities.state_id = states.id and states.name = %s",
              (db.escape_string(argv[4]),))
    lines = c.fetchall()
    if (len(lines) == 0):
        print()
    i = 1
    for line in lines:
        if i != len(lines):
            print(line[0], end=', ')
        else:
            print(line[0])
        i += 1
