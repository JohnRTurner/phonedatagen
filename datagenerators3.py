# Creates TCP-H line-item data.
import math

from faker import Faker
from datetime import datetime, timedelta
from json import dumps
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')


def gen_event(thread, fake, inv, linenumber):
 rndcnt = fake.random_number( digits=8)
 shipdate = datetime.today() + timedelta(days = (rndcnt % 23) - 30)
 recdate = shipdate + timedelta(days =((rndcnt%4) + 1))
 comdate = shipdate + timedelta(days =((rndcnt%5) + 3))
 pkey = (rndcnt % 20000000) + 1
 skey = (rndcnt % 999999) + 1
 return {
         "l_comment":fake.sentence(nb_words=3),
         "l_commitdate":comdate.strftime('%Y-%m-%d'),
         "l_discount":float(fake.pydecimal(left_digits = 2, right_digits = 2, positive = True, max_value = 25.0)),
         "l_extendedprice":float(fake.pydecimal(left_digits = 5,right_digits = 2, positive = True, min_value = 1000, max_value = 99999)),
         "l_linenumber":linenumber,
         "l_linestatus":fake.pystr(min_chars=1, max_chars=1),
         "l_orderkey": inv,
         "l_partkey":pkey,
         "l_quantity":fake.random_int(min=1, max=1000),
         "l_receiptdate":recdate.strftime('%Y-%m-%d'),
         "l_returnflag":fake.pystr(min_chars=1, max_chars=1),
         "l_shipdate":shipdate.strftime('%Y-%m-%d'),
         "l_shipinstruct":fake.sentence(nb_words=3),
         "l_shipmode":fake.sentence(nb_words=3),
         "l_suppkey":skey,
         "l_tax":float(fake.pydecimal(left_digits = 2, right_digits = 2, positive = True, max_value = 25)) }

def gen_events(batch_start, batch_size, thread):
  Faker.seed()
  fake = Faker()
  myarr = []
  for inv in range(0, batch_size):
    for linenumber in range(1,9):
           myarr.append(gen_event(thread, fake, inv + batch_start, linenumber))
  return myarr

#For testing the JSON data creation.
if __name__ == '__main__':
    print(dumps(gen_events(10000, 2,1)))
