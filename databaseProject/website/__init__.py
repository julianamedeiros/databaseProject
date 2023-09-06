from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cats'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/julia/databaseProject/instance/database.db'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app