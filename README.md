rPi-cookbook
============

Flask-based cookbook for use with Raspberry Pi


To install:

    $ sudo pip install Flask
    $ sudo pip install Flask-SQLAlchemy

TODO
----
 - add images to index page (need some way to scale the images down? )
 - create a hRecipe -> json utility for recipes
 - move manage.py to argparse
 - add unit tests (mock?)
 - add 'deploy (send to rPi)' to manage.py
   - should find the rPi's IP address
   - ssh in
   - kill older flask server
   - scp files over, resources
   - start flask instance
   - (optimization) only copy files that have changed
 - add logging
 - move add recipe to it's own page 
 - make an index on the first page
 - have categories to display on the index
 - how to handle grouping (like main + sides) or references?
 - add full-text search
 - display by categories (breakfast, sides, fish), maybe this should
   be tags?
 - pull recipes from websites like BA
 - handle unicode properly
