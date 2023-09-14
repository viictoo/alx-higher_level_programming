#!/usr/bin/python3
""" deletes all State objects with a name
containing the letter a from the database
"""
import sys
from sys import argv
from model_state import Base, State
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

    dels = session.query(State).filter(State.name.like('%a%')).all()
    for d in dels:
        session.delete(d)

    session.commit()
    session.close()
