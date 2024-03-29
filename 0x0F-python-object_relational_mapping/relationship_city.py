#!/usr/bin/python3
"""
class definition of a State and an instance of Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sys import argv


class City(Base):
    """
    inherits from Base Tips
    links to the MySQL table states
    class attribute
    id that represents a column of an auto-gen, unique integer,
    cant be null and is primary key
    class attribute
    name that represents a column of a string with maximum 128
    characters and cant be null
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
