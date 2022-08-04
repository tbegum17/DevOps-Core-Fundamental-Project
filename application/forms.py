from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField

class CustomerForm(FlaskForm):
    customer_name = StringField('Enter Name')
    customer_address = StringField('Enter Address')
    customer_email = StringField('Enter Email')
    submit = SubmitField('Enter')

class BookForm(FlaskForm):
    book_name = StringField('Enter Book Name')
    genre = StringField('Enter Genre')
    author = StringField('Enter Author')
    rating = StringField('Enter Rating')
    submit = StringField('Enter')

class BookOrderForm(FlaskForm):
    book_id = IntegerField('Enter Book ID')
    customer_id = IntegerField('Enter Customer ID')
    order_date = DateField('Enter Order Date')
    due_date = DateField('Enter Due Date')
