from flask_login import LoginManager
from app.models import Users
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
