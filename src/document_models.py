""" Contains all of the mongoengine models for data held in mongo """
from mongoengine import Document, StringField, IntField, ListField, DictField, EmailField

class Person(Document):
    """
    Fields:
    fName           First Name. Required, takes a string with maximum length 240.
                    Example: "John"

    lName           Last Name. Required, takes a string with maximum length 240.
                    Example: "Smith"

    comYear         Community Year (which year the person joined the olin community)
                    Not required, takes an integer.
                    Example: 2015

    email           Email. Not required, takes a string.
                    Example: "JohnSmith@students.olin.edu"

    pronouns        Personal pronouns. Not required, takes a string.
                    Example: "He/Him/His"

    services        Other services associated with this person. Not required, takes a dictionary.
                    Example: {"venmo":"jSmith50", "messenger":"Smithee"}

    """
    fName = StringField(max_length=240, required=True)
    lName = StringField(max_length=240, required=True)
    comYear = IntField()
    email = EmailField(max_length=100, required=True, unique=True, sparse=True)
    pronouns = StringField(max_length=100)
    preferredName = StringField(max_length=240)
    services = DictField()

    # TODO:
    # add role at Olin
    # BOW students?
    # allergies/diet
    # image/gravatar