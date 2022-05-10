#!/usr/bin/python3
"""List the states."""
from multiprocessing import synchronize
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Delete some states using SQLAlchemy."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    update = session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session='fetch')
    session.commit()
