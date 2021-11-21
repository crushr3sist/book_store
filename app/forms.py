from flask_wtf import FlaskForm
from wtforms import *

class BookStoreForm(FlaskForm):
    isbn         = IntegerField('isbn'),
    name         = StringField('name'),
    author       = StringField('author'),
    date         = DateField('date'),
    description  = TextAreaField('description'),
    picture      = StringField('picture'),
    trade_price  = IntegerField('trade_price'),
    retail_price = IntegerField('retail_price'),
    quantity     = IntegerField('quantity'),
    submit       = SubmitField('submit'),