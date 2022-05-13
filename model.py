"""Model for Shopify Inventory Tracking App."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cat(db.Model):
    """A cat."""

    __tablename__ = 'cats'

    cat_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.String(8), nullable=False)
    color = db.Column(db.String, nullable=False)
    spay_or_neutor = db.Column(db.Boolean, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))

    location = db.relationship("Location", back_populates='cats')

    def __repr__(self):
        return f'<cat_id={self.cat_id} name={self.name}>'


    @classmethod
    def create_cat(self, name, gender, birthdate, color, spay_or_neutor, location):
        """Create and return a new cat to adopt."""
        cat = Cat(name=name,
                    gender=gender, 
                    birthdate=birthdate,  
                    color=color,
                    spay_or_neutor=spay_or_neutor,
                    location=location)

        return cat

    @classmethod
    def get_cats(self):
        return Cat.query.all()

    @classmethod
    def get_cat_by_id(self, cat_id):
        return Cat.query.get(cat_id)
    
    @classmethod
    def get_cat_by_name(self, name):
        return Cat.query.filter(Cat.name == name).first()




class Location(db.Model):
    """A location to adopt cats."""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)
    city = db.Column(db.String, nullable=False)

    cats = db.relationship("Cat", back_populates="location")

    def __repr__(self):
        return f'<location_id={self.location_id} city={self.city}>'


    @classmethod
    def create_location(self, city):
        """Create and return a new location to adopt cats."""
        location = Location(city=city)

        return location

    @classmethod
    def get_locations(self):
        return Location.query.all()

    @classmethod
    def get_location_by_id(self, location_id):
        return Location.query.get(location_id)
    
    @classmethod
    def get_location_by_city(self, city):
        return Location.query.filter(Location.city == city).first()


def connect_to_db(flask_app, db_uri="postgresql:///cats", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
