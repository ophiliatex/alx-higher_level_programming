#!/usr/bin/python3
"""
Script: list_states.py

Description:
This script lists all states from the database 'hbtn_0e_6_usa' with the name
passed as an argument. It connects to the MySQL database using the provided
credentials and retrieves the states whose names start with 'N', displaying
the results in the order of state IDs.

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
    - Executes a SQL query to retrieve states with names starting with 'N'.
    - Displays the results in the order of state IDs.

    Arguments:
    sys.argv[1]: MySQL username
    sys.argv[2]: MySQL password
    sys.argv[3]: Database name

    Usage Example:
    python3 list_states.py myusername mypassword hbtn_0e_6_usa
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT
            cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.states_id = state.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
