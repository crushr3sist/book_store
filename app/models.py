from app.__init__ import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, AnonymousUserMixin

class Users(AnonymousUserMixin, UserMixin, db.Model):
    __tablename__= "Users"

    id = db.Column(db.Integer(), primary_key = True)
    email = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    is_Admin = db.Column(db.Boolean())

    is_authenticated = False
    is_active = False
    is_anonymous = False

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.is_authenticated

    def __init__(self, email:str, username:str, password:str, name:str, is_Admin:bool):
        self.email =email 
        self.username = username
        self.password = password
        self.name = name
        self.is_Admin = is_Admin

class bookstore(db.Model):
    __tablename__= "bookstore"

    isbn         = db.Column(db.BIGINT() , nullable    = False, primary_key = True)
    name         = db.Column(db.String() , nullable    = False)
    author       = db.Column(db.String() , nullable    = False)
    date         = db.Column(db.String()   , nullable    = False) 
    description  = db.Column(db.String() , nullable    = False)
    picture      = db.Column(db.String() , nullable    = True, default = 'index.jpg')
    trade_price  = db.Column(db.BIGINT() , nullable    = False)
    retail_price = db.Column(db.BIGINT() , nullable    = False)
    quantity     = db.Column(db.BIGINT() , nullable    = False)

    def __init__(self,isbn :int,name :str,author:str,date:str,description:str,trade_price:int,retail_price:int,quantity:int) -> None:
        self.isbn = isbn
        self.name = name
        self.author = author
        self.date = date
        self.description = description
        self.picture = 'index.jpg'
        self.trade_price = trade_price
        self.retail_price = retail_price
        self.quantity = quantity