#!/usr/bin/python3
"""prints the first State object from the database
"""
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

    instance = session.query(State).order_by(State.id).first()
    if instance:
        print(f'{instance.id:d}: {instance.name:s}')
    else:
        print('Nothing')

    session.close()
