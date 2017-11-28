import os
from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route("/")

def main():
    
    return render_template('index.html') 
    
if __name__ == "__main__":
    #app.run()  # comment out
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))  # use for Cloud9


