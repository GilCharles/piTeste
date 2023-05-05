import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class UserForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)] )
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, max=100)])
    login = SubmitField('Login')

class StudentForm(FlaskForm):
    student_name = StringField('Nome do estudante', [validators.DataRequired(), validators.Length(min=3, max=100)])
    student_email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)])
    student_academic_id = StringField('RA', [validators.DataRequired(), validators.Length(min=1, max=10)])
    save = SubmitField('Salvar')
    