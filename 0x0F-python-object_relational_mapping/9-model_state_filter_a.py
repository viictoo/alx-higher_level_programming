#!/usr/bin/python3
"""lists all State objects that contain the letter a
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
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%')
                                                ).order_by(State.id):
        print(f'{instance.id:d}: {instance.name:s}')

    session.close()
