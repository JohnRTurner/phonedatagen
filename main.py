import argparse
import sys
from time import time
import multiprocessing as mp

from kafka import kafka_producer, acked
from datagenerators3 import gen_events
from json import dumps

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--batch_size',
                    dest='batch_size',
                    help="The amount of messages to be generated for each 'produce'",
                    default=1000
                   )
parser.add_argument('-s', '--start_inv',
                    dest='start_inv',
                    help="The starting invoice number",
                    default=100000
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



def produce_orders(start_inv, start_inv_lock, thrd):
  global lock
  global batch_size
  global topic
  #producer = kafka_producer(server=kafka_server)
  while True:
    start = time()
    print("Aquiring Lock")
    start_inv_lock.acquire()
    print(f"Lock Aquired for start_inv: {start_inv.value}")
    batch_start = start_inv.value
    start_inv.value =  batch_start + batch_size
    start_inv_lock.release()
    print("Lock Released")
    events = gen_events(batch_start, batch_size, thrd)
    #producer.poll(0.0)
    #for o in events:
    #  producer.produce(topic, value=dumps(o).encode('utf-8'), callback=acked)
    #producer.flush()
    tt  = time() - start
    print(f"Thead: {thrd}  StartInv: {start_inv}  Event Count: {len(events)}  Total Time: {tt}\n", file = sys.stderr)




def mp_func(start_inv, start_inv_lock, thrd):
  return produce_orders(start_inv, start_inv_lock, thrd)

if __name__ == '__main__':
  manager = mp.Manager()
  start_inv  = manager.Value('l', int(args.start_inv))
  start_inv_lock = manager.Lock()
  print('Start...')
  mp.freeze_support()
  process_pool = mp.Pool(processes = process_count)
  process_pool.starmap( mp_func,  [(start_inv, start_inv_lock, thrd) for thrd in range(process_count)]  )
