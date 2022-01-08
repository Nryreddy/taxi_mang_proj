from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    userid = StringField('Userid', validators=[DataRequired()])
    fname = StringField('F_name', validators=[DataRequired()])
    lname = StringField('L_name', validators=[DataRequired()])
    contactno = StringField('Contact_no', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
