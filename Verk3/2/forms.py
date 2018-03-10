from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    productName = StringField('productName', validators=[DataRequired("You need to insert á product name")])
    submit = SubmitField('Search')