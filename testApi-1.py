from requests import put, get
# print put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()

# get('http://localhost:5000/todo1').json()

# print put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()

# get('http://localhost:5000/todo2').json()

get('http://olin-api.herokuapp.com/todo1', data = {'query': 'select * from events where event_id is not null'})
