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

import sys
from model_state import Base, State
from sqlalchemy import create_engine

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

    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the database tables if they do not exist
    Base.metadata.create_all(engine)
