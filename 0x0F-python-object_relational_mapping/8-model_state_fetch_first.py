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

    result = engine.execute("SELECT id, name\
                            FROM states\
                            ORDER BY id\
                            LIMIT 1;")
    for data in result:
        if result is not None:
            print("{}: {}".format(data.id, data.name))
        else:
            print('Nothing')
