from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask import Flask
from app.views.auth import auth
def create_app():
    appVar = Flask(__name__)
    appVar.register_blueprint(auth)

    appVar.secret_key = "f47a99ebcf29c1db68e6bbe4906b0d064e289efa65a2796c57edd354f14f6605"
    appVar.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/bookstore_records.sqlite3'
    appVar.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return appVar

app = create_app()

with app.app_context():
    db = SQLAlchemy(app)
    from app.models import * 
    db.create_all()
    db.session.commit()