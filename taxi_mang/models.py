from enum import unique

from taxi_mang import db


class customer(db.Model):
    customer_id = db.Column(db.Integer(), primary_key=True)
    f_name = db.Column(db.String(length=50), nullable=False)
    l_name = db.Column(db.String(length=50), nullable=False)
    contact_no = db.Column(db.Integer(), unique=True, nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    password = db.Column(db.String(length=50), nullable=False)

    def __repr__(self):  # magic method
        return f"customer('{self.customerid}','{self.fname}','{self.lname}','{self.contactno}','{self.gender}','{self.address}')"


class taxi(db.Model):
    taxi_id = db.Column(db.Integer(), primary_key=True)
    taxi_type = db.Column(db.String(length=50), nullable=False)
    #driver_id =db.Column(db.String(length=50), nullable=False)
    registration_no = db.Column(db.String(length=50), nullable=False, unique=True)
    status = db.Column(db.String(length=10), nullable=False)
    price_per_km = db.Column(db.String(length=50), nullable=False)
    # foreign_key driver_id

    def __repr__(self):  # magic method
        return f"taxi('{self.taxi_id}','{self.taxi_type}','{self.registration_no}','{self.status}','{self.price_per_km}')"

