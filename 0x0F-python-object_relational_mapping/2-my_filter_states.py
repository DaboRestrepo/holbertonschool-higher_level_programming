#!/usr/bin/python3
"""Get a states list from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Has to take 3 arguments:
    argv[1]: username
    argv[2]: password
    argv[3] database name.
    It must filter a state using an input."""
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE '{:s}'\
                   ORDER BY id;".format(argv[4]))
    results = cursor.fetchall()
    for data in results:
        if data[1] == argv[4]:
            print(data)
    cursor.close()
    connection.close()
