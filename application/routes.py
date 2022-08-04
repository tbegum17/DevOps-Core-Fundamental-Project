from application import app, db
from application.forms import *  
from application.models import *
from datetime import date, timedelta
from flask import request, redirect, url_for, render_template

@app.route('/')
@app.route('/Home')
def index():
    return render_template('layout.html')

@app.route('/book_form')
def view_books():
    form= BookForm()
    return render_template ('book_form.html', form=form)

@app.route('/bookorder_form')
def view_orders():
    form= BookOrderForm()
    return render_template ('bookorder_form.html', form=form)

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    form= BookForm()
    if form.validate_on_submit():
        book_name = form.book_name.data
        genre = form.genre.data
        author = form.author.data
        rating = form.rating.data
        new_book = Books(book_name=book_name, genre=genre, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('view_books'))
    return render_template('book_form.html', form=form)

@app.route('/customer_form')
def add_customer():
    return render_template ('customer_form.html')

@app.route('/create-customer', methods=['GET', 'POST'])
def create_new_customer():
    form= CustomerForm()
    if form.validate_on_submit():
        customer_name = form.customer_name.data 
        customer_address = form.customer_address.data
        customer_email = form.customer_email.data
        new_customer = Customers(customer_name=customer_name, customer_address=customer_address, customer_email=customer_email)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('view_all_customers'))
    return render_template('customer_form.html', form=form)

@app.route('/add_order', methods=['GET', 'POST'])
def add_new_order():
    form= BookOrderForm()
    if form.validate_on_submit():
        book_id = form.book_id.data
        customer_id = form.customer_id.data
        order_date = form.order_date.data
        due_date = form.due_date.data
        new_bookorder = Book_Order(book_id=book_id, customerid=customer_id, order_date=order_date,due_date=due_date,)
        db.session.add(new_bookorder)
        db.session.commit()
        return redirect(url_for('bookorder_form'))
    return render_template('bookorder_form.html')


@app.route('/view-customers')
def view_all_customers():
    customers = map(str,Customers.query.all())
    return '<br>'.join(customers)

@app.route('/view-books')
def view_all_books():
    books = map(str,Books.query.all())
    return '<br>'.join(books)


@app.route('/view-bookorder')
def view_all_bookorder():
    Book_Orders = map(str,Book_Order.query.all())
    return '<br>'.join(Book_Orders)


@app.route('/get-cust-by-name/<name>')
def view_custs_by_name(name):
    Customers = map(str, Customers.query.fliter_by(Customers.customer_name.like(f'%{name}')).all())
    return '<br>'.join(Customers)

@app.route('/get-cust-by-id/<int:id>')
def get_cust_by_id(id):
    customer = Customers.query.get(id)
    return str(customer)




