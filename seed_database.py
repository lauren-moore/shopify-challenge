"""Script to seed database."""

import os
import json
from random import choice, randint

import model
import server

os.system("dropdb cats")
os.system("createdb cats")

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open("data/movies.json") as f:
    movie_data = json.loads(f.read())

# Create cats
cats_in_db = []
for movie in movie_data:
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(cats_in_db)
model.db.session.commit()