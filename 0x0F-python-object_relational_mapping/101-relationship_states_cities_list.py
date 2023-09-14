#!/usr/bin/python3
"""
prints all State objects, and corresponding City objects,
contained in the database
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
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

    obj = session.query(State).order_by(State.id).all()
    for state in obj:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
