from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
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
  img_link = db.Column(db.String(120))
  # category/tag (many-to-one relationship)

  def __init__(self, title, short_desc, ingredients, 
               preparation_time, directions, num_portions, 
               source, img_link):
    self.title = title
    self.short_desc = short_desc
    self.ingredients = ingredients
    self.preparation_time = preparation_time
    self.directions = directions
    self.num_portions = num_portions
    self.source = source
    self.date_created = time.ctime()
    self.date_updated = time.ctime()
    self.img_link = img_link
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
           img_link=request.form['img_link'],
           )
  recipe = Recipe(**d)
  db.session.add(recipe)
  db.session.commit()
  flash('New recipe was successfully posted')
  return redirect(url_for('show_recipes'))

@app.route('/recipe/<int:id>')
def show_recipe(id):
  recipe = Recipe.query.filter_by(id=id).first()
  return render_template('show_recipe.html', recipe=recipe)

@app.route('/images/<string:name>')
def images(name):
  return send_from_directory("/home/ben/Dropbox/Code/Python/rPi-cookbook/resources/", name)