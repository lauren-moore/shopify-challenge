"""Server for Cat Adoption Center app."""

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


@app.route("/add_cat", methods=["POST"])
def add_cat():
    """Create a new cat."""

    name = request.form.get("name")
    gender = request.form.get("gender")
    birthdate = request.form.get("birthdate")
    color = request.form.get("color")
    spay_or_neutor = request.form.get("spay_or_neutor")
    location = request.form.get("location")

    city = Location.get_location_by_city(location)

    #check if birthdate is correct length
    if len(birthdate) != 8:
        flash("Please enter 8 digits for birthdate as MMDDYYYY")
        return redirect('/')
    else:
        #create cat object in database
        new_cat = Cat.create_cat(name, 
                                gender, 
                                birthdate, 
                                color, 
                                spay_or_neutor, 
                                city)

        # db.session.add(new_cat)
        db.session.commit()
        flash(f"{new_cat.name} has been added to the {new_cat.location.city} Adoption Center!")

    return redirect('/')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
