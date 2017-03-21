import os

# import database_connection_mongo

from src.app import create_app

app = create_app()

port = int(os.environ.get('PORT', 5000)) #not sure this will work

app.run(host='127.0.0.1', debug=True, port=port)
