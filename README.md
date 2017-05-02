# olin-api

Olin-api seeks to provide programmatic access to a wide variety of Olin College digital resources. It is meant to provide the foundation for a variety of student-built applications to benefit the community.

# Getting Started

**First: read and understand the [Olin API Honor Code](HONOR-CODE.md).**

The `./bin/` directory contains a number of scripts which will help you get started:

 - `lint.sh` - lint the codebase to ensure quality
 - `test.sh` - run unit tests
 - `readthedocs.sh` - generate and serve the project's documentation
 - `run.sh` - run the project itself
 - `setUpEnv.sh` - installs dependencies for the project

## Quickstart

 First, make sure MongoDB is running and accepting connections. Then,

 `bin/setUpEnv.sh && bin/run.sh`

 Right now, configuration is stored both in `.env` and `instance/default_settings.py`. This is gross, and should be changed.


# API Components

### API Architecture

Data is stored in [MongoDB](https://www.mongodb.com/) and accessed by the various resources written in [flask](http://flask.pocoo.org/) via the [mongoengine](http://mongoengine.org/) connector. Each resource (people, auth, etc.) is linked to one or more corresponding mongoDB collections (Person, Token, Application, etc.).

Olin-api is hosted at `http://olin-api.herokuapps.com`. Accessing a sub-resource like `auth` is as simple as sending a request to `http://olin-api.herokuapps.com/auth/` and its endpoints!

### Authentication

 The authentication component allows for API users to prove that they own an email. Devlopers utilizing this component can then proceed with trust that the user controls the email account that they claim to be.

 The auth flow is as such:

1. POST request is issued to `/auth` containing an email address. The API returns a JSON Web Signature (JWS) token (referred to here as the "auth token") and sends an email to the specified email address containing another token (referred to here as the "validation token").

2. The user visits their email and clicks a link containing the validation token in the form `/auth/token/validate/<validation_token>`.

3. The API ensures that the validation token is correct, and if so marks the auth token as valid, allowing it to be used for 1 year. Any resource which is accessed with this auth token can assume that the requester is in fact in control of the email address they have validated.

The largest oddity here is that the API does not store auth tokens: since they are tamper-proof and self-expiring cryptographic tokens, they do not need to be checked against a secure database. The API merely stores a structure which contains an email and a "validated" flag indicating whether or not that email currently has a valid token.

Full authentication documentation can be found [here](AUTH.md).


### People

The `People` resources provides access to the `Person` collection in our mongoDB database. This lets users access data and metadata about Olin community members. Everything at Olin is done by people, so it’s probably valuable to keep some records!

We store Person documents in the mongoDB backend. Each Person document has a number of fields as follows:
```python
class Person(Document):
    """
    Represents a real, actual, honest-to-goodness person.

    Fields:
    fName           First Name. Required.
                    Takes a string with maximum length 240.
                    Example: "John"

    lName           Last Name. Required.
                    Takes a string with maximum length 240.
                    Example: "Smith"

    comYear         Community Year (year the person joined the olin community)
                    Not required, takes an integer.
                    Example: 2015

    email           Email. Required, takes a string.
                    Example: "JohnSmith@students.olin.edu"

    pronouns        Personal pronouns. Not required, takes a string.
                    Example: "He/Him/His"

    services        Other services associated with this person.
                    Not required, takes a dictionary.
                    Example: {"venmo":"jSmith50", "messenger":"Smithee"}

    """
    fName = StringField(max_length=240, required=True)
    lName = StringField(max_length=240, required=True)
    comYear = IntField()
    email = EmailField(max_length=100, required=True, unique=True, sparse=True)
    pronouns = StringField(max_length=100)
    preferredName = StringField(max_length=240)
    services = DictField()

    # TODO: other fields
    # add role at Olin
    # BOW students?
    # allergies/diet
    # image/gravatar
```

#### Requests

All URL endpoints are ‘/’. 

If python’s request module and its associated request methods are used, they return an object whose `.json()` method returns a nested dictionary with server response (whether the intended action succeeded, as well as other information like error messages) and results (the information provided by the server).

A `GET` request to `<app_url>/people/?<search_arguments>` lets a user search the `Person` collection in mongoDB, and returns a list of objects matching the search. It does this by  then filtering (with `.filter(field = value)`) the objects in the Person collection (`Person.objects`).

Currently, we support searches for Person documents that match a `fName`, `lName` and `email`, as well as Person documents whose `comYears` are larger than `comYearMIN` or smaller than `comYearMAX`. An example query is 
```python
get_request = get('http://olin-api.herokuapp.com/people/?fName=John&lName=Doe&comYearMIN=2015&comYearMAX=2016')
```
If the request is successful, `get_request.json()[‘results’]` will contain a list of objects matching the search.


A `POST` request to `<app_url>/people/` lets a user insert a new `Person` document into the collection by creating a new `Person` document, populating its fields with json data (included in the request) and calling the `.save()` method.

To do so, include the appropriate fields and values into the request’s json argument. If requests.json's fields do not match those defined in the Person model, this fails. An example query is: 
```python
post_request = post('http://olin-api.herokuapp.com/people/', json={'fName':'Abraham','lName':'Brown','comYear':2018, 'preferredName':'Abe', 'email':'AbeBrown@students.olin.edu'})
```

If the request is successful, `post_request.json()[‘results’]` will contain the created object.

A `PUT` request to `<app_url>/people/?<search_arguments>` lets a user edit a selection of Person documents based on an identical search criteria to the `GET` request. The fields and values in the `PUT` request's URL filter the collection just like the `GET` request, then `.update(**json)` updates the filtered collection in the appropriate manner. An example query is:
```python
put_request = put('http://olin-api.herokuapp.com/people/?comYearMIN=2018&comYearMAX=2018', json={'comYear':2019})
```
If the request is successful, `put_request.json()[‘results’]` will contain a list of edited objects.
