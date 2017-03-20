import pymongo

uri = os.environ.get('MONGODB_URI')

def make_client():
    return pymongo.MongoClient(uri)


def return_database(databaseName):
    client = make_client()
    return client[databaseName]

