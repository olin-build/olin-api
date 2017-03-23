from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os
import database_connection_mongo
import requests
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

# parser.add_argument('requestLocation')
# parser.add_argument('instruction')
# parser.add_argument('op')
parser.add_argument('data')


"""
I think we're sending a r(R?)equest over. 
The Resource then handles it and sends a Response back (it seems like it has to be a string). Maybe we can send json back?
"""
# http://flask.pocoo.org/docs/0.12/api/#flask.Request


def do_something(queryDict):
    return sorted(queryDict)

def search_something(query):
    if True:
        try:
            return "Found something relating to " + str(query) + "!"
        except:
            pass
    return "Nothing was found."


class DatabaseResource(Resource):
    def get(self, query):
        return search_something(query)

    def put(self, query):
        args = parser.parse_args() #args is the dictionary of stuff sent over by the request. On the request side we send post(URL, data = args)
        #everything in args is a string!
        return "put request with args = " + str(args) + " and sorted args = " + str(do_something(args))

    def post(self, query):
        args = parser.parse_args()
        dataDict = json.loads(args.data)
        assert isinstance(dataDict,dict)
        result = database_connection_mongo.handle_request(dataDict['requestLocation'],dataDict['instruction'])
        try:
            return json.dumps([k for k in result])
        except:
            return str(result)
  


api.add_resource(DatabaseResource, '/<string:query>', '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) #not sure this will work
    if os.environ.get('MONGODB_URI'):
        app.run(host='0.0.0.0', debug=True, port=port)
    else:
        app.run(host='127.0.0.1', debug=True, port=port)