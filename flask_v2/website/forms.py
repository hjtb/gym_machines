from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField, TextAreaField, TextField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, IPAddress, NumberRange


class Login_form(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")

class Registration_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    user_age = IntegerField('Age', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')