import logging
import os
import webapp2
import models
import time
import json

from google.appengine.api import mail
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template

###############################################################################
# We'll just use this convenience function to retrieve and render a template.
def render_template(handler, templatename, templatevalues={}):
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)

###############################################################################

#this class renders the homepage
class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'index.php')

###############################################################################
mappings = [
  ('/', MainPageHandler),
]
app = webapp2.WSGIApplication(mappings, debug=True)
