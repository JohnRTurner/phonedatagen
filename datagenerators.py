#from random import randrange, choice, uniform, getrandbits
import math

from faker import Faker
from datetime import datetime, timedelta
from json import dumps
import numpy as np

# ● Switch: The switch the call is hitting
# ● Date: The date of the call
# ● Time: The time of the start of the call (based on the switch)
# ● Orig C/G: Valid cell site for outgoing calls (Only for MO calls)
# ● Term C/G: Valid cell site for incoming calls (Only for MT calls)
# ● Dir:
#   – MO=Outgoing
#   – MT=Incoming
#   – MF=Incoming to voicemail and in rare cases, mobile forwarding
# ● MDN: Your target number
# ● Called #: If outgoing, this is the number your target dialed
# ● ESN: Electronic Serial Number of your target
# ● CPN: If incoming, this is the number that called your target
# ● Szr: Duration of the call in seconds
def gen_event(thread, fake, acct, esn, cg, secparty, seccg):
 dttm = (datetime.now() - timedelta(seconds=fake.pyint(0, 86400 * 30))).strftime("%Y-%m-%d %H:%M:%S.%f")

 if(fake.boolean()):
     dir = "MT"  #incoming
     tcg = cg
     ocg = np.random.choice(seccg)
     called = acct
     cpn = np.random.choice(secparty)

 else:
     dir = "MO"  #outgoing
     tcg = np.random.choice(seccg)
     ocg = cg
     called = np.random.choice(secparty)
     cpn = acct

 return {
   "switch": fake.city(),
   "Datetime": dttm, # last 30 days...
   "Orig C/G": int(ocg),
   "Term C/G": int(tcg),
   "Dir": dir,
   "MDN": int(acct),
   "Called": int(called),
   "ESN" :esn,
   "CPN":int(cpn),
   "szr":int(fake.random_int(min=3, max=1800))
 }

def gen_events(batch_size, thread):
  Faker.seed()
  fake = Faker()
  acct = fake.random_int(min=2001000000, max=8999999999)
  esn = fake.bothify(text='????#######')
  cg = fake.random_int(min=100, max=9999)
  secparty = [fake.random_int(min=2001000000, max=8999999999) for _ in range(0,math.ceil(batch_size / 10))]
  seccg = [fake.random_int(min=100, max=9999) for _ in range(0,math.ceil(batch_size / 10))]
  return [gen_event(thread, fake, acct, esn, cg, secparty, seccg) for _ in range(1, (batch_size + 1))]

if __name__ == '__main__':
    print(dumps(gen_events(1000,1)))
