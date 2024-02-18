#!/usr/bin/python3

"""
prints the State object with the name
passed as an argument from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the database tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state to the database
    new_state = State(name='Louisiana')
    session.add(new_state)

    # Query the added state and print its ID
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)

    # Commit the changes to the database
    session.commit()
