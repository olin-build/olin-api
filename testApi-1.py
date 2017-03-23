from requests import put, get, post
import json
import os

testing_local_app = True

def print_debug(thing):
    try:
        print(thing.json())
    except:
        print(str(thing))

data1 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'delete', 'data':{}}})}

data2 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'insert', 
                                                                                'data':[{'1':'6'},{'1':'7'},{'1':'8'}]}})}

data3 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'find', 'data':{'1':{'$gt':'1'}}}})}

data4 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction': {'op':'update', 
                                                                                'data':({'1':{'$gt':'1'}},{'$set':{'secondfield':'test'}})}})}

data5 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction': {'op':'delete', 'data':{'1':{'$eq':'6'}}}})}

data6 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'find', 'data':{'1':{'$gt':'1'}}}})}

if testing_local_app:
    post_request_delete_all = post('http://localhost:5000/test', data = data1)
    print_debug(post_request_delete_all)

    post_request_insert = post('http://localhost:5000/test', data = data2)
    print_debug(post_request_insert)

    post_request_find_some = post('http://localhost:5000/test', data = data3)
    print_debug(post_request_find_some)

    post_request_update = post('http://localhost:5000/test', data = data4)
    print_debug(post_request_update)

    post_request_delete = post('http://localhost:5000/test', data = data5)     
    print_debug(post_request_delete)

    post_request_find_final = post('http://localhost:5000/test', data = data6)
    print_debug(post_request_find_final)



else:
    get_req = get('http://olin-api.heroku.com/test', data={ 'data': 'get request data?', 'a':'b', 'c':'d' })
    print(get_req)
    # print get_req.__repr__
    print(get_req.json())


    post_req = post('http://olin-api.heroku.com/test', data={ 'data': 'post request data', 'a':'b', 'c':'d' })
    print(post_req)
    # print post_req.__repr__
    print(post_req.json())

    put_req = put('http://olin-api.heroku.com/test', data={ 'data': 'put request data', 'a':'b', 'c':'d' })
    print(put_req)
    # print put_req.__repr__
    print(put_req.json())




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
