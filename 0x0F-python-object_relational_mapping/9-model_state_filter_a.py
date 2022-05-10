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
    state = session.query(State).\
        filter(State.name.like('%a%')).\
        order_by(State.id).all()

    for data in state:
        print("{}: {}".format(data.id, data.name))
