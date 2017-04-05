""" Contains all of the mongoengine models for data held in mongo """
from mongoengine import Document, StringField, IntField, ListField, DictField

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
    email = StringField(max_length=100, required=True)
    pronouns = StringField(max_length=100)
    preferredName = StringField(max_length=240)
    services = DictField()

    # TODO:
    # add role at Olin
    # BOW students?
    # allergies/diet
    # image/gravatar

if __name__ == "__main__":
    from database_connection_mongoengine import make_connection
    make_connection()
    Person.drop_collection()
    people = [
    {"fName": "John", "lName": "Doe", "comYear": 2015, "email": "JohnDoe@students.olin.edu", "pronouns": "He/Him/His", "preferredName": "John", "services":{"venmo":"jDoe109", "messenger":"Doeboy"}},
    {"fName": "Jane", "lName": "Doe", "comYear": 2015, "email": "JaneDoe@students.olin.edu", "pronouns": "She/Her/Hers", "preferredName": "Jane"},
    {"fName": "Alan", "lName": "Smith", "comYear": 2016, "email": "AlanSmith@students.olin.edu", "pronouns": "They/Them/Theirs", "preferredName":"Alan"},
    {"fName": "Bob", "lName": "Burger", "comYear": 2016, "email": "BobBurger@students.olin.edu", "pronouns": "It/It/Its", "preferredName": "Burger"},
    {"fName": "Susan", "lName": "Green", "comYear": 2017, "email": "SusanGreen@students.olin.edu", "pronouns": "She/Her/Hers", "preferredName": "Suzie"},
    {"fName": "Marianne", "lName": "Moss", "comYear": 2017, "email": "MarianneMoss@students.olin.edu", "pronouns": "She/Her/Hers", "preferredName": "Carrie"},
    ]

    for dct in people:
        item = Person(**dct)
        item.save()