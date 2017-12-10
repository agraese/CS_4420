from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class pets(db.Model):
    animal_id = db.Column('animal_id', db.Integer, primary_key = True)
    animal_breed = db.Column(db.String(50))
    animal_name = db.Column(db.String(50))
    animal_gender = db.Column(db.String(20))
    image = db.Column(db.String(300))
    record_type = db.Column(db.String(20))
    animal_type = db.Column(db.String(20))
    color = db.Column(db.String(20))

def __init__(self, animal_breed, animal_gender, image, record_type, animal_type, color):
    self.animal_breed = animal_breed
    self.animal_gender = animal_gender
    self.image = image
    self.record_type = record_type
    self.animal_type = animal_type
    self.color = color

@app.route('/')
def index():
    return render_template('index.html', pets = pets.query.all())

def seed():

    animal1 = pets( animal_breed='Golden Retriever', animal_gender='Female', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=PUBLIC&ID=1771998', record_type='Lost', animal_type='Dog', color='Unknown')
    db.session.add(animal1)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    seed()
    app.run(debug = True)