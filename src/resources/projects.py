""" Exists at `/projects` and offers endpoints to conduct CRUD operations on a
database of Olin projects """

from flask import Blueprint
from flask_restful import Resource, Api, reqparse

from .. import db

# Blueprint setup
projects = Blueprint('projects', __name__)
api = Api(projects)

# Set up a parser
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


# Resources
api.add_resource(DatabaseResource, '/<string:query>')

