from flask_sqlalchemy import SQLAlchemy, sqlalchemy
#importing the library used for avoiding showing raw SQL code in the application

from flask import Flask, session
#importing approprite flask dependencies

from app.views.auth import auth
#importing the auth blueprint

def create_app():
# function used for portability of the application 
    appVar = Flask(__name__)
    # internal application variable

    appVar.register_blueprint(auth)
    # registering the auth blueprint 

    appVar.secret_key = "f47a99ebcf29c1db68e6bbe4906b0d064e289efa65a2796c57edd354f14f6605"
    # the secret key which the csrf tokens are encrypted through

    appVar.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/bookstore_records.sqlite3'
    # the location of the database

    appVar.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # enabled to ease the development of the database
    
    return appVar
    # allowing the application to access the modified internal flask application variable

app = create_app()
# creating a external application variable

with app.app_context():
# a loop checking for file modifications required to be read during request context outside within the app context 
    db = SQLAlchemy(app)
    # producing the db controling variable
    
    from app.models import * 
    #importing the created models
    
    db.create_all()
    # if already exist, it passses otherwise it produces the modification 
    
    db.session.commit()
    # writing to db