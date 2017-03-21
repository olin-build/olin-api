import os

import pymongo

def make_client(uri):
    return pymongo.MongoClient(uri)

def connect_database(database_name):
    client = make_client()
    return client[database_name]

uri = os.environ.get('MONGODB_URI')
db = make_client(uri)
