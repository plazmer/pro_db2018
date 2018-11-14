import json
import csv
import time

def load_csv(filename):
    rows = []
    file = open(filename, 'r')
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)
    file.close()
    return rows
    
def load_json(filename):
    rows = []
    file = open(filename, 'r')
    for row in json.load(file):
        rows.append(row)
    file.close()
    return rows

def analyze_sales_by_month():
    printArray = {}

    for sale in sales:
        date = time.strptime(sale['date'], '%x')
        if (date[1] != 10) & (date[1] != 11) & (date[1] != 12):
            monthStr = '0' + str(date[1])
        else:
            monthStr = str(date[1])
        month = str(date[0]) + monthStr
        if month in printArray.keys():
            printArray[month]['summa'] = int(printArray[month]['summa']) + int(sale['count'])
        else:
            printArray[month] = {'year': date[0], 'month': date[1], 'summa': sale['count']}

    listKeys = list(printArray.keys())
    listKeys.sort()
    for key in listKeys:
        print(printArray[key]['year'], printArray[key]['month'], printArray[key]['summa'])
    
def best_3_persons():
    """выводит 3 имени лучших покупателя и сумму их покупок, от большего к меньшему"""
    userSales = {}
    for u in users:
        for s in sales:
            if u['name'] == s['user']:
                for p in products:
                    if u['name'] in userSales.keys():
                        if p['name'] == s['product']:
                            userSales[u['name']] = round(float(userSales[u['name']]) + float(p['price']) * int(s['count']), 2)
                    else:
                        if p['name'] == s['product']:
                            userSales[u['name']] = round(float(p['price']) * int(s['count']), 2)

    sortUserSales = sorted(userSales.items(), key=lambda item: (-item[1], item[0]))
    for val in range(3):
         print(sortUserSales[val][0], sortUserSales[val][1])

def worst_3_products():
    """выводит 3 худших по продажам товаровб от меньшего к большему"""
    sumProducts = {}
    for p in products:
        sumProducts[p['name']] = 0
        for s in sales:
            if p['name'] == s['product']:
                sumProducts[p['name']] = round(float(sumProducts[p['name']]) + float(p['price']) * int(s['count']), 2)

    sortSumProducts = sorted(sumProducts.items(), key=lambda item: (item[1], item[0]))
    for val in range(3):
        print(sortSumProducts[val][0], sortSumProducts[val][1])

users = load_csv('users.csv')
products = load_csv('products.csv')
sales = load_csv('sales.csv')

analyze_sales_by_month()
best_3_persons()
worst_3_products()

users = load_json('users.json')
products = load_json('products.json')
sales = load_json('sales.json')

analyze_sales_by_month()
best_3_persons()
worst_3_products()