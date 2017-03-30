import os

from src.database_connection_mongoengine import make_connection, handle_get_request, handle_post_request

make_connection()

def database_get(docType, data):
    """
    wrapper function for handle_get_request.
    """
    return handle_get_request(docType, data)

def database_post(docType, data):
    return handle_post_request(docType, data)

### Unused Code ###

# import pymongo

# def make_client(uri):
#     return pymongo.MongoClient(uri)

# def connect_database(database_name):
#     client = make_client()
#     return client[database_name]

# uri = os.environ.get('MONGODB_URI')
# db = make_client(uri)
