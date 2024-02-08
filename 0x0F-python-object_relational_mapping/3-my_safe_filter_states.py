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
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    rows = cur.fetchall()

    for row in rows:
        print(row)
