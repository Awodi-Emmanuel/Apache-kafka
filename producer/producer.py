from atexit import register
from ensurepip import bootstrap
from kafka import KafkaProducer
from data import get_registered_user
import json
import time


# from kafka.errors import KafkaError

def json_serilizer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=json_serilizer)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send('test-events', registered_user)
        time.sleep(4)