from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from .models import owner,customer


class CustomerForm(FlaskForm):
    def validate_customername(self, username_to_check):
        customerr= customer.query.filter_by(username=username_to_check.data).first()
        if customerr:
            raise ValidationError('Username already exists! Please try add full name')

    customer_id = StringField(validators=[DataRequired()])
    f_name = StringField(validators=[DataRequired()])
    l_name = StringField(validators=[DataRequired()])
    contact_no = StringField(validators=[DataRequired()])  # recheck nno
    gender = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])

    submit = SubmitField('Sign_In')


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
    def validate_owername(self, username_to_check):
        ownerr= owner.query.filter_by(username=username_to_check.data).first()
        if ownerr:
            raise ValidationError('Username already exists! Please try add full name')

    user_name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField('Sign_In')
