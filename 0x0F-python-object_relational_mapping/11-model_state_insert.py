#!/usr/bin/python3
"""adds the State object “Louisiana” to the database
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

    adds = State(name="Louisiana")
    session.add(adds)
    session.commit()

    print(f'{adds.id:d}')

    session.close()
