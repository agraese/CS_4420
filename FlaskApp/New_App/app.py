from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class pets(db.Model):
    animal_id = db.Column('animal_id', db.Integer, primary_key=True)
    animal_breed = db.Column(db.String(50))
    animal_name = db.Column(db.String(50))
    animal_gender = db.Column(db.String(20))
    image = db.Column(db.String(300))
    record_type = db.Column(db.String(20))
    animal_type = db.Column(db.String(20))
    color = db.Column(db.String(20))

def __init__(self, animal_name, animal_breed, animal_gender, image, record_type, animal_type, color):
    self.animal_name = animal_name
    self.animal_breed = animal_breed
    self.animal_gender = animal_gender
    self.image = image
    self.record_type = record_type
    self.animal_type = animal_type
    self.color = color

@app.route('/')
def index():
    return render_template('index.html', pets=pets.query.all())

@app.route('/narrow')
def narrow():
    type_search = request.args.get('type', None)
    #gender_search = request.args.get['gender']
    #aorl_search = request.args.get['aorl']

    result = pets.query.filter_by(animal_type=type_search)

    return render_template('index.html', pets=result)


def seed():

    animal1 = pets( animal_name='Izzy', animal_breed='Golden Retriever', animal_gender='Female', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=PUBLIC&ID=1771998', record_type='Lost', animal_type='Dog', color='Unknown')
    db.session.add(animal1)

    animal2 = pets(animal_name='Neko', animal_breed='Domestic Shorthair', animal_gender='Male', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=PUBLIC&ID=1778704', record_type='Lost', animal_type='Cat', color='Unknown')
    db.session.add(animal2)

    animal3 = pets(animal_name='Trixie', animal_breed='Jack Russel Terrier', animal_gender='Female', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=PUBLIC&ID=1783927', record_type='Lost', animal_type='Dog', color='Unknown')
    db.session.add(animal3)

    animal4 = pets(animal_name='Chewie', animal_breed='Shih Tzu / Havanese', animal_gender='Male', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=KING&ID=A427735', record_type='Adoptable', animal_type='Dog', color='Tricolor')
    db.session.add(animal4)

    animal5 = pets(animal_name='Tilly', animal_breed='Domestic Longhair', animal_gender='Female', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=KING&ID=A530641', record_type='Adoptable', animal_type='Cat', color='Dilute Tor')
    db.session.add(animal5)

    animal6 = pets(animal_name='Ollie', animal_breed='Chihuahua - Smooth Coated', animal_gender='Male', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=KING&ID=A537770', record_type='Adoptable', animal_type='Dog', color='Black / White')
    db.session.add(animal6)

    animal7 = pets(animal_name='Flounder', animal_breed='Domestic Shorthair', animal_gender='Male', image='http://www.petharbor.com/get_image.asp?RES=Detail&LOCATION=KING&ID=A543738', record_type='Adoptable', animal_type='Cat', color='Brn Tabby')
    db.session.add(animal7)
    db.session.commit()


if __name__ == "__main__":
    if database_exists('sqlite:///pets.sqlite3'):
        # app.run()
        app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080))) 
    else:
        db.create_all()
        seed()
        app.run()
