import json
import logging
import os
import webapp2
import datetime
from datetime import date
import time
from google.appengine.ext import ndb
from google.appengine.api import memcache
from collections import OrderedDict

#MODELS
###############################################################################

#data structure for a watch
class WatchListing(ndb.Model):
    Company = ndb.StringProperty()
    WatchName = ndb.StringProperty()
    ReferenceNum = ndb.StringProperty()
    ItemId = ndb.StringProperty()
    Price = ndb.FloatProperty()

#creates and stores a new WatchListing in database
def createWallMessage(company,name,ref,itemid,price):
    watch = WallMessage(
        Company = company,
        WatchName = name,
        ReferenceNum = ref,
        ItemId = itemid,
        Price = price
        )
    watch.put()
    return watch.key

#queries the NBD for all Watch Listings in datastore
def getWallMessages():
    query = WatchListing.query()
    watchList = []
    list = query.fetch()
    for item in list:
        temp = item.to_dict()   #strip off date property which is not easily parseable by json
        watchList.append(temp)
    return json.dumps(watchList)                  #return json representation of the ordered query

#queries the NBD for all Watch Listings in datastore, sorted by ascending or descending price
def getWallMessagesByPrice(bool):
    if (bool == False):
        query = WatchListing.query().order(-WatchListing.price)
    else:
        query = WatchListing.query().order(WatchListing.price)
    watchList = []
    list = query.fetch()
    for item in list:
        temp = item.to_dict(exclude=['date'])   #strip off date property which is not easily parseable by json
        watchList.append(temp)
    return json.dumps(watchList)                  #return json representation of the ordered query

def loadTextFile():
    
