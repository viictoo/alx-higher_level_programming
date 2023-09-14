#!/usr/bin/python3
"""prints all State objects, and corresponding City objects,
contained in the database
"""
import sys
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(City).order_by(City.id).all():
        print(f'{instance.id:d}: {instance.name:s} -> {instance.state.name:s}')

    session.close()
