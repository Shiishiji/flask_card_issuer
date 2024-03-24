from pprint import pprint

from kafka import KafkaProducer, KafkaConsumer
import os

TOPIC_CARD_ORDERED = "card_ordered"

class KafkaAdapter:
    server: str
    client_id: str

    def __init__(self):
        self.server = os.getenv("KAFKA_URL")
        self.client_id = os.getenv("KAFKA_CLIENT_ID")

    def topic_send(self, msg: str) -> None:
        producer = KafkaProducer(bootstrap_servers=[self.server], client_id=self.client_id)
        producer.send(TOPIC_CARD_ORDERED, bytes(msg, 'utf-8'))

    def topic_subscribe(self):
        consumer = KafkaConsumer(TOPIC_CARD_ORDERED, bootstrap_servers=[self.server], group_id="consumer-group-1")
        record = consumer.poll()
        pprint(record)
