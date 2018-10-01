from service_api.server import initialize_app, app
from service_api.database import reset_database

initialize_app(app)
with app.app_context():
   reset_database()
