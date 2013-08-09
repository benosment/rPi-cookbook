from cookbook import db, app
import sys
import os
import util

def usage():
  print """manage.py - provides management options for Flask app
              initdb - initialize database
              dbshell - shell for db 
              start - start the server
              deploy - kill existing server, copy files, start server
        """
  sys.exit(-1)

if __name__ == '__main__':
  # provide options for server management
  #  - initdb
  #  - dbshell
  #  - start
  #  - deploy TODO (send to rPi)
  if len(sys.argv) == 2:
    if sys.argv[1] == 'initdb':
      base_dir = os.path.abspath(os.path.dirname(__file__))
      # remove existing database
      os.remove(os.path.join(base_dir, 'cookbook.db'))
      # recreate tables
      db.create_all()
      # form path to recipes directory
      recipes_dir = os.path.join(base_dir, 'recipes')
      # populate_database with json recipes
      util.populate_database(recipes_dir)
    elif sys.argv[1] == 'dbshell':
      pass
    elif sys.argv[1] == 'start':
      app.run()
    elif sys.argv[1] == 'deploy':
      pass
    else:
      usage()
  else:
    usage()
