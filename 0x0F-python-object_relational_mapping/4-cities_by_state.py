#!/usr/bin/python3
"""Module to list all citie"""


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
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC;")

    """ fetch the results of the query """
    res = cursor.fetchall()

    """ print the results """
    for row in res:
        print(row)

    # Close cursor
    cursor.close()
    # Close database
    db.close()
