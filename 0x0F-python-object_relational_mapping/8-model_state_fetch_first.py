#!/usr/bin/python3

"""
prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).first()

    if instance is None:
        print("Nothing")
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
