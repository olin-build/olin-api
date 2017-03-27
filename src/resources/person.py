""" Exists at `/people` and offers endpoints to conduct CRUD operations on a
database of Olin people """

from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse

# from .. import db

# Blueprint setup
people = Blueprint('people', __name__)
api = Api(people)

# Set up a parser
# parser = reqparse.RequestParser()

# parser.add_argument('data')
# parser.add_argument('a')
# parser.add_argument('c')


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
    def get(self):
        payload = request.args #[request.args[k] for k in request.args]
        return str(payload) #searchSomething(query)

    def put(self):
        return request.get_json()

    def post(self):
        return request.get_json()


# Resources
api.add_resource(DatabaseResource, '/') #url_prefix is registered as /people in src/app.py

