#!/usr/bin/python3
"""
class definition of a State and an instance of Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
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
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
