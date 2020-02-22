#! /usr/local/bin/python

import sys
sys.path.insert(0, "/var/www/FlaskApp")
sys.path.insert(0, "/var/www/FlaskApp/apps")
sys.path.insert(0, "/var/www/FlaskApp/static")
sys.path.insert(0,'/usr/local/lib/python3.7/site-packages')
sys.path.insert(0, "/usr/local/bin/")

import os
os.environ['PYTHONPATH'] = '/usr/local/bin/python'

from main import app as application
application = application.server