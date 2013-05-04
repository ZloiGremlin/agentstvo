import os
import sys
sys.path += ['/home/gremlin/webapps/agentstvo/agentstvo']
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'agentstvo.settings'
# activate_this = os.path.expanduser("~/webapps/agentstvo/env/bin/activate_this.py")
# execfile(activate_this, dict(__file__=activate_this))
application = WSGIHandler()