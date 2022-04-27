from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from nbformat import ValidationError
from grocery_app.models import User



class SignUpForm(FlaskForm):
  username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
  username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Log In')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if not user:
      raise ValidationError('No user with that username. Please try again.')
