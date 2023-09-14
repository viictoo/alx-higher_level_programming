#!/usr/bin/python3
"""lists all cities from the database"""

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
    c.execute("select cities.id, cities.name, states.name from cities,\
              states where cities.state_id = states.id order by cities.id asc")
    lines = c.fetchall()

    for line in lines:
        print(line)
