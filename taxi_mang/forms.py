from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from .models import owner, customer


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        ownerr = owner.query.filter_by(username=username_to_check.data).first()
        if ownerr:
            raise ValidationError('Username already exists! Please try a different username')
    owner_name = StringField('User Name', validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField('Create Account')


class ownerForm(FlaskForm):
    owner_name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Sign_In')


class CustomerRegisterForm(FlaskForm):
    def validate_customername(self, customername_to_check):
        customerr = customer.query.filter_by(customer_name=customername_to_check.data).first()
        if customerr:
            raise ValidationError('Username already exists! Please try add full name')
    customer_name = StringField(validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField('Create Account')


class CustomerForm(FlaskForm):
    customer_name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Sign_In')


class DriverForm(FlaskForm):
    driver_name = StringField(validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    submit = SubmitField('ADD')


class addTaxiForm(FlaskForm):
    taxi_type = StringField(validators=[DataRequired()])
    registration_no = StringField(validators=[DataRequired()])
    From = StringField(validators=[DataRequired()])
    To = StringField(validators=[DataRequired()])

    submit = SubmitField('ADD')


class BookTaxiForm(FlaskForm):
    Bdate = StringField('Date', validators=[DataRequired()])
    Btime = StringField('Time', validators=[DataRequired()])
    submit = SubmitField('Book Taxi')
