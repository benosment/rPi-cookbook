from cookbook import db, app
import sys

def usage():
  print """manage.py - provides management options for Flask app
              initdb - initial database (and bootstrap?)
              dbshell - shell for db 
              start - start the server
        """
  sys.exit(-1)

if __name__ == '__main__':
  # provide options for server management
  #  - initdb
  #  - dbshell
  #  - start
  if len(sys.argv) == 2:
    if sys.argv[1] == 'initdb':
      db.create_all()
    elif sys.argv[1] == 'dbshell':
      pass
    elif sys.argv[1] == 'start':
      app.run()
    else:
      usage()
  else:
    usage()
