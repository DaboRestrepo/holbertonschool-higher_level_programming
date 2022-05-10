#!/usr/bin/python3
"""This module soport the State class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String


Base = declarative_base()


class State(Base):
    """Contain the class definition of the state:
    Id: Entry identification
    name: State's name"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
