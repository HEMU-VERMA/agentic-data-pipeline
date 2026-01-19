import json
from confluent_kafka import Consumer

class DataStreamConsumer:
    def __init__(self, bootstrap_servers="localhost:9092"):
        self.conf = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': "agentic-data-group",
            'auto.offset.reset': 'earliest'
        }
        self.consumer = Consumer(self.conf)

    def listen(self, topic, callback):
        self.consumer.subscribe([topic])
        print(f"Agentic Consumer listening on topic: {topic}")
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None: continue
                data = json.loads(msg.value().decode('utf-8'))
                callback(data)
        finally:
            self.consumer.close()