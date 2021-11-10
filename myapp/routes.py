from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect, request
from myapp import db
from myapp.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/", methods = ['GET','POST'])
def home():
    name = 'Khuong'
    title = 'Top Cities'
    top_cities = User.query.all()
    form = TopCities()
    if request.method == 'GET':
        return render_template("home.html", name=name, title=title, top_cities=top_cities, form=form)
    if request.method == 'POST':
        if not request.form ['city_name'] or not request.form ['city_rank']:
            flash('Type in city_name and city_rank')
        else:
            cities = User(city_name = form.city_name.data, city_rank = form.city_rank.data)
            db.session.add(cities)
            db.session.commit()
            flash('New city was added!')
            return redirect('/')
 
    return render_template("home.html", name=name, title=title, top_cities=top_cities, form=form)

