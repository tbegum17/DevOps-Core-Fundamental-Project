from flask import url_for 
from application import app, db
from application.models import *
from flask_testing import TestCase
from datetime import date

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-library.db',
            WTF_CSRF_ENABLED = False,
            DEBUG = True,
            SECRET_KEY = 'KSCBV DV VH D'
        )
        return app


    def setUp(self): # runs before each test
        db.create_all()
        customer3 = Customers(customer_name= "Krishnika V", customer_address="114 Fake Street", customer_email="krishv32@outlook.com")
        book3 = Books(book_name= "Shatter Me", genre="Dystopian", rating="Young Adult", author= "Thea Queen")
        book_order3 = Book_Order(book_id="3", customer_id="3", order_date=date(2022, 6, 17), due_date=date(2022, 6, 30))
        db.session.add(customer3)
        db.session.add(book3)
        db.session.add(book_order3)
        db.session.commit()

    def tearDown(self): # runs after every test
        db.session.remove()
        db.drop_all()

class TestHomeView(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'Stratford Library App', response.data)
    
    def test_get_customers(self):
        response = self.client.get(url_for('view_all_customers'))
        self.assert200(response)
        self.assertIn(b'Krishnika V', '114 Fake Street', 'krishv32@outlook.com', response.data)
    
    def test_get_books(self):
        response = self.client.get(url_for('view_all_books'))
        self.assert200(response)
        self.assertIn(b'Shatter Me', 'Dystopian', 'Young Adult', 'Thea Queen', response.data)
    
    def test_get_bookorder(self):
        response = self.client.get(url_for('view_all_bookorder'))
        self.assert200(response)
        self.assertIn(b'3', '3', date(2022, 6, 17), date(2022, 6, 30), response.data)
    

class TestPostRequests(TestBase):
    def test_post_add_customer(self):
        response = self.client.post(
            url_for('create_new_customer'),
            data = dict(
                customer_name = "Alice Oseman",
                customer_address = "24 Pixley Lane",
                customer_email = "aoseman@icloud.com",
            ),
        follow_redirects = True

        )

        self.assert200(response)
        self.assertIn(b'Alice Oseman', '24 Pixley Lane', 'aoseman@icloud.com')

    def test_post_add_book(self):
        response = self.client.post(
            url_for('add_book'),
            data = dict(
                book_name = "Warbreaker",
                genre = "Fantasy",
                author = "Brandon Sanderson",
                rating = "Young Adult",
            ),
        follow_redirects = True

        )

        self.assert200(response)
        self.assertIn(b'Warbreaker', 'Fantasy', 'Brandon Sanderson', 'Young Adult')
    
    def test_post_add_bookorder(self):
        response = self.client.post(
            url_for('add_new_order'),
            data = dict(
                book_id = "4",
                customer_id = "4",
                order_date= date(2022, 8, 4),
                due_date = date(2022, 8, 18),
            ),
        follow_redirects = True
             
        )

        self.assert200(response)
        self.assertIn(b'4', date(2022, 8, 4), date(2022, 8, 18))
    


