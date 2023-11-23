#!/usr/bin/python3
"""Module to list all citis by state"""


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

    """ write and execute the sql query """
    query = "SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC;"
    cursor.execute(query, (uinput,))

    """ fetch the results of the query """
    res = cursor.fetchall()

    """ print the results """
    if res is not None:
        print(", ".join([row[0] for row in res]))

    # Close cursor
    cursor.close()
    # Close the database
    db.close()
