from taxi_mang import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return owner.query.get(user_id)


class customer(db.Model):  # relationship not done yet
    customer_id = db.Column(db.Integer(), primary_key=True)
    f_name = db.Column(db.String(length=50), nullable=False)
    l_name = db.Column(db.String(length=50), nullable=False)
    contact_no = db.Column(db.String(length=50), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)



    def __repr__(self):  # magic method
        return f"customer('{self.customer_id}','{self.f_name}','{self.l_name}','{self.contact_no}','{self.gender}','{self.address}')"


class taxi(db.Model):  # relationship not done yet
    taxi_id = db.Column(db.Integer(), primary_key=True)
    taxi_type = db.Column(db.String(length=50), nullable=False)
    # driver_id = db.Column(db.String(length=50), nullable=False)
    registration_no = db.Column(db.String(length=50), nullable=False, unique=True)
    status = db.Column(db.String(length=10), nullable=False)
    price_per_km = db.Column(db.String(length=50), nullable=False)

    # foreign_key driver_id

    def __repr__(self):  # magic method
        return f"taxi('{self.taxi_id}','{self.taxi_type}','{self.registration_no}','{self.status}','{self.price_per_km}')"


class owner(db.Model, UserMixin):  # relationship not done yet
    owner_id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=50), nullable=False, unique=True)  # change to owner name ###
    contact_no = db.Column(db.String(length=50), unique=True, nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)

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
    f_name = db.Column(db.String(length=50), nullable=False)
    l_name = db.Column(db.String(length=50), nullable=False)
    contact_no = db.Column(db.String(length=50), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    # taxi_id = db.Column(db.Integer(),nullable=False)



    def __repr__(self):  # magic method
        return f"customer('{self.customer_id}','{self.f_name}','{self.l_name}','{self.contact_no}','{self.gender}','{self.address}')"

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
