#!/usr/bin/python3
"""Module to filter states based on user-provided input"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    uinput = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3]
    )

    """ create a crsor object """
    cursor = db.cursor()

    """ write and execut the sql query """
    query = "SELECT * FROM states WHERE name LIKE BINARY %s \
        ORDER BY states.id ASC"
    cursor.execute(query, (uinput,))

    """ fetch the results of the query from """
    res = cursor.fetchall()

    """ print the results """
    for row in res:
        print(row)
