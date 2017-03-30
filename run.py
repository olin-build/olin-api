import os

from src.app import create_app

app = create_app()

port = int(os.environ.get('PORT', 5000))

if os.environ.get('MONGODB_URI'):
    app.run(host='0.0.0.0', debug=True, port=port)
else:
    app.run(host='127.0.0.1', debug=True, port=port)
