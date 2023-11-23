#!/usr/bin/python3
"""Module to filter states"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3]
    )

    """ create a crsor object """
    cursor = db.cursor()

    """ write and execute the sql query """
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(argv[4]))

    """ fetch the results of the query from"""
    res = cursor.fetchall()

    """ print the results """
    for row in res:
        print(row)
