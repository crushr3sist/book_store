from app import app 
#importing the flask app variable to a file runner 

from app.views.shopRoutes import bookStoreRoutes
app.register_blueprint(bookStoreRoutes)
from app.views.login import login_manager
# importing the blueprint files 

if __name__ == "__main__":
    app.run()
# main file security implimentation
