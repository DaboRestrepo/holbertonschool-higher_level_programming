#!/usr/bin/python3
"""List the states."""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """List the states by id, using SQLAlchemy."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    result = engine.execute("SELECT states.id, states.name\
                            FROM states\
                            ORDER BY states.id\
                            LIMIT 1;")
    for data in result:
        if result is None:
            print('Nothing')
        else:
            print("{}: {}".format(data.id, data.name))
