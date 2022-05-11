"""Server for medical appointment app."""

# imports
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import Cat, Location, db, connect_to_db
from jinja2 import StrictUndefined


db = SQLAlchemy()

# initializing Flask app
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
