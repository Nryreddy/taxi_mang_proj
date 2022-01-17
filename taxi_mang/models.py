from taxi_mang import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user_loader1(user_id):
    return owner.query.get(user_id)


@login_manager.user_loader
def user_loader2(customer_id):
    return customer.query.get(customer_id)


class customer(db.Model,UserMixin):  # relationship not done yet
    customer_id = db.Column(db.Integer(), primary_key=True)
    customer_name = db.Column(db.String(length=50), nullable=False,unique=True)
    contact_no = db.Column(db.String(length=50), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    # bookedtaxiiii = db.relationship('bookedtaxi', backref='customer', lazy=True)

    def __repr__(self):  # magic method
        return f"customer('{self.customer_id}','{self.customer_name}','{self.contact_no}','{self.gender}','{self.address}')"

    def get_id(self):
        return (self.customer_id)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)



# class bill(db.Model):  # relationship not done yet
#     bill_no = db.Column(db.Integer(), primary_key=True)
#     customer_id = db.Column(db.Integer(), nullable=False)  # fk  #####
#     f_name = db.Column(db.String(length=50), nullable=False)  # fk    ######
#     contact_no = db.Column(db.String(length=50), nullable=False)  # fk     ######
#     taxi_id = db.Column(db.Integer(), nullable=False)  # fk
#     total_amount = db.Column(db.Numeric, nullable=False)
#
#     def __repr__(self):  # magic method
#         return f"customer('{self.bill_no}','{self.customer_id}','{self.f_name}','{self.contact_no}','{self.taxi_id}','{self.total_amount}') "


class taxi(db.Model):  # relationship not done yet
    taxi_id = db.Column(db.Integer(), primary_key=True)
    taxi_type = db.Column(db.String(length=50), nullable=False)
    registration_no = db.Column(db.String(length=50), nullable=False, unique=True)
    From = db.Column(db.String(50), nullable=False)
    To = db.Column(db.String(50), nullable=False)
    flag = db.Column(db.Integer)
    # driver_id = db.Column(db.Integer(), db.ForeignKey('driver.driver_id'))
    owner_owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id'))
    # bookedtaxiiiii = db.relationship('bookedtaxi', backref='taxi', lazy=True)


    # foreign_key driver_id

    def __repr__(self):  # magic method
        return f"taxi('{self.taxi_id}','{self.taxi_type}','{self.registration_no}','{self.From}','{self.To}','{self.flag},'{self.owner_owner_id}')"


class owner(db.Model, UserMixin):  # relationship not done yet
    owner_id = db.Column(db.Integer(), primary_key=True)
    owner_name = db.Column(db.String(length=50), nullable=False, unique=True)  # change to owner name ###
    contact_no = db.Column(db.String(length=50), unique=True, nullable=False)
    gender = db.Column(db.String(length=50), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    taxiii = db.relationship('taxi', backref='owner', lazy=True)

    def __repr__(self):  # magic method
        return f"owner('{self.user_name}','{self.contact_no}','{self.gender}','{self.address}')"

    def get_id(self):
        return (self.owner_id)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class driver(db.Model):  # relationship not done yet
    driver_id = db.Column(db.Integer(), primary_key=True)
    driver_name = db.Column(db.String(length=50), nullable=False,unique=True)
    contact_no = db.Column(db.String(length=50), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    # taxiiii = db.relationship('taxi', backref='driver', lazy=True)
    # bookedtaxiiii= db.relationship('bookedtaxi', backref='driver', lazy=True)


    def __repr__(self):  # magic method
        return f"customer('{self.driver_id}','{self.f_name}','{self.l_name}','{self.contact_no}','{self.gender}','{self.address}')"


class bookedtaxi(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration_no = db.Column(db.String(50), index=True)
    taxi_type = db.Column(db.String(length=50), nullable=False)
    From = db.Column(db.String(50), index=True)
    To = db.Column(db.String(50), index=True)
    yname = db.Column(db.String(64), index=True)
    Bdate = db.Column(db.String(64), index=True)
    Btime = db.Column(db.String(64), index=True)
    # taxi_id = db.Column(db.Integer, db.ForeignKey('taxi.taxi_id'))
    # customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    # driver_id = db.Column(db.Integer(), db.ForeignKey('driver.driver_id'))

    def __repr__(self):
        return '<booktaxi{}>'.format(self.dname)

# from taxi_mang.models import db
# db.create_all()
# db.drop_all() - to clear all tables
# from taxi_mang.models import customer
# cm1 = customer(customer_id=789,f_name='nry',l_name='rdy',contact_no = 789456,gender='male',address='bengaluru',password='789456')
# cm2 = customer(customer_id=889,f_name='lry',l_name='pdy',contact_no = 899456,gender='male',address='bengaluru',password='789856')
# db.session.add(cm1)
#  db.session.add(cm2)
# db.session.commit()
# customer.query.all()
# ---> [customer('789','nry','rdy','789456','male','bengaluru'), customer('889','lry','pdy','899456','male','bengaluru')]
