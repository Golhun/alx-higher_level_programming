#!/usr/bin/python3
"""
Script to list all states from a MySQL database.

Usage: ./0-select_states.py <username> <password> <database>
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    List all states from the specified MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Execute the query to select all states and sort by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'db' in locals() and db is not None:
            db.close()


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    list_states(username, password, database)
