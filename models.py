from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
import os
import json

db = SQLAlchemy()
migrate = Migrate()

# database_path = "postgresql://{}:{}@{}/{}".format('postgres','9048','localhost:5432', 'capstone')

database_path = os.getenv('DATABASE_URL')

if not database_path:
    database_path = "postgresql://postgres:9048@localhost:5432/capstone"


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.config["SQLALCHEMY_DATABASE_URI"]=database_path
    db.app=app
    migrate.init_app(app,db)
    db.init_app(app)
    db.create_all()


class Movies(db.Model):
    __tablename__='movie'
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String,nullable=False,unique=True)
    genres=db.Column(db.String, nullable=False)

    def __init__(self, title, genres):
        self.title = title
        self.genres=genres

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "genres": self.genres
        }


class Actors(db.Model):
    __tablename__='actor'
    id=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String, nullable=False, unique=True)
    age=db.Column(db.Integer, nullable=False)

    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age=age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "age": self.age
        }