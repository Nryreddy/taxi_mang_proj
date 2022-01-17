from taxi_mang import app, db
from flask import render_template, redirect, flash, url_for, request
from taxi_mang.models import taxi, owner, customer, driver, bookedtaxi
from taxi_mang.forms import RegisterForm, CustomerForm, ownerForm, DriverForm, BookTaxiForm, selectTaxiForm, \
    CustomerRegisterForm, addTaxiForm
from flask_login import login_user, logout_user, login_required, current_user


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

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('owner_register.html', form=form)


@app.route('/ownerlogin', methods=['GET', 'POST'])
def owner_login_page():
    form = ownerForm()
    if form.validate_on_submit():
        attempted_user = owner.query.filter_by(owner_name=form.owner_name.data).first()
        owner_id = attempted_user.owner_id
        # owner_id = owner.query(owner.owner_id).filter_by(owner.owner_name == attempted_user.owner_id).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Successfully logged in as: {attempted_user.owner_name} (id-{attempted_user.owner_id})',
                  category='success')

            return redirect(url_for('owner_home', owner_id=owner_id))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('owner_login.html', form=form)


@app.route('/ownerlogin/ownerhome/<owner_id>', methods=['GET', 'POST'])
def owner_home(owner_id):
    return render_template('owner_home.html', owner_id=owner_id)


@app.route('/ownerlogin/taxi', methods=['GET', 'POST'])
def taxi_owner_page():
    items = taxi.query.all()
    return render_template('add_taxi.html', items=items)


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


@app.route('/ownerlogin/listbookedtaxis', methods=['GET', 'POST'])
def list_booked_taxi_page():
    items = bookedtaxi.query.all()
    return render_template('list_booked_taxi.html', items=items)


@app.route('/ownerlogin/adddriver', methods=['GET', 'POST'])
def add_drivers_page():
    form = DriverForm()

    if form.validate_on_submit():
        driver_to_create = driver(driver_name=form.driver_name.data,
                                  contact_no=form.contact_no.data,
                                  gender=form.gender.data,
                                  address=form.address.data, )
        db.session.add(driver_to_create)
        db.session.commit()
        flash(f'Successfully added driver: {form.driver_name.data}', category='success')
        return redirect(url_for('owner_home'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_driver.html', form=form)


@app.route('/ownerlogin/addtaxi/<owner_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def add_taxi_page(owner_id):
    form = addTaxiForm()
    if form.validate_on_submit():
        taxii = taxi(registration_no=form.registration_no.data,
                     taxi_type=form.taxi_type.data, From=form.From.data, To=form.To.data,
                     flag=0, owner_owner_id=owner_id)  # ??????
        db.session.add(taxii)
        db.session.commit()
        flash('The details of the vehicle has been added successfully!')
        return redirect(url_for('owner_home', owner_id=owner_id))
    return render_template('add_taxi.html', form=form)


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

    if form.errors != {}:  # If there are not errors from the validations
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
            flash(f'Successfully logged in as: {attempted_customer.customer_name}', category='success')

            return redirect(url_for('customer_home'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('customer_login.html', form=form)


@app.route('/customerlogin/customer_home', methods=['GET', 'POST'])
def customer_home():
    return render_template('customer_home.html')


@app.route('/customerlogin/customer_home/check', methods=['GET', 'POST'])
def check_taxi():
    taxii = taxi.query.filter_by(flag=0).all()
    results = [
        {
            # "dname":one.dname,
            "taxi_id": one.taxi_id,
            "registration_no": one.registration_no,
            "taxi_type": one.taxi_type,
            "From": one.From,
            "To": one.To,
        } for one in taxii]
    return render_template('check_taxi.html', title='Check Availability', results=results)


@app.route('/customerlogin/customer_home/check/booktaxi/<taxi_id>/<registration_no>/<taxi_type>/<From>/<To>',
           methods=['GET', 'POST'])
def booktaxi(taxi_id, registration_no, taxi_type, From, To):
    form = BookTaxiForm()
    if form.validate_on_submit():
        obj = taxi.query.filter_by(registration_no=registration_no).first()
        cust_id = customer.query.filter_by(customer_name=form.yname.data).first()
        btaxi = bookedtaxi(registration_no=registration_no, taxi_type=taxi_type, From=From, To=To,
                           yname=form.yname.data,
                           Bdate=form.Bdate.data,
                           Btime=form.Btime.data)  ###   ,taxi_id=obj.taxi_id,customer_id=cust_id.customer_id)
        obj.flag = 1
        db.session.add(btaxi)
        db.session.commit()
        flash('Thank You, your taxi has been booked !')
        return redirect(url_for('customer_home'))
    return render_template('book_taxi.html', registration_no=registration_no, taxi_type=taxi_type, From=From, To=To,
                           form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
