from confluent_kafka import Producer, Consumer
import threading
import json
from collections import deque

c = Consumer({'bootstrap.servers':'broker:29092','group.id':'python-consumer','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')
print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['integer-count'])

p = Producer({'bootstrap.servers':'broker:29092'})
print('Kafka Producer has been initiated...')

INT_LIST = deque()

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        print(message)

def consume(consumer):
    while True:
        msg=consumer.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        INT_LIST.append(data)

def produce(producer):
    while True:
        if len(INT_LIST) != 0:
            message = json.dumps(int(INT_LIST.popleft()) * 10)
            producer.produce('times-ten', message.encode('utf-8'), callback=receipt)
            producer.flush()

if __name__ == "__main__":
    consume_thread = threading.Thread(target=consume, args=(c,))
    produce_thread = threading.Thread(target=produce, args=(p,))

    consume_thread.start()
    produce_thread.start()