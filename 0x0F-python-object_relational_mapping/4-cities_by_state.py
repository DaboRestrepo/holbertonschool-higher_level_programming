#!/usr/bin/python3
"""Get a states list from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Has to take 3 arguments:
    argv[1]: username
    argv[2]: password
    argv[3]: database name
    It set a rlation ship between states and cities."""
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id ORDER BY\
                   cities.id;")
    results = cursor.fetchall()
    for data in results:
        print(data)
    cursor.close()
    connection.close()
