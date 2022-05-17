"""Script to seed database."""

import os
import model
import server

os.system("dropdb cats")
os.system("createdb cats")

model.connect_to_db(server.app)
model.db.create_all()

location1 = model.Location.create_location("Seattle")
location2 = model.Location.create_location("Los Angeles")
location3 = model.Location.create_location("San Francisco")

model.db.session.add(location1)
model.db.session.add(location2)
model.db.session.add(location3)
model.db.session.commit()