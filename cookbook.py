import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing
import settings

app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)

class Recipe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  ingredients = db.Column(db.String(120))
  # preparation_time = db.Column(db.String(20))
  # directions = db.Column(db.String(120))
  # num_portions = db.Column(db.Integer)
  # source = db.Column(db.String(120))
  # date_created = db.Column(db.String(120))
  # date_updated = db.Column(db.String(120))

  # category/tag (many-to-one relationship)

  # def __init__(self, title, ingredients, preparation_time,
  #              directions, num_portions, source, date_created,
  #              date_updated):
  #   self.title = title
  #   self.ingredients = ingredients
  #   self.preparation_time = preparation_time
  #   self.directions = directions
  #   self.num_portions = num_poritions
  #   self.source = source
  #   self.date_created = date_created
  #   self.date_updated = date_updated

  def __init__(self, title, ingredients):
    self.title = title
    self.ingredients = ingredients

  def __repr__(self):
    return 'Recipe<%s>' % self.title


@app.route('/')
def show_recipes():
  recipes = Recipe.query.all()
  return render_template('show_recipes.html', recipes=recipes)

@app.route('/add', methods=['POST'])
def add_recipe():
  recipe = Recipe(request.form['title'], request.form['ingredients'])
  db.session.add(recipe)
  db.session.commit()
  flash('New recipe was successfully posted')
  return redirect(url_for('show_recipes'))
