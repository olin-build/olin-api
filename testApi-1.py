from requests import put, get

get('http://olin-api.herokuapp.com/todo1', data = {'query': 'select * from events where event_id is not null'})
