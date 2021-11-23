from flask_login import LoginManager
# importing the flask_login library

from app.models import Users
# importing the users's model

from app import app
#importing the app variable

login_manager = LoginManager()
# instansiating the login_manager class

login_manager.init_app(app)
# initalising the login manager class and binding to the external application variable

login_manager.login_view = 'auth.login'
# login view redirector for the login_required decorator

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
# a function which is automatically called upon logging in user to fetch the user from the database