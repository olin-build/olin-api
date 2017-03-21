#! /bin/bash

# INSTRUCTIONS: ./lint.sh <path to code you want to lint>
# (otherwise it'll assume you're running from project root)
source venv/bin/activate &&

if [ -z "$1" ]
  then
    echo "No argument supplied, using default" &&
    python3 -m pylint -d invalid-name,no-member,no-self-use,too-few-public-methods src/
  else
    python3 -m pylint -d invalid-name,no-member,no-self-use,too-few-public-methods $1
fi

# -d ignores the errors listed:
# no-member because flask/mongoengine stuff frequently shows up as false positive
# no-self-use for flask, which causes many false positives due to things needing to be members
# too-few-public-methods for flask as well, since some things have to be classes
