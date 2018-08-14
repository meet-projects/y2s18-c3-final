# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import get_all_elders, get_elder_by_location, get_all_volunteers, get_vol_by_elder, delete_all_elders, delete_all_vols, query_by_elder_name, add_elder, add_volunteer

# Starting the flask app
app = Flask(__name__)
app.secret_key= b'gh57658tsxyh'
# App routing code here
@app.route('/')
def home():
    '''if 'username' not in session:
        return render_template('log_in.html')'''
    return render_template('home.html')
def logout():
    session.RemoveAll()
    return render_template('log_in.html')
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
    if request.method == 'POST':
        name=request.form['username']
        password=request.form['password']
        eld=query_by_elder_name(name)
        if eld!=None:
            if password==eld.password:

                session['username'] = eld.username

                session['username']=eld.name
                session['password']=eld.password
                session['age']=eld.age
                session['location']=eld.location
                session['phone']=eld.phone
                session['id']=eld.id
                session['info']=eld.info
                session['vol_id']=eld.volunteer_id

                a="<h1>Welcome</h1>"
                return render_template('home.html',a=a)
            else:
                return "<h1>Wrong Password</h1>"
        else:
            return "<h1>Wrong User Name</h1>"
    return render_template('log_in.html')


@app.route('/myaccount')
def myacc():
    eld = query_by_elder_name(session['username'])
    return render_template('my_acount.html', eld=eld)
@app.route('/myaccount')
def myacc():
    vol = query_by_vol_name(session['username'])
    return render_template('my_acount.html', eld=eld)
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    a=""
    if request.method=='POST':
        if request.form['user_type'] == 'Elder':
            if request.form['password']==request.form['confirm_password']:
                add_elder(request.form['full_name'],request.form['password'],
                request.form['Age'],request.form['location'],request.form['phone_number'],"",None)
            else:
                a="Passwords don't match"
        else:
            if request.form['password']==request.form['confirm_password']:
                add_volunteer(request.form['full_name'],request.form['password'],
                request.form['Age'],request.form['location'],request.form['phone_number'],"")
            else:
                a="Passwords don't match"
    return render_template('sign_up.html',a=a)
# Running the Flask app
app.run(debug=True)
