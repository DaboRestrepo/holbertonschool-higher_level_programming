#!/usr/bin/python3
"""List the states."""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """List the states by id, using SQLAlchemy."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    update = session.query(State).filter_by(id=2).from_self()
    update[0].name = 'New Mexico'
    session.commit()
