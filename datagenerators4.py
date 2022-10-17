# Creates TCP-H line-item data.
import math

from faker import Faker
from datetime import datetime, timedelta
from json import dumps
from json import encoder
from dateutil import tz
encoder.FLOAT_REPR = lambda o: format(o, '.2f')


def gen_event(thread, fake, inv):
 ad_accnt_id = 8006927753
 rndcnt = fake.random_number( digits=8)
 ad_org_date = fake.past_datetime('-30d',tz.gettz('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S %Z")

 return {
         "AD_ACCOUNT_ID":ad_accnt_id,
         "CAMPAIGN_ID":fake.random_int(min=8006927753100, max=8006927753200),
         "AD_GROUP_ID":fake.random_int(min=8006927753100300, max=8006927753200600),
         "AD_ID":fake.random_number( digits=8),
         "KEYWORD_ID":fake.random_number( digits=13),
         "CREATIVE_ID":fake.random_number( digits=18),
         "MATCH_TYPE":fake.pystr(min_chars=10, max_chars=20),
         "SEARCH_TERM": fake.pystr(min_chars=8, max_chars=24),
         "SPEND":float(fake.pydecimal(left_digits = 6,right_digits = 4, positive = True, min_value = 1000, max_value = 999999)),
         "IMPRESSIONS":fake.random_int(min=1, max=1000000),
         "TAPS":fake.random_int(min=1, max=100000),
         "DOWNLOAD":fake.random_int(min=1, max=10000),
         "AD_ORG_DATE": ad_org_date
 }

def gen_events(batch_start, batch_size, thread):
  Faker.seed()
  fake = Faker()
  myarr = []
  for inv in range(0, batch_size):
               myarr.append(gen_event(thread, fake, inv))
  return myarr

#For testing the JSON data creation.
if __name__ == '__main__':
    print(dumps(gen_events(10000, 4,1)))
