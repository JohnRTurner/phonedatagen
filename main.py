import argparse
import sys
from time import time
import multiprocessing as mp
from kafka import kafka_producer, acked
#from datagenerators import gen_events
from datagenerators2 import gen_events
from json import dumps

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--batch_size',
                    dest='batch_size',
                    help="The amount of messages to be generated for each 'produce'",
                    default=1000
                   )
parser.add_argument('-t', '--topic',
                    dest='topic',
                    help="The destination kafka topic",
                    default="test"
                   )
parser.add_argument('-P', '--process_count',
                    dest='process_count',
                    help="The count of processes to be ran",
                    default=8
                   )
parser.add_argument('-k', '--kafka_server',
                    dest='kafka_server',
                    help="The kafka server being used with port"
                    )

args = parser.parse_args()

process_count = int(args.process_count)
batch_size    = int(args.batch_size)
topic         = str(args.topic)
kafka_server  = str(args.kafka_server)


def produce_orders(batch_size, topic, thread):
  producer = kafka_producer(server=kafka_server)
  while True:
    start = time()
    events = gen_events(batch_size, thread)
    #print(thread, events[0])
    producer.poll(0.0)
    for o in events:
      producer.produce(topic, value=dumps(o).encode('utf-8'), callback=acked)
    producer.flush()
    end     = time()
    tt    = end - start
    print(f"Thead: {thread}\nEvent Count: {len(events)}\nTotal Time: {tt}\n", file = sys.stderr)



def mp_func(x):
  global batch_size
  global topic
  return produce_orders(batch_size, topic, x)

if __name__ == '__main__':
  print('Start...')
  mp.freeze_support()
  #cpu_count    = mp.cpu_count()
  process_pool = mp.Pool(processes = process_count)
  process_pool.map( mp_func, range(process_count))