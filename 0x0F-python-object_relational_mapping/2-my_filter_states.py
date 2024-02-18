#!/usr/bin/python3

"""
Script: list_states_dynamic.py

Description:
This script connects to a MySQL database and retrieves states based on a provided name pattern. It takes MySQL credentials, database name, and name pattern as command-line arguments.

Usage:
python3 list_states_dynamic.py <MySQL_username> <MySQL_password> <database_name> <name_pattern>

Example:
python3 list_states_dynamic.py myusername mypassword hbtn_0e_6_usa 'N%'
"""

# Import necessary modules
import MySQLdb
import sys

if __name__ == "__main__":

    """
    Main function to execute the script.

    - Connects to the MySQL database using provided credentials.
    - Executes a dynamic SQL query to retrieve states based on the name pattern.
    - Displays the results ordered by state IDs.

    Arguments:
    sys.argv[1]: MySQL username
    sys.argv[2]: MySQL password
    sys.argv[3]: Database name
    sys.argv[4]: Name pattern for states (e.g., 'N%')

    Usage Example:
    python3 list_states_dynamic.py myusername mypassword hbtn_0e_6_usa 'N%'
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute dynamic SQL query to retrieve states based on name pattern
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Display the retrieved rows
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

