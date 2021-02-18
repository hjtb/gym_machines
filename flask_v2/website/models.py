# When you make updates to the models in this file, you need to bring the database into synch with it
# open a terminal with the correct environment activated
# type: python -m  flask db migrate 
# 
# Then check the sql update statements in the script that was generated. 
# NB This is an important check, not a cursory glance!
# NB They might be wrong!
# 
# When you are confident they are correct, type: python -m flask db upgrade
# 
# The database is now updated to reflect this model file
# 

from datetime import datetime
from flask import current_app as app
from website import db
from sqlalchemy.sql import func 

exercises_muscles = db.Table('exercises_muscles',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'), primary_key=True),
    db.Column('muscle_id', db.Integer, db.ForeignKey('muscles.id'), primary_key=True)
)

class Muscle(db.Model):
    __tablename__ = 'muscles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    exercises = db.relationship("Exercise", secondary=exercises_muscles, backref="muscles_backref")

    
    def __repr__(self):
        return dict(id=self.id, name=self.name, description=self.description, image=self.image ) 


class Machine(db.Model):
    __tablename__ = 'machines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return dict(id=self.id, name=self.name, description=self.description) 


class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    #muscles_worked = db.Column(db.string(100), nullable=False)
    muscles = db.relationship("Muscle", secondary=exercises_muscles, backref="exercises_backref")

    def __repr__(self):
        return dict(id=self.id, name=self.name, description=self.description) 


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return dict(id=self.id, user_name=self.user_name, user_age=self.user_age) 




