from faker import Faker
import random
import datetime
import time
import json
import csv

f = Faker("ru_RU")

users = [] #10 пользователей -> users.json, users.csv
products = [] #10 товаров -> products.json, products.csv
sales = [] #0-10 случайных продаж случайного товара каждому пользователю ->sales.json, sales.csv

for i in range(10):
    users.append({
        'name': f.name(),
        'mail': f.email(),
        'phone': f.phone_number()
    })
    products.append({
        'name': f.company(),
        'price': random.randint(100, 10000) / 100
    })
for i in range(random.randint(0, 10)):
    sales.append({
        'user': users[random.randint(0, 9)]['name'],
        'product': products[random.randint(0, 9)]['name'],
        'date': time.strftime('%x', f.date_between(
            start_date=datetime.date(2017, 1, 1),
            end_date=datetime.date(2018, 12, 31)
        ).timetuple()),
        'count': random.randint(1, 10)
    })

data = {'users': users, 'products': products, 'sales': sales}
for name in data:
    f = open(name + '.json', 'w', encoding="UTF-8")
    json.dump(data[name], f)
    f.close()

    f = open(name + '.csv', 'w', newline='')
    for i in data[name]:
        writer = csv.DictWriter(f, i.keys())
    writer.writeheader()
    writer.writerows(data[name])
    f.close()
