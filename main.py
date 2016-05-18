import logging
import os
import webapp2
import models
import time
import json
import sys

from google.appengine.api import mail
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
sys.path.insert(0, 'libs')
from lxml import objectify
from amazon.api import AmazonAPI

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
        if (models.WatchListing.query().count() == 0):
            models.loadTextFile()
        watchList = models.getWatchListing()
        page_params = {
            'list': watchList,
        }
        render_template(self, 'index.html',page_params)

###############################################################################
mappings = [
  ('/', MainPageHandler),
]
app = webapp2.WSGIApplication(mappings, debug=True)
