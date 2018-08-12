# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/login')
def login():
    return render_template('login.html')
# Running the Flask app
app.run(debug=True)
