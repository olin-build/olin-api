from requests import put, get, post
import json
import os

if __name__ == "__main__":
    from database_connection_mongoengine import make_connection
    from document_models import Person

testing_local_app = True

def print_debug(thing):
    try:
        print(thing.json())
    except:
        print(str(thing))



    if testing_local_app:
        get_request = get('http://localhost:5000/people/?comYearMIN=2000&comYearMAX=2050a')
        print_debug(get_request)
        print()

        post_request_insert = post('http://localhost:5000/people/', json={'fName':'Abraham','lName':1,'comYear':2018, 'preferredName':'Abe', 'email':'AbeLincoln@students.olin.edu'})
        print_debug(post_request_insert)
        print()

        post_request_insert_1 = post('http://localhost:5000/people/', json={'fName':'Abraham','lName':'Lincoln','comYear':2018, 'preferredName':'Abe', 'email':'AbeLincoln@students.olin.edu'})
        print_debug(post_request_insert_1)
        print()

        put_request_edit = put('http://localhost:5000/people/?comYearMIN=2016&comYearMAX=2017', json={'comYear':2000})
        print_debug(put_request_edit)
        print()

        get_request_1 = get('http://localhost:5000/people/?comYearMIN=2000&comYearMAX=2050')
        print_debug(get_request_1)
        print()


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


# data1 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'delete', 'data':{}}})}

# data2 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'insert', 
#                                                                                 'data':[{'1':'6'},{'1':'7'},{'1':'8'}]}})}

# data3 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'find', 'data':{'1':{'$gt':'1'}}}})}

# data4 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction': {'op':'update', 
#                                                                                 'data':({'1':{'$gt':'1'}},{'$set':{'secondfield':'test'}})}})}

# data5 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction': {'op':'delete', 'data':{'1':{'$eq':'6'}}}})}

# data6 = {'data':json.dumps({'requestLocation':'test-collection', 'instruction':{'op':'find', 'data':{'1':{'$gt':'1'}}}})}


# post_request_find_some = post('http://localhost:5000/test', data = data3)
# print_debug(post_request_find_some)

# post_request_update = post('http://localhost:5000/test', data = data4)
# print_debug(post_request_update)

# post_request_delete = post('http://localhost:5000/test', data = data5)     
# print_debug(post_request_delete)

# post_request_find_final = post('http://localhost:5000/test', data = data6)
# print_debug(post_request_find_final)
