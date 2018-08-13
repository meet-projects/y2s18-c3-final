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
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        location = request.form['search']
        elders = get_elder_by_location(location)
        return render_template('search_results.html', elders=elders)

@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('log_in.html')

@app.route('/myaccount')
def myacc():
    return render_template('my_acount.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        if request.form['user_type'] == 'Elder':
            add_elder(request.form['full_name'],request.form['password'],request.form['Age'],request.form['location'],request.form['phone_number'],"",None)
        else:
            add_volunteer(request.form['full_name'],request.form['password'],request.form['Age'],request.form['location'],request.form['phone_number'],"")
    return render_template('sign_up.html')
# Running the Flask app
app.run(debug=True)
