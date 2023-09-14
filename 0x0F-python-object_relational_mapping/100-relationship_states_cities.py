#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost/{argv[3]}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    adds = State(name="California")
    addS = State(name="California")
    addC = City(name="San Francisco")
    addS.cities.append(addC)

    session.add(addS)
    session.add(addC)

    session.commit()
    session.close()
