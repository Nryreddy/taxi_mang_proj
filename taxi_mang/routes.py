from taxi_mang import app, db
from flask import render_template, redirect, flash, url_for, request
from taxi_mang.models import taxi, owner, customer, driver
from taxi_mang.forms import RegisterForm, CustomerForm, ownerForm, DriverForm
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


@app.route('/test')
def test_db():
    try:
        a = owner.query.all()
        print(a)
        return f'my db conneted{a}'
    except Exception as e:
        print('e')
        return f'my db not connect {e}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/customerlogin', methods=['GET', 'POST'])
def customer_login_page():
    form = CustomerForm()

    if form.validate_on_submit():
        customer_to_create = customer(customer_id=form.customer_id.data,
                                      f_name=form.f_name.data,
                                      l_name=form.l_name.data,
                                      contact_no=form.contact_no.data,
                                      gender=form.gender.data,
                                      address=form.address.data, )
        db.session.add(customer_to_create)
        db.session.commit()
        return redirect(url_for('taxi_page'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('customer_login.html', form=form)


@app.route('/customerlogin/taxi', methods=['GET', 'POST'])
def taxi_page():
    items = taxi.query.all()
    return render_template('taxi.html', items=items)


@app.route('/ownerlogin/taxi', methods=['GET', 'POST'])
def taxi_owner_page():
    items = taxi.query.all()
    return render_template('taxi.html', items=items)


@app.route('/ownerlogin/listcustomer', methods=['GET', 'POST'])
def list_customer_page():
    # items = customer.query.all()
    return render_template('list_customers.html')


@app.route('/ownerlogin/listdrivers', methods=['GET', 'POST'])
def list_drivers_page():
    # items = .query.all()
    return render_template('list_drivers.html')


@app.route('/ownerlogin/listdrivers', methods=['GET', 'POST'])
def list_taxi_page():
    items = taxi.query.all()
    return render_template('list_taxi.html', items=items)


@app.route('/ownerlogin/adddriver', methods=['GET', 'POST'])
def add_drivers_page():
    form = DriverForm()

    if form.validate_on_submit():
        driver_to_create = driver(driver_id=form.driver_id.data,
                                  f_name=form.f_name.data,
                                  l_name=form.l_name.data,
                                  contact_no=form.contact_no.data,
                                  gender=form.gender.data,
                                  address=form.address.data, )
        db.session.add(driver_to_create)
        db.session.commit()
        flash(f'Successfully added driver: {form.f_name.data} {form.l_name.data}', category='success')
        return redirect(url_for('owner_page'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_driver.html',form=form)


@app.route('/user')
def user_page():
    return 'hi user'


@app.route('/owner/ownerpage')
@login_required
def owner_page():
    return render_template('owner.html')


@app.route('/owner', methods=['GET', 'POST'])
def owner_login_page():
    form = ownerForm()

    if form.validate_on_submit():
        attempted_user = owner.query.filter_by(user_name=form.user_name.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Successfully logged in as: {attempted_user.user_name}', category='success')

            return redirect(url_for('owner_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('owner_login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        owner_to_create = owner(user_name=form.user_name.data,
                                contact_no=form.contact_no.data,
                                gender=form.gender.data,
                                address=form.address.data,
                                password=form.password1.data)
        db.session.add(owner_to_create)
        db.session.commit()
        return redirect(url_for('owner_login_page'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))