#!/usr/bin/python3
"""Get a states list from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Has to take 3 arguments:
    argv[1]: username
    argv[2]: password
    argv[3]: database name
    argv[4]: the state name
    It set a relationship between states and cities."""
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   WHERE states.name = %(stateName)s\
                   ORDER BY cities.id;", {'stateName': argv[4]})
    results = cursor.fetchall()
    print(str(', '.join(data[0] for data in results)))
    cursor.close()
    connection.close()
