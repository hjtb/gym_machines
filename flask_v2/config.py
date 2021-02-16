# Use in conjucntion with a .env file
# format of the .env is plain text with lines as follows

import datetime
# Class-based Flask app configuration
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'),override=True)

class Config:
    # 
    # first the safe ones that we know the answer to
    # 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# The application entry point
    FLASK_APP = 'wsgi.py'
    # 
    # Now the secret and machine specific ones from environment variables - see .env
    # 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    THIS_MACHINE = os.environ.get('THIS_MACHINE')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    database_password = os.environ.get('database_password')
    # And the dependant on environment variables
    # We don't need the if statement
	# We left it here to show how you can create the database connection string based on the environment variable set in .env file

    if FLASK_ENV in ["development"]:
        db_username = "my_db_user"
        database = "my_db_schema"
        database_url = "127.0.0.1"

    if FLASK_ENV in ["production"]:
        db_username = "my_db_user"
        database = "hjtb$my_db_schema"
        database_url = "hjtb.mysql.eu.pythonanywhere-services.com"

    # Create the db connection string
    SQLALCHEMY_DATABASE_URI = (
        "mysql+mysqlconnector://"
        + db_username
        + ":"
        + database_password
        + "@"
        + database_url
        + "/"
        + database
    )

if __name__ == "__main__":

    # test to see that config is working 
    config = Config()
    keys = config.__dir__()
    for key in keys:
        if key[0:2] != "__":
            value = config.__getattribute__(key)
            if isinstance(value, str):
                print(f"key: {key}    value: {value}")
