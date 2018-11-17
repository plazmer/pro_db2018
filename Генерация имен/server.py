from bottle import *
from faker import Faker

fake = Faker('ru_RU')

@route('/assets/<filename>')
def stat(filename):
    return static_file(filename, 'assets/')


@route('/')
def ret_index():
    return static_file('index.html', './')

@get('/phone')
def phone_gen():
    return fake.phone_number()


@get('/name')
def name_gen():
    return fake.name()


@get('/user')
def user_gen():
    return json_dumps({
        'name': fake.name(),
        'phone': fake.phone_number(),
    })


run(host='localhost', port=8080, debug=True)
