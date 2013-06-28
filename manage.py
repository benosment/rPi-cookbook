from cookbook import db, app
import sys
import os
import settings

def usage():
  print """manage.py - provides management options for Flask app
              initdb - initial database
              dbshell - shell for db 
              start - start the server
        """
  sys.exit(-1)

if __name__ == '__main__':
  # provide options for server management
  #  - initdb
  #  - dbshell
  #  - start
  #  - push TODO (send to rPi)
  #  - bootstrap TODO (add some basic recipes)
  if len(sys.argv) == 2:
    if sys.argv[1] == 'initdb':
      basedir = os.path.abspath(os.path.dirname(__file__))
      os.remove(os.path.join(basedir, 'cookbook.db'))
      db.create_all()
    elif sys.argv[1] == 'dbshell':
      pass
    elif sys.argv[1] == 'start':
      app.run()
    else:
      usage()
  else:
    usage()
