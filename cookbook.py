## Ben Osment
## Fri Aug  9 12:02:00 EDT 2013
## cookbook.py
"""
Main flask app
"""
from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import settings
import time
import json

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

  def __init__(self, param_dict):
    self.d = param_dict
    self.title = param_dict['title']
    self.short_desc = param_dict['short_desc']
    self.ingredients = "\n".join(param_dict['ingredients'])
    self.preparation_time = param_dict['preparation_time']
    self.directions = "\n".join(param_dict['directions'])
    self.num_portions = param_dict['num_portions']
    self.source = param_dict['source']
    self.date_created = time.ctime()
    self.date_updated = time.ctime()
    self.img_link = param_dict['img_link']
    # TODO notes
    # TODO pairs with
    # TODO possible sides


  def store_json(self):
    filename = self.title
    filename = filename.lower()
    filename = filename.replace(' ', '_')
    filename = filename.replace('-', '_')
    filename = filename.replace('/', "")
    filename = 'recipes/' + filename + ".json"
    with open(filename, 'w') as f:
        f.write(json.dumps(self.d, indent=4, separators=(',', ': ')))
    

  def __repr__(self):
    return 'Recipe<%s>' % self.title


@app.route('/')
def show_recipes():
  recipes = Recipe.query.all()
  return render_template('show_recipes.html', recipes=recipes)

@app.route('/add', methods=['POST', 'GET'])
def add_recipe():
  if request.method == 'GET':
    return render_template('add_recipe.html')
  elif request.method == 'POST':    
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
    recipe = Recipe(d)
    recipe.store_json()
    db.session.add(recipe)
    db.session.commit()
    flash("New recipe was successfully posted")
  return redirect(url_for('show_recipes'))

@app.route('/recipe/<string:title>')
def show_recipe(title):
  recipe = Recipe.query.filter_by(title=title).first()
  return render_template('show_recipe.html', recipe=recipe)

@app.route('/static/images/<string:name>')
def images(name):
  return send_from_directory("static/images/", filename=name)
