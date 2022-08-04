from application import db

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_address = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(30), nullable=False)
    customer_book_order = db.relationship('Book_Order', backref='Customers')
    def __str__(self):
        return f"{self.customer_name}, {self.customer_address}, {self.customer_email}"

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    books_book_order = db.relationship('Book_Order', backref= 'Books')

    def __str__(self):
        return f"{self.book_name}, {self.genre}, {self.author}, {self.rating}"


class Book_Order(db.Model):
    bookorder_id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    
    
    def __str__(self):
        return f"{self.book_id}, {self.customer_id}, {self.order_date} ,{self.due_date}"

