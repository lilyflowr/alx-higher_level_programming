#!/usr/bin/python3
"""
This module is use to connect to a MySQL database and retrieve all records
from the 'states' table sorted by their IDs in ascending order.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the MySQL database using credentials and database name passed as command-line arguments
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SQL query to retrieve all states, sorted in ascending order by their IDs
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the results of the query
    res = cursor.fetchall()

    # Iterate through the results and print each state
    for row in res:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
