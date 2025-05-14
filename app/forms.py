from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import TextAreaField, SelectField, DateTimeField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    due_date = DateTimeField('Due Date', format='%Y-%m-%d %H:%M')
    priority = SelectField('Priority', choices=[(
        'Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    submit = SubmitField('Save Task')
