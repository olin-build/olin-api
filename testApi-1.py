from requests import put, get

# print put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()

# get('http://localhost:5000/todo1').json()

# print put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()

# get('http://localhost:5000/todo2').json()
print get('http://olin-api.heroku.com/todo1').json()
print get('http://olin-api.heroku.com/todo1', data = {'data': 'select * from events where event_id is not null'}).json()
print post('http://olin-api.heroku.com/todo1', data = {'data': 'select * from events where event_id is not null'}).json()
print put('http://olin-api.heroku.com/todo2', data={'data': 'Change my brakepads'}).json()
