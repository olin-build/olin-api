""" Exists at `/people` and offers endpoints to conduct CRUD operations on a
database of Olin people """

from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse
from .. import database_get, database_post
from src.document_models import Person
# from src.database_connection_mongoengine import handle_get_request

# Blueprint setup
people = Blueprint('people', __name__)
api = Api(people)


# http://flask.pocoo.org/docs/0.12/api/#flask.Request


class DatabaseResource(Resource):
    def get(self):
        # payload = request.args #[request.args[k] for k in request.args]
        # make_connection()
        # return payload
        return database_get(docType=Person, data=request.args)
        # return str(handle_get_request(docType=Person, data=request.args))

    def put(self):
        return request.get_json()

    def post(self):
        # return request.args
        return database_post(docType=Person, data=request.get_json())
        # return request.get_json()


# Resources
api.add_resource(DatabaseResource, '/') #url_prefix is registered as /people in src/app.py

