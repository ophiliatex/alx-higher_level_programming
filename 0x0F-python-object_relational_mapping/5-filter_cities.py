#!/usr/bin/python3

"""
Script: list_states.py

Description:
This script lists all cities from the database 'hbtn_0e_6_usa' and their
corresponding states. It connects to the MySQL database using the provided
credentials and retrieves the cities along with their associated states,
displaying the results in the order of city IDs.

Usage:
python3 list_states.py <MySQL_username> <MySQL_password> <database_name>

Example:
python3 list_states.py myusername mypassword hbtn_0e_6_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to execute the script.

    - Connects to the MySQL database using provided credentials.
    - Executes a SQL query to retrieve cities and their associated states.
    - Displays the results in the order of city IDs.

    Arguments:
    sys.argv[1]: MySQL username
    sys.argv[2]: MySQL password
    sys.argv[3]: Database name

    Usage Example:
    python3 list_states.py myusername mypassword hbtn_0e_6_usa
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        ORDER BY
            cities.id ASC
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the database connection
    db.close()
