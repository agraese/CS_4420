import os
import pandas as pd
from flask import Flask, render_template
from sqlalchemy import create_engine
app = Flask(__name__)



@app.route("/")


def main():

   return render_template('index.html') 


file = '/Users/lunaambaye/CS_4420/Lost__found__adoptable_pets.csv'
file2 = '/Users/lunaambaye/CS_4420/Animal_Breed_Index.csv'

print (pd.read_csv(file, nrows=5))
print (pd.read_csv(file2, nrows=5))

pets_database = create_engine('sqlite:///pets_database.db')
bread_database = create_engine('sqlite:///bread_database.db')

chunksize = 100000
i = 0
j = 1
for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
      df.index += j
      i+=1
      df.to_sql('table', pets_database, if_exists='append')
      j = df.index[-1] + 1
for df in pd.read_csv(file2, chunksize=chunksize, iterator=True):
      df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
      df.index += j
      i+=1
      df.to_sql('table', bread_database, if_exists='append')
      j = df.index[-1] + 1


if __name__ == "__main__":
    app.run()  # comment out
    #app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))  # use for Cloud9




"""
@app.route("/")
app = Flask(__name__)
"""

"""
def main():
    
    return render_template('index.html') 
    
if __name__ == "__main__":
    app.run()  # comment out
    #app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))  # use for Cloud9

"""






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

