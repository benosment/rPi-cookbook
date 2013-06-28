import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing
import settings
import time

app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)

class Recipe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  short_desc = db.Column(db.String(120))
  ingredients = db.Column(db.String(120))
  preparation_time = db.Column(db.String(20))
  directions = db.Column(db.String(120))
  num_portions = db.Column(db.Integer)
  source = db.Column(db.String(120))
  date_created = db.Column(db.String(120))
  date_updated = db.Column(db.String(120))
  # category/tag (many-to-one relationship)

  def __init__(self, title, short_desc, ingredients, 
               preparation_time, directions, num_portions, 
               source):
    self.title = title
    self.short_desc = short_desc
    self.ingredients = ingredients
    self.preparation_time = preparation_time
    self.directions = directions
    self.num_portions = num_portions
    self.source = source
    self.date_created = time.ctime()
    self.date_updated = time.ctime()
    # TODO notes
    # TODO pairs with
    # TODO possible sides

  def __repr__(self):
    return 'Recipe<%s>' % self.title


@app.route('/')
def show_recipes():
  recipes = Recipe.query.all()
  return render_template('show_recipes.html', recipes=recipes)

@app.route('/add', methods=['POST'])
def add_recipe():
  # group together all the form attributes 
  d = dict(title=request.form['title'],
           short_desc=request.form['short_desc'],
           ingredients=request.form['ingredients'],
           preparation_time=request.form['preparation_time'],
           directions=request.form['directions'],
           num_portions=request.form['num_portions'],
           source=request.form['source'],
           )
  recipe = Recipe(**d)
  db.session.add(recipe)
  db.session.commit()
  flash('New recipe was successfully posted')
  return redirect(url_for('show_recipes'))

## TODO -- need a show_recipe (shows all details
