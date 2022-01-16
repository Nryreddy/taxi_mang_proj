from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from .models import owner, customer, driver


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        ownerr = owner.query.filter_by(username=username_to_check.data).first()
        if ownerr:
            raise ValidationError('Username already exists! Please try a different username')

    user_name = StringField('User Name', validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField('Create Account')


class ownerForm(FlaskForm):
    user_name = StringField(validators=[DataRequired()])
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
    driver_id = StringField(validators=[DataRequired()])
    driver_name = StringField(validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])

    submit = SubmitField('ADD')


class selectTaxiForm(FlaskForm):
    driver_name = StringField('Driver Name', validators=[DataRequired()])
    registration_no = StringField('Vehicle Number', validators=[DataRequired()])
    taxi_type = StringField('Vehicle Type', validators=[DataRequired()])
    From = StringField('From', validators=[DataRequired()])
    To = StringField('To', validators=[DataRequired()])
    submit = SubmitField('Add')


class BookTaxiForm(FlaskForm):
    yname = StringField('Customer Name', validators=[DataRequired()])
    Bdate = StringField('Date', validators=[DataRequired()])
    Btime = StringField('Time', validators=[DataRequired()])
    submit = SubmitField('Book Taxi')
