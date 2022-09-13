# Creates Claim data
from faker import Faker
from datetime import datetime, timedelta
from json import dumps
import numpy as np
import time as time

type_of_injury = ['Shoulder','Knee','Paralyzed','Back']
risk_score = ['Green','Yellow' ,'Red']

def gen_event(thread, fake):
    return {
        "claimant": fake.name(),
        "claimantId": (int((time.clock_gettime(time.CLOCK_MONOTONIC_RAW) % 1000000) * 10000000)* 100) + thread,
        "DOB": fake.date_between(start_date='-65y', end_date='-28y').strftime('%Y-%m-%d'),
        "DOI": fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),
        "Type of Injury": np.random.choice(type_of_injury, p=[0.40, 0.30, 0.20, 0.10]),
        "Risk": np.random.choice(risk_score, p=[0.50, 0.30, 0.20]),
        "Total Claim Value": fake.random_int(100000, 5000000),
        "updated": datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f')
    }


def gen_events(batch_size, thread):
  Faker.seed()
  fake = Faker()
  return [gen_event(thread, fake) for _ in range(1, (batch_size + 1))]

#For testing the JSON data creation.
if __name__ == '__main__':
    print(dumps(gen_events(10,1)))
