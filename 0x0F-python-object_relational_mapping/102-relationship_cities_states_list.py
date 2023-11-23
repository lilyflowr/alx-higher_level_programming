#!/usr/bin/python3
"""Module that lists all City objects"""

import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    if cities:
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the sssion.
    session.close()
