from flask import Flask, redirect, url_for, Blueprint, render_template, request
from sqlalchemy import or_, func

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_params = {
            'saint_name': request.form.get('saint_name'),
            'type_miracle': request.form.get('type_miracle'),
            'hierarchy': request.form.get('hierarchy')
        }
        return redirect(url_for('views.index', **search_params))
    else:
        return render_template('search.html')


@views.route('/index', methods=['GET'])
def index():
    from .models import Miracle
    from . import db
    
    saint_name = request.args.get('saint_name')
    type_miracle = request.args.get('type_miracle')
    hierarchy = request.args.get('hierarchy')

    miracles = Miracle.query
    if saint_name:
        miracles = miracles.filter_by(saint_name=saint_name)
    if type_miracle:
        miracles = miracles.filter_by(type_miracle=type_miracle)
    if hierarchy:
        miracles = miracles.filter_by(hierarchy=hierarchy)
    miracles = miracles.all()
    
    return render_template('index.html', miracles=miracles)


@views.route('/visualization')
def visualization():
    from .models import Miracle
    from . import db

    saints_data = db.session.query(Miracle.saint_name, func.count(Miracle.id)).group_by(Miracle.saint_name).all()

    saints_data_list = [(row.saint_name, row[1]) for row in saints_data]

    total_miracles = db.session.query(func.count(Miracle.id)).scalar()

    return render_template('visualization.html', total_miracles=total_miracles, saints_data=saints_data_list)
