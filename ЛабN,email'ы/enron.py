import os, sys
import email
import csv
from pymongo import MongoClient
from datetime import datetime
import time

mongo = MongoClient()
db = mongo['my_db']


out_file = open('1.csv', "w", newline='')
obj = {'from':None,'to':None,'subj':None,'date':None,'path':None}
writer = csv.DictWriter(out_file, delimiter='\t', fieldnames=obj.keys())
writer.writeheader()




# Getting the current work directory (cwd)
thisdir = os.getcwd()

cnt = 0
# r=root, d=directories, f = files
for r, d, f in os.walk('C:/Users/Student/Desktop/453105/enron/maildir'):
    if f:
        for file in f:
            path = r.replace('C:/Users/Student/Desktop/453105/enron/maildir\\','')
            fname = os.path.join(r, file)
            # print(path, fname)
            f = open(fname).read()
            #print(f)
            msg = email.message_from_string(f)

            d = email.utils.parsedate(msg.get('date'))
            dd = '-'.join([str(x) for x in d[0:3]])
            row = {'from':msg.get('From'),'to':msg.get('To', '').replace('\n', ' '),'subj':msg.get('Subject','').replace('\n', ' '),'date':dd,'path':path}
            writer.writerow(row)


            row['to'] = row['to'].split(',')
            arr = []
            for tmp in row['to']:
                arr.append(tmp.strip())
            row['to'] = arr
            print(row)

            if cnt > 100:
                sys.exit(0)
            cnt += 1







