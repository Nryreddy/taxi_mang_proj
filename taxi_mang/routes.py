from taxi_mang import app
from flask import render_template
from taxi_mang.models import taxi

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/customerlogin')
def customer_login_page():
    return render_template('customer_login.html')


@app.route('/customerlogin/taxi')
def taxi_page():
    items = taxi.query.all()
    return render_template('taxi.html', items=items)


@app.route('/user')
def user_page():
    return 'hi user'


@app.route('/owner')
def owner_login_page():
    return render_template('owner_login.html')

# app.run('127.0.0.1', port = 5500)
