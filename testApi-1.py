from requests import put, get, post
import os

if os.environ.get('DATABASE_URL'):
    c = get('http://olin-api.heroku.com/test', params={ 'data': 'data to be sent here', 'a':'b' })
    print c
    print c.__repr__
    print c.json()

else:
    get_req = get('http://localhost:5000/test', data={ 'data': 'get request data?', 'a':'b', 'c':'d' })
    print get_req
    # print get_req.__repr__
    print get_req.json()


    post_req = post('http://localhost:5000/test', data={ 'data': 'post request data', 'a':'b', 'c':'d' })
    print post_req
    # print post_req.__repr__
    print post_req.json()

    put_req = put('http://localhost:5000/test', data={ 'data': 'put request data', 'a':'b', 'c':'d' })
    print put_req
    # print put_req.__repr__
    print put_req.json()


### Unused Queries ###


# print put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()

# get('http://localhost:5000/todo1').json()

# a = put('http://olin-api.heroku.com/todo1', data={'data': 'Change my brakepads'})
# # a is a Response type
# print a.__repr__
# print a.json()

# b = get('http://olin-api.heroku.com/todo1', data={'data': 'Change my brakepads', 'a':'b'})
# #so is b
# print b.__repr__
# print b.json()
# get('http://localhost:5000/todo2').json()
# print get('http://olin-api.heroku.com/todo1').json()
# print get('http://olin-api.heroku.com/todo1', data = {'data': 'select * from events where event_id is not null'}).json()
# a = post('http://olin-api.heroku.com/todo2', data = {'data': 'select * from events where event_id is not null'})
# print a
# print a.text
# print a.json()
# print put('http://olin-api.heroku.com/todo2', data={'data': 'Change my brakepads'}).json()
