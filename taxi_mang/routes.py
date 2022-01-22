from taxi_mang import app, db
from flask import render_template, redirect, flash, url_for
from taxi_mang.models import taxi, owner, customer, driver, bookedtaxi, taxi_log
from taxi_mang.forms import RegisterForm, CustomerForm, ownerForm, DriverForm, BookTaxiForm, \
    CustomerRegisterForm, addTaxiForm
from flask_login import login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/owner_register', methods=['GET', 'POST'])
def owner_register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        owner_to_create = owner(owner_name=form.owner_name.data,
                                contact_no=form.contact_no.data,
                                gender=form.gender.data,
                                address=form.address.data,
                                password=form.password1.data)
        db.session.add(owner_to_create)
        db.session.commit()
        return redirect(url_for('owner_login_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('owner_register.html', form=form)


@app.route('/ownerlogin', methods=['GET', 'POST'])
def owner_login_page():
    form = ownerForm()
    if form.validate_on_submit():
        attempted_user = owner.query.filter_by(owner_name=form.owner_name.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            owner_id = attempted_user.owner_id
            flash(f'Successfully logged in as: {attempted_user.owner_name} (id-{attempted_user.owner_id})',
                  category='success')

            return redirect(url_for('owner_home', owner_id=owner_id))
        else:
            flash("Username and password didn't match! Please try again", category='danger')

    return render_template('owner_login.html', form=form)


@app.route('/ownerlogin/ownerhome/<owner_id>', methods=['GET', 'POST'])
def owner_home(owner_id):
    return render_template('owner_home.html', owner_id=owner_id)


@app.route('/ownerlogin/listcustomer', methods=['GET', 'POST'])
def list_customer_page():
    items = customer.query.all()
    return render_template('list_customers.html', items=items)


@app.route('/ownerlogin/listdrivers', methods=['GET', 'POST'])
def list_drivers_page():
    items = driver.query.all()
    return render_template('list_drivers.html', items=items)


@app.route('/ownerlogin/listtaxis', methods=['GET', 'POST'])
def list_taxi_page():
    items = taxi.query.all()
    return render_template('list_taxi.html', items=items)


@app.route('/ownerlogin/list_taxi_log', methods=['GET', 'POST'])
def list_taxi_log_page():
    items = taxi_log.query.all()
    return render_template('list_taxi_log.html', items=items)


@app.route('/ownerlogin/listbookedtaxis', methods=['GET', 'POST'])
def list_booked_taxi_page():
    items = bookedtaxi.query.all()
    return render_template('list_booked_taxi.html', items=items)


@app.route('/ownerlogin/adddriver/<owner_id>', methods=['GET', 'POST'])
def add_drivers_page(owner_id):
    form = DriverForm()
    if form.validate_on_submit():
        driver_to_create = driver(driver_name=form.driver_name.data,
                                  contact_no=form.contact_no.data,
                                  gender=form.gender.data,
                                  address=form.address.data, )
        db.session.add(driver_to_create)
        db.session.commit()
        driver_name = form.driver_name.data
        flash(f'Successfully added driver: {form.driver_name.data}', category='success')
        return redirect(url_for('add_taxi_page', owner_id=owner_id, driver_name=driver_name))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_driver.html', form=form)


@app.route('/ownerlogin/adddriver/addtaxi/<owner_id>/<driver_name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def add_taxi_page(owner_id, driver_name):
    form = addTaxiForm()
    if form.validate_on_submit():
        taxii = taxi(registration_no=form.registration_no.data,
                     taxi_type=form.taxi_type.data, From=form.From.data, To=form.To.data,
                     flag=0, owner_owner_id=owner_id, driver_driver_name=driver_name)
        db.session.add(taxii)
        db.session.commit()
        flash('The details of the Taxi has been added successfully!', category='success')
        return redirect(url_for('owner_home', owner_id=owner_id))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_taxi.html', form=form, driver_name=driver_name)


@app.route('/customer_register', methods=['GET', 'POST'])
def customer_register_page():
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        customer_to_create = customer(customer_name=form.customer_name.data,
                                      contact_no=form.contact_no.data,
                                      gender=form.gender.data,
                                      address=form.address.data,
                                      password=form.password1.data)
        db.session.add(customer_to_create)
        db.session.commit()
        return redirect(url_for('customer_login_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('customer_register.html', form=form)


@app.route('/customerlogin', methods=['GET', 'POST'])
def customer_login_page():
    form = CustomerForm()
    if form.validate_on_submit():
        attempted_customer = customer.query.filter_by(customer_name=form.customer_name.data).first()

        if attempted_customer and attempted_customer.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_customer)
            customer_id = attempted_customer.customer_id
            customer_name = attempted_customer.customer_name
            flash(
                f'Successfully logged in as: {attempted_customer.customer_name} (id-{attempted_customer.customer_id})',
                category='success')
            return redirect(url_for('customer_home', customer_id=customer_id, customer_name=customer_name))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('customer_login.html', form=form)


@app.route('/customerlogin/customer_home/<customer_id>/<customer_name>', methods=['GET', 'POST'])
def customer_home(customer_id, customer_name):
    return render_template('customer_home.html', customer_id=customer_id, customer_name=customer_name)


@app.route('/customerlogin/customer_home/previous_booking/<customer_id>', methods=['GET', 'POST'])
def history_taxi(customer_id):
    btaxis = bookedtaxi.query.filter_by(customer_customer_id=customer_id).all()
    return render_template('history_taxi.html', btaxis=btaxis)


@app.route('/customerlogin/customer_home/check/<customer_id>/<customer_name>', methods=['GET', 'POST'])
def check_taxi(customer_id, customer_name):
    taxii = taxi.query.filter_by(flag=0).all()
    results = [
        {"taxi_id": one.taxi_id,
         "registration_no": one.registration_no,
         "taxi_type": one.taxi_type,
         "From": one.From,
         "To": one.To,
         } for one in taxii]
    return render_template('check_taxi.html', customer_id=customer_id, customer_name=customer_name,
                           title='Check Availability', results=results)


@app.route(
    '/customerlogin/customer_home/check/booktaxi/<customer_id>/<customer_name>/<taxi_id>/<registration_no>'
    '/<taxi_type>/<From>/<To>', methods=['GET', 'POST'])
def booktaxi(customer_id, customer_name, taxi_id, registration_no, taxi_type, From, To):
    form = BookTaxiForm()
    if form.validate_on_submit():
        obj = taxi.query.filter_by(registration_no=registration_no).first()
        btaxi = bookedtaxi(taxi_taxi_id=taxi_id, registration_no=registration_no, taxi_type=taxi_type, From=From, To=To,
                           Bdate=form.Bdate.data,
                           Btime=form.Btime.data,
                           customer_customer_id=customer_id)
        obj.flag = 1
        db.session.add(btaxi)
        db.session.commit()
        flash('Thank You, your taxi has been booked !', category='success')
        return redirect(url_for('customer_home', customer_id=customer_id, customer_name=customer_name))
    return render_template('book_taxi.html', customer_id=customer_id, customer_name=customer_name, taxi_id=taxi_id,
                           registration_no=registration_no,
                           taxi_type=taxi_type, From=From, To=To, form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
