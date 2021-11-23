from flask_login import login_required, current_user, login_user, logout_user
#importing the flask_login dependicies for the authentication functionality

from flask import Blueprint, render_template, request
# importing flask itself for routing

auth = Blueprint('auth', __name__)
# creating the auth blueprint

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method =="POST":
        pass
    if request.method =="GET":
        return render_template('auth/login.html')
# login route with post and get request methods following the REST functionality