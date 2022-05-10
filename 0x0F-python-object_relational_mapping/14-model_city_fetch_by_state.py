#!/usr/bin/python3
"""List the Cities and the States"""
from model_state import Base, State
from model_city import City
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
    print_all = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()
    for i, j in print_all:
        print("{}: ({}) {}".format(i.name, j.id, j.name))
