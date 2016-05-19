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
from amazon.api import AmazonAPI

#MODELS
###############################################################################

#data structure for a watch
class WatchListing(ndb.Model):
    Company = ndb.StringProperty()
    DisplayName = ndb.StringProperty()
    ReferenceNum = ndb.StringProperty()
    ItemId = ndb.StringProperty()
    Price = ndb.FloatProperty()
    ImageURL = ndb.StringProperty()

#creates and stores a new WatchListing in database
def createWatchListing(company,name,ref,itemid,price):
    watch = WatchListing(
        Company = company,
        DisplayName = name,
        ReferenceNum = ref,
        ItemId = itemid,
        Price = price,
        ImageURL = '/static/images/'+company+'/'+ref+'.jpg'
        )
    watch.put()
    return watch.key

#queries the NBD for all Watch Listings in datastore
def getWatchListing():
    query = WatchListing.query()
    watchList = []
    list = query.fetch()
    for item in list:
        temp = item.to_dict()   #strip off date property which is not easily parseable by json
        watchList.append(temp)
    return json.dumps(watchList)                  #return json representation of the ordered query

#queries the NBD for all Watch Listings in datastore, sorted by ascending or descending price
def getWatchListingsByPrice(bool):
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

#loads watches from text file into database as WatchListings. Time complexity is 1 second per watch due to Amazon API throttling
def loadTextFile():
    txt = open('watchlist.txt')
    amazon = AmazonAPI()
    list = []
    for line in txt:
        list.append(line.rstrip().split(','))

    for x in range(0,len(list),1):
            logging.warning("Watch Num: "+str(x))
            logging.warning(list[x][0])
            logging.warning(list[x][1])
            logging.warning(list[x][2])
            product = amazon.lookup(ItemId=list[x][2])
            logging.warning(product.price_and_currency[0])
            if (list[x][0] == 'Frederique Constant'):
                createWatchListing(
                list[x][0],
                list[x][1],
                list[x][1],
                list[x][2],
                product.price_and_currency[0])
            else:
                createWatchListing(
                list[x][0],
                list[x][0] + ' ' + list[x][1],
                list[x][1],
                list[x][2],
                product.price_and_currency[0])
            time.sleep(1) #amazon only allows a single API per second...
