import webapp2
import models
import time
import logging
from google.appengine.ext import ndb
from amazon.api import AmazonAPI

class update_prices(webapp2.RequestHandler):
    def get(self):
        amazon = AmazonAPI()
        watches = models.get_db_watches()
        if watches:
            for WatchListing in watches:
                product = amazon.lookup(ItemId=WatchListing.ItemId)
                WatchListing.Price = product.price_and_currency[0]
                WatchListing.put()
                time.sleep(1) #amazon only allows a single API per second...
        return

mappings = [
  ('/tasks/update_prices', update_prices),
]

app = webapp2.WSGIApplication(mappings, debug=True)
