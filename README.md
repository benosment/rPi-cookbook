rPi-cookbook
============

Flask-based cookbook for use with Raspberry Pi


To install:

    $ sudo pip install Flask
    $ sudo pip install Flask-SQLAlchemy

TODO
----
 - add images to show_recipe.html
 - add images to index page (need some way to scale the images down? )
 - move recipes to json format
 - add an option to manage.py to add all recipes 
 - move manage.py to argparse
 - add unit tests (mock?)
 - add 'push (send to rPi)' to manage.py
   - should find the rPi's IP address
   - ssh in
   - kill older flask servere
   - scp files, resources
   - start flask instance
   - (optimization) only copy files that have changed
 - add 'bootstrap (init DB with some recipes)' to manage.py
 - add logging
 - move add recipe to it's own page 
 - make an index on the first page
 - have categories to display on the index

