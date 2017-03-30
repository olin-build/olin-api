from mongoengine import *
import os

try:
    from src.document_models import *
except:
    pass

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

def handle_get_request(docType, data):
    """
    data will vary based on request type. Criteria to select certain documents, documents to insert, data to change...
        In this case it'll be a dictionary with selection criteria {field1:value1, field2:value2}
    Some fields will be searchable by range (e.g. communityYear.) On the user side, they should be able to search for 
        ...&MINcommunityYear=2016&MAXcommunityYear=2018...
    We can then take those key value pairs {'MINcommunityYear':2016, 'MAXcommunityYear':2018} from args.
    Strip the MIN and MAX from the start of every string keys that begins with MIN or MAX to find out which field they're actually describing

    AND operators can probably be implemented by
    objects.find({ {field: {$gte:min, $lte:max}},
                   {field1: {comparator:value, co
mparator, other value}}
    })
    """
    queryDict = {}
    for key in data:
        if key[:3] == "MIN":
            temp = queryDict.get(key[3:],{})
            # print(temp)
            temp['$gte'] = data[key]
            queryDict[key[3:]] = temp
        elif key[:3] == "MAX":
            temp = queryDict.get(key[3:],{})
            temp['$lte'] = data[key]
            queryDict[key[3:]] = temp
        else:
            temp = queryDict.get(key,{})
            temp['$eq'] = data[key]
            queryDict[key] = temp
    return [thing.to_json() for thing in docType.objects(__raw__ = queryDict)]


def handle_post_request(docType, data):
    """
    docType is the type of document. data will be dictionary with key:value pairs corresponding to document fields. 
    """
    new_object = docType(**data)
    new_object.save()
    return new_object.to_json()

def test_wipe_add():
    """
    Tests collection dropping and insertion of documents.
    """
    Person.drop_collection()
    personDict = [
        {'fName':'Tim','lName':'Green', 'communityYear':'2015'},
        {'fName':'John','lName':'Blue', 'communityYear':'2015'},
        {'fName':'Abe','lName':'Smith', 'communityYear':'2016'},
        {'fName':'Suzy','lName':'Brown', 'communityYear':'2017'},
        {'fName':'Jane','lName':'Tan', 'communityYear':'2017'},
        {'fName':'Jane','lName':'Doe', 'communityYear':'2018'}
        ]

    people = [Person(fName = a['fName'],lName=a['lName'],communityYear=a['communityYear']) for a in personDict]
    for person in people:
        person.save()



if __name__ == "__main__":
    from document_models import *
    make_connection()
    test_wipe_add()

    print(handle_post_request(docType = Person, data={'fName':'Bob','lName':'Burger','communityYear':'2014'}))
    print([person.to_json() for person in Person.objects()])
    # print(handle_get_request(docType = Person, data={'communityYear':'2017'}))


### Unused Code ###


# from mongoengine.queryset.visitor import Q as multiQ

# def test_query(x):
#     """
#     Tests searching function and returns results.
#     """
#     query1 = multiQ(__raw__={'communityYear':{'$eq':'2015'}})
#     query2 = multiQ(__raw__={'lName':{'$eq':'Green'}})
#     query3 = multiQ(__raw__={'fName':{'$eq':'Jane'}})
#     query4 = multiQ(__raw__={'communityYear':{'$lte':'2017'}})
#     queryF = ((query1 & query2) | (query4 & query3))
#     print(queryF.__repr__)
#     querylist = [query1, query2, query3]
#     queryfinal = recursive_generate_query(querylist, 'or')
#     print(queryF.__repr__)
#     for person in x.objects(queryF):
#         print(person.to_json()) #this allows us to dump every variable at once.


# def recursive_generate_query(lst, andOr='and'):
#     """
#     lst is a list of multiQ objects. Can probably be optimized.
#     """
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         if andOr == 'and':
#             return lst[0] & recursive_generate_query(lst[1:], andOr='and')
#         elif andOr == 'or':
#             return lst[0] | recursive_generate_query(lst[1:], andOr='or')