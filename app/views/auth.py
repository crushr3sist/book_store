from flask_login import login_required, current_user, login_user, logout_user
from flask import Blueprint, render_template, request



auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method =="POST":
        pass
    if request.method =="GET":
        return render_template('auth/login.html')

# @auth.route('/register', methods = ['GET, POST'])
# def register():
#      if request.method =="POST":
#         pass
#     if request.method =="GET":
#         return render_template()
