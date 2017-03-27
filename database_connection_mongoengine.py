from mongoengine import *
from document_models import *
from mongoengine.queryset.visitor import Q as multiQ
import os


### Resources ###
# http://docs.mongoengine.org/


### Database Interaction ###

def make_connection(requestLocation=None):
    """
    Connects a user to a database on the mongoDB server.
    requestLocation is the name of the database the user wants to connect to, and is either None or a string.
    By default, a database has enough space for ~24000 collection namespaces.
    """
    if os.environ.get('MONGODB_URI'):
        uri = os.environ.get('MONGODB_URI')
    else:
        uri = 'mongodb://localhost:27017/'
    if not requestLocation:
        databaseName = 'test'
    else:
        databaseName = requestLocation
    connect(databaseName, host = uri) #is this global? It shouldn't be too much of a problem since we're running this once for each request.


def test_wipe_add():
    """
    Tests collection dropping and insertion of documents.
    """
    Person.drop_collection()
    personDict = [
        {'fName':'Tim','lName':'Green', 'communityYear':2015},
        {'fName':'Abe','lName':'Smith', 'communityYear':2016},
        {'fName':'Suzy','lName':'Brown', 'communityYear':2017},
        {'fName':'Jane','lName':'Doe', 'communityYear':2018}
        ]

    people = [Person(fName = a['fName'],lName=a['lName'],communityYear=a['communityYear']) for a in personDict]
    for person in people:
        person.save()

def test_query(x):
    """
    Tests searching function and returns results.
    """
    for person in x.objects(multiQ(__raw__={'communityYear':{'$eq':2016}}) | multiQ(__raw__={'lName':{'$eq':'Doe'}})):
        #print(person.fName)
        return person.to_json() #this allows us to dump every variable at once.


if __name__ == "__main__":
    make_connection()
    test_wipe_add()
    print(test_query(Person))