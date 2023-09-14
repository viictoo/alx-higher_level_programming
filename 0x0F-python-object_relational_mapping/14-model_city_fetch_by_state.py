#!/usr/bin/python3
"""prints all City objects from the database
"""
import sys
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}',
                           pool_pre_ping=True)
    # create all tables
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print(f'{obj[0]}: ({obj[1]}) {obj[2]}')

    session.close()
