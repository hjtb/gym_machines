from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField, TextAreaField, TextField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, IPAddress, NumberRange


class Login_form(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")
