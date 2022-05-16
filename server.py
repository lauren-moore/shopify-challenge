"""Server for Cat Adoption Center app."""

# imports
from flask import Flask, render_template, request, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from model import Cat, connect_to_db, db
from jinja2 import StrictUndefined


# initializing Flask app
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    cats = Cat.get_cats()

    return render_template("homepage.html",
                            cats=cats)


@app.route("/add_cat", methods=["POST"])
def add_cat():
    """Create a new cat."""

    name = request.form.get("name")
    gender = request.form.get("gender")
    birthdate = request.form.get("birthdate")
    color = request.form.get("color")
    spay_or_neutor = request.form.get("spay_or_neutor")
    # location = request.form.get("location")

    # city = Location.get_location_by_city(location)

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
                                spay_or_neutor)

        db.session.add(new_cat)
        print("***************************************")
        print(new_cat)

        
        
    db.session.commit()    
    print(new_cat)
    flash(f"{new_cat.name} has been added to the Adoption Center!")

    return redirect('/')


@app.route("/delete/<int:cat_id>", methods=["POST"])
def delete(cat_id):
    """Delete cat from database."""

    cat_to_delete = Cat.get_cat_by_id(cat_id)
    print("*****************")
    print(cat_to_delete)

    # try:
    db.session.delete(cat_to_delete)
    print("*******after db delete**********")
    print(cat_to_delete)
    db.session.commit()
    return redirect('/')

    # except:
    #     flash("Cannot delete at this time.")
    #     return redirect('/')

@app.route("/cats")
def all_cats():
    """View all cats."""

    cats = Cat.get_cats()
    print(cats)

    return render_template("all_cats.html",
                            cats=cats)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
