"""Server for Cat Adoption Center app."""

# imports
from flask import Flask, render_template, request, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from model import Cat, Location, connect_to_db, db
from jinja2 import StrictUndefined


# initializing Flask app
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    cats = Cat.get_cats()
    locations = Location.get_locations()

    return render_template("homepage.html",
                            cats=cats,
                            locations=locations)


@app.route("/add_cat", methods=["POST"])
def create():
    """Create a new cat."""

    name = request.form.get("name")
    gender = request.form.get("gender")
    birthdate = request.form.get("birthdate")
    color = request.form.get("color")
    spay_or_neuter = request.form.get("spay_or_neuter")
    location = request.form.get("location")

    city = Location.get_location_by_city(location)

    #create new location if not in database
    if not city:
        city = Location.create_location(location)
        db.session.add(city)

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
                                spay_or_neuter,
                                city)

        db.session.add(new_cat)
        db.session.commit()   


    flash(f"{new_cat.name} has been added to the {new_cat.location.city} Adoption Center!")

    return redirect('/')


@app.route("/update/<int:cat_id>", methods=["POST"])
def update(cat_id):
    """Update cat info."""

    cat_to_update = Cat.get_cat_by_id(cat_id)
    new_spay_or_neuter = request.form.get("new_spay_or_neuter")
    cat_to_update.spay_or_neuter = new_spay_or_neuter
    db.session.commit()

    return redirect('/')


@app.route("/delete/<int:cat_id>", methods=["POST"])
def delete(cat_id):
    """Delete cat from database."""

    cat_to_delete = Cat.get_cat_by_id(cat_id)

    db.session.delete(cat_to_delete)
    db.session.commit()

    return redirect('/')



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
