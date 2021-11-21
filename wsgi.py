from app import app
from app.views.shopRoutes import bookStoreRoutes
app.register_blueprint(bookStoreRoutes)
from app.views.login import login_manager
if __name__ == "__main__":
    app.run(debug=True)
