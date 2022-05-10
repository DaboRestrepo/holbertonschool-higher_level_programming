#!/usr/bin/python3
"""This module soport the City class"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Contain the class definition of cities:
    Id: the city's identification
    name: City's name"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
