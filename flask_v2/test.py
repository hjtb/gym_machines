from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets

# from sqlalchemy import text
import sqlalchemy

# We will start the web app running using the create_app function defined in __init__.py
# so import the function here
from website import create_app

# This is a proof of concept / demonstration module to show how to use
# database independent parameter passing into sql queries to avoid the
# risk of sql injection attacks


def test_sql_query_params():

    # incorporating sql parameters into a sql string using is a
    # bad practise as it is prone to sql injection attacks
    # Although we can try to sanitise the parameters before incorporating
    # them it is better to use the power of the database to achieve that
    # for us.
    # The following method demonstrates how to achieve that
    # It was inspired by this link:
    #     https://docs.sqlalchemy.org/en/14/core/tutorial.html#using-text

    # define the sql using the :key notation to indicate where the
    # substitution parameters are and give them a name
    # the : notation works across all supported db backends
    sql = """
        SELECT *
        FROM users
        where id >= :lower_limit  
        and id < :upper_limit
    """

    # define a dictionary with keys and values appropriate to the
    # substitution parameters in the sql
    query_parameters = dict(lower_limit="51", upper_limit="354")

    # convert the sql as string to a sqlalchemy text clause object
    # so that we can bind the parameters to it before the execute
    sql = sqlalchemy.text(sql)

    # now bind the parameters to the text clause object
    sql = sql.bindparams(**query_parameters)

    try:
        # now execute the text clause object with the bound parameters
        users = db.session.execute(sql)
        for user in users:
            print(f"The user id is {user.id}, the email is: {user.email}")
        you_can_break_here = True

    except Exception as err:
        print(err)

    return


def test_sql_insert_params():

    # define the sql using the :key notation to indicate where the
    # substitution parameters are and give them a name
    # the : notation works across all supported db backends
    sql = """
        insert into users 
        (user_name, user_age) 
        VALUES 
        (:user_name, :user_age)
    """

    # define a dictionary with keys and values appropriate to the
    # substitution parameters in the sql
    # The dict() method is often more convenient when creating dictionaries with
    # many key value pairs as it's easier to avoid typing errors
    query_parameters = [
        dict(
            user_name=f"delete_this_'{secrets.token_urlsafe(7)}@gmail.com",
            user_age=0,
        ),
        dict(
            user_name=f"delete_this_'{secrets.token_urlsafe(7)}@gmail.com",
            user_age=0,
        ),
    ]

    # convert the sql as string to a sqlalchemy text clause object
    # so that we can bind the parameters to it before the execute
    sql = sqlalchemy.text(sql)

    # Now loop over the parameters and add a new record each time
    for query_parameter in query_parameters:
        # now bind the parameters to the text clause object
        sql_bound = sql.bindparams(**query_parameter)

        try:
            # now execute the text clause object with the bound parameters
            add_roles = db.session.execute(sql_bound)
            db.session.commit()

        except Exception as err:
            print(err)

    # now just check that we have added some records that need deleting
    users = db.session.execute("select * from users")
    for user in users:
        print(f"The user id is {user.id}, the email is: {user.user_name}")

        
    return


def test_myql():

    # just checks that mySQL is up and accessible using sqlalchemy
    sql = "select * from users"
    try:
        results = db.engine.execute(sql)
        return True
    except Exception as err:
        print(f"There was no MySQL available. The error was {err}")
        return False


if __name__ == "__main__":

    # Get the app
    app = create_app()

    # create a context for the db to use then create the database object db linked to this app
    app.app_context().push()
    db = SQLAlchemy(app)

    # just a quick test to make sure that we have the db and app context sorted
    my_sql_is_available = test_myql()
    if not my_sql_is_available:
        # fall over because there is no point
        1 / 0

    # Now demo the sql query params in a select
    test_sql_query_params()

    # Now demo the sql query params in an insert
    test_sql_insert_params()


