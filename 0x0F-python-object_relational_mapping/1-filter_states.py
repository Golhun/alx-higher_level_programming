#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N' from a MySQL database.

Usage: ./1-filter_states.py <username> <password> <database>
"""

import sys
import MySQLdb


def list_states_starting_with_n(username, password, database):
    """
    List states starting with 'N' from the specified MySQL database.

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

        # Execute the query to select states starting with 'N' and sort by id
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close cursor and connection
        try:
            cursor.close()
        except NameError:
            pass
        try:
            db.close()
        except NameError:
            pass


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    list_states_starting_with_n(username, password, database)
