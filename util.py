## Ben Osment
## Fri Aug  9 12:02:00 EDT 2013
## util.py
"""
Provides utility functions for recipes
"""

import os
import json
from cookbook import Recipe, db

def json_to_recipe(json_file):
  # read the json file in as a string
  with open(json_file, 'r') as f:
    s = f.read()
  # covert json file to a dictionary
  d = json.loads(s)
  # pass dictionary to constructor, add to db
  recipe = Recipe(d)
  db.session.add(recipe)
  db.session.commit()

  
def populate_database(directory):
  """ given a directory, add all json format recipes to a database """
  # how to exclude .~?
  for filename in os.listdir(directory):
    if filename.endswith('.json'):
      json_to_recipe(os.path.join(directory, filename))
  