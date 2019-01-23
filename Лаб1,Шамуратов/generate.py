from faker import Faker
import json
import csv
import random
from datetime import datetime

f = Faker("ru_RU")


def random_date(first, last):
    first = datetime(*first).timestamp()
    last = datetime(*last).timestamp()
    day = 86400
    random_timestamp = random.randint(first+day, last)
    date = datetime.fromtimestamp(random_timestamp)
    return '%s-%s-%s' % (date.day, date.month, date.year)


def gen_users(count=10):
    users = []
    for i in range(count):
        users.append(gen_user(i))
        i+=1
    return users


def gen_user(id):
    return {
        'id': id,
        'name':f.name(),
        'mail':f.email(),
        'phone':f.phone_number()
    }


def gen_products(count=10):
    products = []
    for i in range(count):
        products.append(gen_product(i))
    return products


def gen_product(id):
    return {
        'id':id,
        'name':f.company(),
        'price': random.randint(1, 10000) / 100
    }


def gen_sales(users, products, count=10):
    sales = []
    id = 0
    for i in range(len(users)):
        id_user = users[i]['id']
        for j in range(count):
            id_product = random.choice(products)['id']
            sales.append(gen_sale(id, id_product, id_user))
            id+=1
    return sales


def gen_sale(id, id_product, id_user):
    return {
        'id':id,
        'user':id_user,
        'product':id_product,
        'count':random.randint(1,10),
        'date':random_date((2017, 1, 1), (2018, 12, 31))
    }


def create_json(file_name, data):
    file = open(file_name+'.json', 'w', encoding='utf-8')
    json.dump(data, file)
    file.close()


def create_csv(file_name, data):
    file = open(file_name+'.csv', 'w', newline='')
    keys = data[0].keys()
    writter = csv.DictWriter(file, keys)
    writter.writeheader()
    writter.writerows(data)
    file.close()


users = gen_users()
products = gen_products()
sales = gen_sales(users, products)

create_json('persons', users)
create_json('products', products)
create_json('sales', sales)

create_csv('persons', users)
create_csv('products', products)
create_csv('sales', sales)


