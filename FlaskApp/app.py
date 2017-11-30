import os
import pandas as pd
from sqlalchemy import create_engine



file = '/Users/lunaambaye/CS_4420/Lost__found__adoptable_pets.csv'


print (pd.read_csv(file, nrows=5))

pets_database = create_engine('sqlite:///pets_database.db')


chunksize = 100000
i = 0
j = 1
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
      df.index += j
      i+=1
      df.to_sql('table', pets_database, if_exists='append')
      j = df.index[-1] + 1









"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '/Users/lunaambaye/Desktop/SQLAlchemy-1.1.15/lib/sqlalchemy/databases/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    
    def __repr__(self):
        return '<User %r>' % self.username     
"""

