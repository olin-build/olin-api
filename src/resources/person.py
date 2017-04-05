""" Exists at `/people` and offers endpoints to conduct CRUD operations on a
database of Olin people """

from flask import Blueprint, request
from flask_restful import Resource, Api
from src.document_models import Person
# from src.database_connection_mongoengine import handle_get_request

# Blueprint setup
people = Blueprint('people', __name__)
api = Api(people)


# http://flask.pocoo.org/docs/0.12/api/#flask.Request


class PersonEndpoint(Resource):
    """ Allows for querying, editing, and inserting people in the database """

    def get(self):
        """
        Returns one or more user objects

        Params:
            email       User's email address
            fName       First name of the user
            lName       Last name of the user
            comYearMIN  Minimum community year of the user (inclusive)
            comYearMAX  Maximum community year of the user (inclusive)
        """
        """
        we pull everything with db.query(all)? 
        Or query = Person.objects() and then 
        if params.get('fName'):
            query = query.filter(fName = params['fName'])
        if params.get('comYearMIN'):
            query = query.filter(comYear > int(params['comYearMIN']))

        and then at the end:
        return [person.to_json() for person in query]

        """
        params = request.args
        query = Person.objects()
        if params.get('fName'):
            query = query.filter(fName = params['fName'])
        if params.get('lName'):
            query = query.filter(lName = params['lName'])
        if params.get('email'):
            query = query.filter(email = params['email'])
        if params.get('comYearMIN'):
            query = query.filter(comYear__gte = int(params['comYearMIN']))
        if params.get('comYearMAX'):
            query = query.filter(comYear__lte = int(params['comYearMAX']))
        return [person.to_json() for person in query]

    def put(self):
        """
        If requests.json's fields do not match those defined in the Person model, this fails. 
        See documentation for src.document_models.Person for more details.
        """
        object = Person(**request.json) 
        object.save()
        return object.to_json()


    def post(self):
        params = request.args
        postQuery = Person.objects()
        if params.get('fName'):
            postQuery = postQuery.filter(fName = params['fName'])
        if params.get('lName'):
            postQuery = postQuery.filter(lName = params['lName'])
        if params.get('email'):
            postQuery = postQuery.filter(email = params['email'])
        if params.get('comYearMIN'):
            postQuery = postQuery.filter(comYear__gte = int(params['comYearMIN']))
        if params.get('comYearMAX'):
            postQuery = postQuery.filter(comYear__lte = int(params['comYearMAX']))
        postQuery.update(**request.json)
        return "Update Request Received"


# Resources
api.add_resource(PersonEndpoint, '/') #url_prefix is registered as /people in src/app.py
