import json
import csv
from datetime import datetime

def load_csv(filename):
    rows = []
    file = open(filename, 'r')
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)
    file.close()
    return rows
    
def load_json(filename):
    return json.load(open(filename))

def analyze_sales_by_month():
    """выводит сумму проданных товаров по месяцам за весь период, """
    summ = {}
    for sale in sales:
        date = datetime.strptime(sale['date'], '%d-%m-%Y')
        key = '%d-%d' % (date.year, date.month)
        count = float(sale['count'])
        product = find_by_id(products, sale['product'])
        price = float(product['price'])
        total = count*price
        if summ.get(key, False):
            summ[key]['summ_price'] += total
        else:
            summ[key] = {
                'date': date,
                'summ_price': total
            }
    summ = to_array(summ)
    summ.sort(key=sort_by_date)
    print('Сумма по месяцам за весь период')
    for period in summ:
        print(period['date'].strftime('%m/%y'), round(period['summ_price'], 2))
    
def best_3_persons():
    summ = {}
    for sale in sales:
        user = sale['user']
        count = float(sale['count'])
        prod_id = sale['product']
        price = float(find_by_id(products, prod_id)['price'])
        total = count*price
        if(summ.get(user, False)):
            summ[user]['summ_price'] += total
        else: summ[user] = {
            'summ_price': total,
            'user_id': user
        }
    summ = to_array(summ)
    summ.sort(key=sort_by_sum, reverse=True)
    active_users_count = len(summ)
    limit = 3 if active_users_count > 3 else active_users_count
    print('3 лучших клиента')
    for i in range(limit):
        info = summ[i]
        user = find_by_id(persons, info['user_id'])
        name = user['name']
        total = round(info['summ_price'], 2)
        print(name, total)
        
def worst_3_products():
    """выводит 3 худших по продажам товаровб от меньшего к большему"""
    summ = {}
    for sale in sales:
        count = float(sale['count'])
        prod_id = sale['product']
        price = float(find_by_id(products, prod_id)['price'])
        total = count*price
        if(summ.get(prod_id, False)):
            summ[prod_id]['summ_price'] += total
        else: summ[prod_id] = {
            'summ_price': total,
            'prod_id': prod_id
        }
    summ = to_array(summ)
    summ.sort(key=sort_by_sum, reverse=False)
    active_products_count = len(summ)
    limit = 3 if active_products_count > 3 else active_products_count
    print('3 худших товара')
    for i in range(limit):
        info = summ[i]
        product = find_by_id(products, info['prod_id'])
        name = product['name']
        total = round(info['summ_price'], 2)
        print(name, total)


def find_by_id(array, id):
    for elem in array:
        if (int(elem['id'])==int(id)):
            return elem
    return False


def sort_by_sum(input):
    return input['summ_price']


def sort_by_date(input):
    return input['date'].timestamp()


def to_array(assoc):
    array = []
    for key in assoc:
        array.append(assoc[key])
    return array

persons = load_csv('persons.csv')
products = load_csv('products.csv')
sales = load_csv('sales.csv')

analyze_sales_by_month()
best_3_persons()
worst_3_products()

persons = load_json('persons.json')
products = load_json('products.json')
sales = load_json('sales.json')

analyze_sales_by_month()
best_3_persons()
worst_3_products()

