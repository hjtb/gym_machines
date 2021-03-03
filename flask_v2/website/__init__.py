
# This is inspired by the article here:
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
#

import platform
import os
import socket


from flask import Flask
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instantiate the migrate for initialisation with app and db later
# to create the files and folders in the first instance, you need to
# execute "flask db init" from the conda command window in the project top level directory
migrate = Migrate()

# set up the global login manager for initialisation with app later
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "warning"

# instantiate db for initialisation with app later
db = SQLAlchemy()

# create the holder for site config stuff
site_config = {}
site_config["platform"]= platform.system()
site_config["base_directory"] = os.path.abspath(os.path.dirname(__file__))
site_config["host_name"] = socket.gethostname()
site_config["environment"] = f'host:{site_config["host_name"]}, platform:{site_config["platform"]}'
site_config["FLASK_ENV"] = os.environ.get('FLASK_ENV') 

def create_app():
    # Create Flask application.
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    with app.app_context():   
        
        from website.models import User

        # now all the initiations
        db.init_app(app)
        migrate.init_app(app, db=db)
        login_manager.init_app(app)

        # create the user loader required for flask login 
        @login_manager.user_loader
        def load_user(user_id):
            user = User.query.filter(User.id == int(user_id)).first()
            return user

        # import the routes
        from website import routes

        # all is set up correctly so return the app  
        return app
