"""Model for Shopify Inventory Tracking App."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    def __repr__(self):
        return f'<cat_id={self.cat_id} name={self.name}>'


    @classmethod
    def create_cat(self, first_name, last_name, gender, birthdate, phone_number, email, photo_id, appointment_type, time_checked_in):
        """Create and return a new cat to adopt."""
        patient = Cat(first_name=first_name,
                    last_name=last_name,
                    gender=gender, 
                    birthdate=birthdate, 
                    phone_number=phone_number, 
                    email=email, 
                    photo_id=photo_id, 
                    appointment_type=appointment_type,
                    time_checked_in=time_checked_in)

        return patient

    @classmethod
    def get_patients(self):
        return Patient.query.all()

    @classmethod
    def get_patient_by_id(self, patient_id):
        return Patient.query.get(patient_id)

    @classmethod
    def get_patient_by_email(self, email):
        return Patient.query.filter(Patient.email == email).first()
    
    @classmethod
    def get_patient_by_phone_number(self, phone_number):
        return Patient.query.filter(Patient.phone_number == phone_number).first()



def connect_to_db(flask_app, db_uri="postgresql:///med_appointments", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
