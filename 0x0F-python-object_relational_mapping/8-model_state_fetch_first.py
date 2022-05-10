#!/usr/bin/python3
"""List the states."""
from statistics import StatisticsError
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
    Session.configure(bind=engine)
    session = Session()
    First = session.query(State).order_by(State.id).first()

    if First is not None:
        print("{}: {}".format(First.id, First.name))
    else:
        print('Nothing')
