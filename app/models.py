from app.__init__ import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, AnonymousUserMixin

# importing the required libraries for the models of the data base
class Users(AnonymousUserMixin, UserMixin, db.Model):
    # inheriting from pre-determined classes which allow for the libraries to insert thier functionality inside the database
    __tablename__ = "Users"
    # assigning table name
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    is_Admin = db.Column(db.Boolean())
    cart = db.Column(db.Integer(), nullable=True)
    # the approprite fields for the user's table

    is_authenticated = False
    is_active = False
    is_anonymous = False
    # flask login specific variables

    def get_id(self):
        return self.id

    # flask login id fetcher, it is a abstraction function

    def is_authenticated(self):
        return self.is_authenticated

    # another flask login abstraction function

    def __init__(
        self, email: str, username: str, password: str, name: str, is_Admin: bool
    ):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.is_Admin = is_Admin

    # the initalisite function for the table to create a new record without shell.
    #


class bookstore(db.Model):
    __tablename__ = "bookstore"
    # the bookstore table
    isbn = db.Column(db.BIGINT(), nullable=False, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    date = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    picture = db.Column(db.String(), nullable=True, default="index.jpg")
    trade_price = db.Column(db.BIGINT(), nullable=False)
    retail_price = db.Column(db.BIGINT(), nullable=False)
    quantity = db.Column(db.BIGINT(), nullable=False)
    # the required fields for the application

    def __init__(
        self,
        isbn: int,
        name: str,
        author: str,
        date: str,
        description: str,
        trade_price: int,
        retail_price: int,
        quantity: int,
    ) -> None:
        self.isbn = isbn
        self.name = name
        self.author = author
        self.date = date
        self.description = description
        self.picture = "static/index.jpg"
        self.trade_price = trade_price
        self.retail_price = retail_price
        self.quantity = quantity

    # the used to add a book record.
