
#don't forget to turn the dyno back on!'


from bson import SON
import pymongo
import os
import json



"""
Usage:

1) user uses the 'requests' library to send olin-api a get/put/post request. 

    a) Put/post requests can have an additional data dictionary attached: we can parse that, as long as it uses keys we already know.

    b) What format should the users' queries be in? As long as it's standardized we can repackage it into mongo-executable BSON.
        i) Alternatively, have them compile their own BSON queries and send those over?


2) olin-api parses the request and passes it on to database_connection.

    a) There's probably information which is private to one or several users. How do we handle that?


3) database_connection interacts with a database accordingly. I think we just need one database with a bunch of different collections in it.

    a) For a single request:

        i)   Generate client
        ii)  Acquire the appropriate collections from one or more databases
        iii) Perform some operation on said databases
        iv)  Return something to olin-api
        v)   Close the client

    b) How are we setting up the database/collections? It seems like we could have all our collections in one database.

        i)   What if a user wants to search in multiple collections? mongoDB seems to support a left outer join between 2 collections with $lookup.
        ii)  Alternatively, only allow users to access one collection at once - 
             if they want to search for a user_id that appears in multiple collections, have them pull all the collections and check it themselves?
        iii) What type of data can pyMongo store? It seems to be a form of JSON called BSON. There might be easy date <-> json conversion in datetime.

    c) Can this process work if multiple users make requests at once?


4) olin-api receives a response from database_connection (3-a-iv) and sends it back to the user as a json response.


"""


def execute(database, collectionName, instruction):
    """
    Executes an instruction on a collection and returns a result to handle_request.
    We want to handle insert, find, replace and delete
        The insert operation needs a document to insert.
        Find, replace and delete need criteria to decide which documents to target.
    example instruction for insert = {'insert': stuff}, where stuff is an array of documents to insert
    example instruction for other operations = {'operationType':{'field1':{'$lt':'value1'}, 'field2':{$lt:'value2'}, 'field3':{'$lt':'value3'}} etc.
        I think mongoDB uses find({fieldName:{operator:value}}) to find documents where fieldName (operator) value is true.
        Operator list:
            $lt - less than
            $lte - less than or equal to
            $gt - greater than
            $gte - greater than or equal to
            $eq - equal to. Is equivalent to {fieldname:value}
            $ne - not equal to.
            $in - is in array. Usage: {fieldName:{'in':['value1', 'value2', 'value3'...]}}
            $nin - is not in array.

    instruction looks like 
    {'op':'update', 'data':(
                            {filter:value},
                            {action:actionValue}
                                                )}

    or 
    {'op':'find'/'delete', 'data':{'field':'value'}}
    or 
    {'op':'insert', 'data':[document1, document2]}
    
    """
    commandDict = {'insert': lambda x: database[collectionName].insert_many(x),          # requires a list of documents
                    'find': lambda x: database[collectionName].find(x, {'_id':False}), # requires a filter
                    'delete': lambda x: database[collectionName].delete_many(x),         # requires a filter
                    'update': lambda x: database[collectionName].update_many(x[0],x[1])  # requires a filter and actions to perform on matching documents
                    }

    operation = instruction['op'] #operation is 'find', 'update', 'insert' or 'delete'
    function = commandDict[operation]
    result = commandDict[operation](instruction['data'])
    if instruction['op']=='find':
        return [k for k in result]
    else:
        return result


    


    # exampleCommand = SON([
    #                         ('insert','collectionName'),
    #                         ('documents',[{'1':'2'},{'3':'4'}])
    #                         ])

    # exampleCommand2 = SON([
    #                         ('find','collectionName'),
    #                         ('filter',{'1':{'$gt':'1'}})
    #                         ])
    # #result = database.command(exampleCommand2) will make result a dictionary with 'first-batch':[document1, document2, document3 etc.]

    # #alternatively:
    # result2 = database[collectionName].find({'1':{'$gt':'1'}})
    # result2 returns a cursor instead of a dictionary, but performance-wise there shouldn't be much difference. 
    # Getting data out is as simple as [document for document in result2] - the difference is each operation has a different name.
    # db[cN].find(), db[cN].insert_many(), db[cN].update_many() etc. as opposed to db.command() which does everything inside. 
    # For our purposes (simple CRUD), we can read user instructions and then map those to different functions.
    # User queries will need to be wrapped up at some point, unless we want them to compile their own BSON queries and send those over.




def handle_request(requestLocation, instruction):
    """
    For now, only access to a single collection is supported. requestLocation is a ('databaseName','collectionName') tuple or list.
    Instruction is probably a {'find':['field_1=xx','field_2=yy'], 'sort':['field_3':'asc', 'field_4':'desc']} dictionary or something like that
    handle_request will be imported by olin-api and called when a user makes a request. It will return the results of 'execute' to be returned to the user. 

    Default database is 'test'. If we only ever want 1 database, we can take that out of requestLocation: users will only have to request collections.
    """
    if os.environ.get('MONGODB_URI'):
        uri = os.environ.get('MONGODB_URI')
    else:
        uri = 'mongodb://localhost:27017/'
    client = pymongo.MongoClient(uri)
    if len(requestLocation)>1:
        (databaseName,collectionName) = (requestLocation[0],requestLocation[1])
        database = client[databaseName]
    else:
        database = client['test']
        collectionName = requestLocation
    result = execute(database, collectionName, instruction)
    client.close()
    return result



if __name__ == '__main__':
    requestLocation = ('test','test-collection')
    clear = handle_request(requestLocation, {'op':'delete', 'data':{}})
    a = handle_request(requestLocation,{'op':'insert', 'data':[{'1':'6'},{'1':'7'}]})
    b = handle_request(requestLocation,{'op':'insert', 'data':[{'1':'8'}]})
    c = handle_request(requestLocation,{'op':'find', 'data':{'1':{'$gt':'1'}}})
    d = handle_request(requestLocation,{'op':'update', 'data':({'1':{'$gt':'1'}},{'$set':{'secondfield':'test'}})})
    e = handle_request(requestLocation,{'op':'delete', 'data':{'1':{'$eq':'1'}}})


    print(json.dumps(c))