rPi-cookbook
============

Flask-based cookbook for use with Raspberry Pi


To install:

    $ sudo pip install Flask
    $ sudo pip install Flask-SQLAlchemy

TODO
----
 - move add recipe to it's own page 
 - add short names
   -> use recipe/orecchiette-carbonara-with-charred-brussels-sprouts instead
      of recipe/7
 - add images to index page (need some way to scale the images down? )
 - create a hRecipe -> json utility for recipes
 - move manage.py to argparse
 - add unit tests (mock?)
   - sorely needed
 - is there some way to validate if a file is valid json or not?
 - add 'deploy (send to rPi)' to manage.py
   - should find the rPi's IP address:
       
       arp-scan --interface=eth0 --localnet | grep b8:27:eb
       >>> 192.168.1.147	b8:27:eb:83:e4:34	(Unknown)
       
       ssh pi@192.168.1.147 (password raspberry)

   ---> can something similar be done with Twisted

   - ssh in
   - kill older flask server
   - scp files over, resources
   - start flask instance
   - (optimization) only copy files that have changed
 - add logging
 - have categories to display on the index
 - how to handle grouping (like main + sides) or references?
 - add full-text search
 - display by categories (breakfast, sides, fish), maybe this should
   be tags?
 - pull recipes from websites like BA
 - handle unicode properly
