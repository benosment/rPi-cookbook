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
 - add an option to manage.py to add all recipes 
 - move manage.py to argparse
 - add unit tests (mock?)
 - create a blank json recipe?
 - add 'deploy (send to rPi)' to manage.py
   - should find the rPi's IP address
   - ssh in
   - kill older flask servere
   - scp files, resources
   - start flask instance
   - (optimization) only copy files that have changed
 - add logging
 - move add recipe to it's own page 
 - make an index on the first page
 - have categories to display on the index

