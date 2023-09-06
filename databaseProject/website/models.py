from . import db
from sqlalchemy.sql import func


class Miracle(db.Model):
    __tablename__ = 'miracles'
    id = db.Column(db.Integer, primary_key=True)
    saint_name = db.Column(db.String(40))
    gender = db.Column(db.String(10))
    hierarchy = db.Column(db.String(40))
    type_miracle = db.Column(db.String(40))
    agent_of_miracle = db.Column(db.String(40))
    method = db.Column(db.String(40))
    beneficiary = db.Column(db.String(40))
    resume = db.Column(db.String(200))
