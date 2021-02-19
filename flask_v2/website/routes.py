# Import relevant modules
import secrets
from sqlalchemy.exc import IntegrityError

from flask import Flask, request, render_template, url_for, redirect, flash

# Import the Flask webapp instance that we created in the __init__.py
from flask import current_app as app
from website import db

from website.gym_machines_v2 import gym_machines
from website.gym_machines_v2 import muscle_dictionary
from website.gym_machines_v2 import exercise_dictionary

from website.models import User
from website.models import Muscle
from website.models import Machine
from website.models import Exercise

# Define our first route (the last part of the url for our website application)
# We can define what urls should land in this function. Let's say / and /index
# We can also define the legitimate methods for this page of GET and POST


@app.route("/", methods=["GET", "POST"])
@app.route("/gym_machines_site_sql", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def gym_machines_site_sql():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    specific_machines = []
    muscle_from_form = ""
    
    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

        # create a for loop to loop through our machines to determine which machines can be used for the target muscle
        for gym_machine in gym_machines:
            for exercise, muscles in gym_machine["exercises"].items():
                muscle_from_form = form_package.get("muscle")[0]
                if muscle_from_form.lower() in muscles:
                    if gym_machine not in specific_machines:
                        specific_machines.append(gym_machine)
     

    return render_template (
        "gym_machines_site_sql.html",
        form_package=form_package,
        url_arguments=url_arguments,
        muscle_dictionary=muscle_dictionary,
        gym_machines=gym_machines,
        specific_machines=specific_machines,
        muscle_from_form=muscle_from_form,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

# Define our route (the last part of the url for our website application)
# We can define what urls should land in this function. Let's say / and /index
# We can also define the legitimate methods for this page of GET and POST
@app.route("/muscles_v2", methods=["GET", "POST"])

# Now comes the actual function definition for processing this page
def muscles_v2():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments = request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function
    # if the form was submitted
    # Create a default form_package in case the form not submitted
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

    return render_template(
        "muscles_v2.html",
        form_package=form_package,
        url_arguments=url_arguments,
        muscle_dictionary=muscle_dictionary,
        gym_machines=gym_machines,
        THIS_MACHINE=app.config["THIS_MACHINE"]
    )

# Define our route (the last part of the url for our website application)
# We can define what urls should land in this function. Let's say / and /index
# We can also define the legitimate methods for this page of GET and POST
@app.route("/exercises_v2", methods=["GET", "POST"])

# Now comes the actual function definition for processing this page
def exercises_v2():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments = request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function
    # if the form was submitted
    # Create a default form_package in case the form not submitted
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

    return render_template(
        "exercises_v2.html",
        form_package=form_package,
        url_arguments=url_arguments,
        muscle_dictionary=muscle_dictionary,
        exercise_dictionary=exercise_dictionary,
        gym_machines=gym_machines,
        THIS_MACHINE=app.config["THIS_MACHINE"]
    )


# Define our first route (the last part of the url for our website application)
# We can define what urls should land in this function. Let's say / and /index
# We can also define the legitimate methods for this page of GET and POST
@app.route("/machines_v2", methods=["GET", "POST"])

# Now comes the actual function definition for processing this page
def machines_v2():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments = request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function
    # if the form was submitted
    # Create a default form_package in case the form not submitted
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

    return render_template(
        "machines_v2.html",
        form_package=form_package,
        url_arguments=url_arguments,
        muscle_dictionary=muscle_dictionary,
        gym_machines=gym_machines,
        THIS_MACHINE=app.config["THIS_MACHINE"]
    )

@app.route("/manage_machines", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def manage_machines():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # Use sqlalchemy to query the machines table 
    sql = f"SELECT * FROM machines"
    machines = db.session.execute(sql)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    return render_template (
        "manage_machines.html",
        machines=machines,
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/manage_muscles", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def manage_muscles():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # Use sqlalchemy to query the muscles table 
    sql = f"SELECT * FROM muscles"
    muscles = db.session.execute(sql)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    return render_template (
        "manage_muscles.html",
        muscles=muscles,
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/add_muscle", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def add_muscle():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

        muscle = Muscle(name=form_package["name"][0], description=form_package["description"][0], image=form_package["image"][0])
        try:
            db.session.add(muscle)
            db.session.commit()
            flash(f"Just added {form_package['name'][0]}", category='success')

        except IntegrityError as err:
            flash(f"{form_package['name'][0]} already exists.", category='warning')
            db.session.rollback()

        except Exception as err:
            flash(f"Could not add muscle with name = {form_package['name'][0]}", category='warning')
            print(err)
            db.session.rollback()

        return redirect("manage_muscles")

    return render_template (
        "add_muscle.html",
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/edit_muscle", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def edit_muscle():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # set a try-except to ensure malicious sql injection will be handled correctly
    try:
        muscle_id = int(url_arguments["muscle_id"][0])
    except:
        print("The url has become corrupted")
        flash(f"The url has become corrupted", category='warning')
        return redirect("/")

    # query the muscles db to get info on selected muscle
    sql = f"SELECT * FROM muscles WHERE id = {muscle_id}"

    try:
        muscle_from_db = db.session.execute(sql).first()

    except:
        flash(f"could not select muscle with id = {muscle_id}", category='warning')

    form_package["name"] = muscle_from_db.name
    form_package["description"] = muscle_from_db.description
    form_package["image"] = muscle_from_db.image
    form_package["id"] = muscle_from_db.id

    print(f"You are in edit muscle, editing muscle with ID = {muscle_id}")

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

        id = int(form_package['id'][0])
        image = form_package['image'][0]
        description = form_package['description'][0]
        name = form_package['name'][0]

        sql = f"""
        UPDATE muscles 
        SET name = '{name}',
            description = '{description}',
            image = '{image}'
        WHERE id = {id}
        """

        try:
            muscles = db.session.execute(sql)
            db.session.commit()
            flash(f"Updated muscle with id = {muscle_id}", category='success')

        except IntegrityError as err:
            flash(f"{name} already exists.", category='warning')
            db.session.rollback()

        except Exception as err:
            flash(f"Could not update muscle with name = {name}", category='warning')
            print(err)
            db.session.rollback()

        return redirect("manage_muscles")

    return render_template (
        "edit_muscle.html",
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )


@app.route("/delete_muscle", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def delete_muscle():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")


    try:
        muscle_id = int(url_arguments["muscle_id"][0].strip())
    except:
        flash(f"The url has become corrupted", category='warning')
        return redirect("/")

    print(f"You are in delete muscle, deleting muscle with ID = {muscle_id}")

    sql = f"DELETE FROM exercises_muscles WHERE muscle_id = {muscle_id}"

    try:
        exercises = db.session.execute(sql)
        db.session.commit()
        flash(f"Deleted exercise-muscle relationships with muscle-id = {muscle_id}", category='success')

    except:
        flash(f"could not delete exercise-muscle relationship with id = {muscle_id}", category='warning')
        db.session.rollback

    sql = f"DELETE FROM muscles WHERE id = {muscle_id}"

    try:
        muscles = db.session.execute(sql)
        db.session.commit()
        flash(f"Deleted muscle with id = {muscle_id}", category='success')

    except:
        flash(f"could not delete muscle with id = {muscle_id}", category='warning')
        db.session.rollback
    return redirect("manage_muscles")

@app.route("/manage_exercises", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def manage_exercises():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # Use sqlalchemy to query the tables 
    sql = f"SELECT * FROM exercises"
    exercises = db.session.execute(sql)

    sql = f"""
        SELECT exercises.id AS exercise_id, exercises.name AS exercise_name, exercises_muscles.muscle_id, muscles.name AS muscle_name
        FROM exercises 
        LEFT JOIN exercises_muscles
        ON exercises.id = exercises_muscles.exercise_id
        LEFT JOIN muscles
        ON muscles.id = exercises_muscles.muscle_id;
    """
    exercises_data = db.session.execute(sql)

    sql = f"SELECT * FROM muscles"
    muscles = db.session.execute(sql)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    return render_template (
        "manage_exercises.html",
        exercises=exercises,
        exercises_data=exercises_data,
        muscles=muscles,
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/add_exercise", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def add_exercise():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    sql = f"SELECT * FROM muscles"
    muscles = db.session.execute(sql)

    sql = f"SELECT * FROM exercises_muscles"
    exercise_muscle = db.session.execute(sql)


    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

        exercise = Exercise(name=form_package["name"][0], description=form_package["description"][0])
        try:
            db.session.add(exercise)
            db.session.commit()
            flash(f"Just added {form_package['name'][0]}", category='success')
            sql = f'INSERT INTO exercises_muscles (exercise_id, muscle_id) VALUES'
            for muscle_id in form_package['muscle_ids']:
                muscle_id = int(muscle_id)
                sql = f'{sql} ({exercise.id}, {muscle_id}),'
            sql = f'{sql[0:-1]};'
            db.session.execute(sql)
            db.session.commit()

        except IntegrityError as err:
            flash(f"{form_package['name'][0]} already exists.", category='warning')
            db.session.rollback()

        except Exception as err:
            flash(f"Could not add exercise with name = {form_package['name'][0]}", category='warning')
            print(err)
            db.session.rollback()

        return redirect("manage_exercises")

    return render_template (
        "add_exercise.html",
        muscles=muscles,
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/edit_exercise", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def edit_exercise():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # set a try-except to ensure malicious sql injection will be handled correctly
    try:
        exercise_id = int(url_arguments["exercise_id"][0])
    except:
        print("The url has become corrupted")
        flash(f"The url has become corrupted", category='warning')
        return redirect("/")

    # query the db to get the muscles table
    sql = f"SELECT * FROM muscles"
    muscles = db.session.execute(sql)

    # query the db to get the exercises_muscles table
    sql = f"SELECT * FROM exercises_muscles"
    exercise_muscle = db.session.execute(sql)

    # query the exercises db to get info on selected exercise
    sql = f"SELECT * FROM exercises WHERE id = {exercise_id}"

    try:
        exercise_from_db = db.session.execute(sql).first()

    except:
        flash(f"could not select exercise with id = {exercise_id}", category='warning')

    form_package["name"] = exercise_from_db.name
    form_package["description"] = exercise_from_db.description
    form_package["id"] = exercise_from_db.id

    print(f"You are in edit exercise, editing exercise with ID = {exercise_id}")

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")

        id = int(form_package['id'][0])
        description = form_package['description'][0]
        name = form_package['name'][0]

        try:
            sql = f'INSERT INTO exercises_muscles (exercise_id, muscle_id) VALUES '
            for muscle_id in form_package['muscle_ids']:
                muscle_id = int(muscle_id)
                sql = f'{sql} ({exercise.id}, {muscle_id}),'
            sql = f'{sql[0:-1]};'
            db.session.execute(sql)
            db.session.commit()
            flash(f"Just edited {form_package['name'][0]}", category='success')

        except IntegrityError as err:
            flash(f"{form_package['name'][0]} already exists.", category='warning')
            db.session.rollback()

        except Exception as err:
            flash(f"Could not edit relational db entry with exercise id = {form_package['id'][0]}", category='warning')
            print(err)
            db.session.rollback()

        sql = f"""
        UPDATE exercises 
        SET name = '{name}',
            description = '{description}'
        WHERE id = {id}
        """

        try:
            exercises = db.session.execute(sql)
            db.session.commit()
            flash(f"Updated exercise with id = {exercise_id}", category='success')

        except IntegrityError as err:
            flash(f"{name} already exists.", category='warning')
            db.session.rollback()

        except Exception as err:
            flash(f"Could not update exercise with name = {name}", category='warning')
            print(err)
            db.session.rollback()

        return redirect("manage_exercises")

    return render_template (
        "edit_exercise.html",
        muscles=muscles,
        form_package=form_package,
        url_arguments=url_arguments,
        THIS_MACHINE=app.config["THIS_MACHINE"]
        )

@app.route("/delete_exercise", methods=["GET", "POST"])
# Now comes the actual function definition for processing this page
def delete_exercise():

    # Url arguments can be added to the url like this ?name=Peter&age=57
    # Get the url arguments if there are any
    url_arguments =  request.args.to_dict(flat=False)

    # if there are any url arguments, print them to the console here
    if len(url_arguments) > 0:
        print(f"\nThere were some url arguments and they were:\n{url_arguments}\n")

    # When pages contain a form, we can access the variables in this function 
    # if the form was submitted 
    # Create a default form_package in case the form not submitted 
    form_package = {}

    # And now check to see if the form was actually submitted
    if request.method == "POST":

        # pull the form fields into a dictionary for ease
        form_package = request.form.to_dict(flat=False)

        # print the form fields to the console so we can see it was submitted
        print(f"\nThe form was submitted. The data is:\n{form_package}\n")


    try:
        exercise_id = int(url_arguments["exercise_id"][0].strip())
    except:
        flash(f"The url has become corrupted", category='warning')
        return redirect("/")

    print(f"You are in delete exercise, deleting exercise with ID = {exercise_id}")

    sql = f"DELETE FROM exercises_muscles WHERE exercise_id = {exercise_id}"

    try:
        exercises = db.session.execute(sql)
        db.session.commit()
        flash(f"Deleted exercise-muscle relationships with exercise-id = {exercise_id}", category='success')

    except:
        flash(f"could not delete exercise with id = {exercise_id}", category='warning')
        db.session.rollback

    sql = f"DELETE FROM exercises WHERE id = {exercise_id}"

    try:
        exercises = db.session.execute(sql)
        db.session.commit()
        flash(f"Deleted exercise with id = {exercise_id}", category='success')

    except:
        flash(f"could not delete exercise with id = {exercise_id}", category='warning')
        db.session.rollback
    return redirect("manage_exercises")

    


# Now we can define a page to handle 404 errors
# 404 errors occur when we try to visit a page for
# which there is no route set up
@app.errorhandler(404)
def page_not_found(error):

    # We can do a very simple return of a text string
    # or we could do a full blown template
    # And we could include handling logic in this
    # route as well if we needed to
    return f"There was no such page. The error was - {error}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
