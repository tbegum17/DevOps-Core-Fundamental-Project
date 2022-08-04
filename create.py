from application import db
from application.models import Customers, Books, Book_Order
from datetime import date

db.drop_all()
db.create_all()

customer1 = Customers(customer_name="Beverly Smith", customer_address="123 Fake St.", customer_email="bsmith@gmail.com", bookorder_id= "1")
customer2 = Customers(customer_name= "Tamanna Begum", customer_address="114 Imaginary Street", customer_email="tbegum32@outlook.com", bookorder_id= "2")
book1 = Books(book_name="A Good Girl's Guide To Murder", genre="Mystery, Thriller", rating="Young Adult", bookorder_id="1")
book2 = Books(book_name= "Heartstopper", genre="Romance", rating="Young Adult", bookorder_id="2")
book_order1 = Book_Order(book_id="1", customer_id="1", order_date=date(2022, 6, 10), due_date=date(2022, 3, 24))
book_order2 = Book_Order(book_id="2", customer_id="2", order_date=date(2022, 6, 17), due_date=date(2022, 6, 31))
db.session.add(customer1)
db.session.add(customer2)
db.session.add(book1)
db.session.add(book2)
db.session.add(book_order1)
db.session.add(book_order2)
