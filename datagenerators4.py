# Creates TCP-H line-item data.
import math

from faker import Faker
from datetime import datetime, timedelta
from json import dumps
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')


def gen_event(thread, fake, inv, linenumber):
 ad_accnt_id = 8323779991
 rndcnt = fake.random_number( digits=8)
 ad_utc_date = datetime.today() + timedelta(days = (ad_accnt_id % 23) - 30)
 recdate = shipdate + timedelta(days =((ad_accnt_id%4) + 1))
 comdate = shipdate + timedelta(days =((ad_accnt_id%5) + 3))
 pkey = (ad_accnt_id % 20000000) + 1
 skey = (ad_accnt_id % 999999) + 1
 return {
         "AD_ACCOUNT_ID":ad_accnt_id,
         "CAMPAIGN_ID":fake.random_int(min=8323779991100, max=8323779991200),
         "AD_GROUP_ID":fake.random_int(min=8323779991100300, max=8323779991200600),
         "AD_ID":fake.random_number( digits=8),
         "KEYWORD_ID":fake.random_number( digits=13),
         "CREATIVE_ID":fake.random_number( digits=18),
         "MATCH_TYPE":fake.pystr(min_chars=10, max_chars=20),
         "SEARCH_TERM": fake.pystr(min_chars=8, max_chars=24),
         "SPEND":float(fake.pydecimal(left_digits = 6,right_digits = 4, positive = True, min_value = 1000, max_value = 999999)),
         "IMPRESSIONS":fake.random_int(min=1, max=1000000),
         "TAPS":fake.random_int(min=1, max=100000),
         "DOWNLOAD":fake.random_int(min=1, max=10000),
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
