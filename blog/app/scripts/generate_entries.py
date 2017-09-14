import sys, random
sys.path.append('/home/xray/PycharmProjects/flask_project/blog/app')
from models import *

for i in range(1000):
    db.session.add(Entry(title='Generated entry ' + str(i) + str(random.randint(0, 1000000)), body='A generated entry.', status=i % 2))
db.session.commit()
