from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('data')
parser.add_argument('a')
parser.add_argument('c')


"""
I think we're sending a r(R?)equest over. 
The Resource then handles it and sends a Response back (it seems like it has to be a string). Maybe we can send json back?
"""
# http://flask.pocoo.org/docs/0.12/api/#flask.Request


def doSomething(query_dict):
    return sorted(query_dict)

def searchSomething(query):
    if True:
        try:
            return "Found something relating to " + str(query) + "!"
        except:
            pass
    return "Nothing was found."


class DatabaseResource(Resource):
    def get(self, query):
        return searchSomething(query)

    def put(self, query):
        args = parser.parse_args() #args is a dictionary of stuff sent over by the request.
        return "put request with args = " + str(args) + " and sorted args = " + str(doSomething(args))

    def post(self, query):
        args = parser.parse_args()
        return "post request with args = " + str(args) + "and sorted args = " + str(doSomething(args))


api.add_resource(DatabaseResource, '/<string:query>', '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) #not sure this will work
    if os.environ.get('MONGODB_URI'):
        import database_connection_mongo
        app.run(host='0.0.0.0', debug=True, port=port)
    else:
        app.run(host='127.0.0.1', debug=True, port=port)