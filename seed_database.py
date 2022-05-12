"""Script to seed database."""

import os

from model import Cat, Location, db, connect_to_db
import server

os.system("dropdb cats")
os.system("createdb cats")

connect_to_db(server.app)
db.create_all()


location1 = Location.create_location("Seattle")
location2 = Location.create_location("Los Angeles")
location3 = Location.create_location("San Francisco")

db.session.add(location1)
db.session.add(location2)
db.session.add(location3)
db.session.commit()
