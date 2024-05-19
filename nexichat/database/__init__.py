from pymongo import MongoClient

import config

DAXXdb = MongoClient(config.MONGO_URL)
DAXX = DAXXdb["DAXXDb"]["DAXX"]


from .chatsdb import *
from .usersdb import *
