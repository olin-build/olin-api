from requests import put, get, post

# print put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()

# get('http://localhost:5000/todo1').json()

a = post('http://olin-api.heroku.com/todo1', params={'data': 'Change my brakepads'})
print a.json()
print a.url

# get('http://localhost:5000/todo2').json()
# print get('http://olin-api.heroku.com/todo1').json()
# print get('http://olin-api.heroku.com/todo1', data = {'data': 'select * from events where event_id is not null'}).json()
# a = post('http://olin-api.heroku.com/todo2', data = {'data': 'select * from events where event_id is not null'})
# print a
# print a.text
# print a.json()
# print put('http://olin-api.heroku.com/todo2', data={'data': 'Change my brakepads'}).json()
