from kafka import KafkaProducer
import os


class KafkaAdapter:
    server: str
    client_id: str

    def __init__(self):
        self.server = os.getenv("KAFKA_URL")
        self.client_id = os.getenv("KAFKA_CLIENT_ID")

    def topic_send(self, msg: str) -> None:
        producer = KafkaProducer(bootstrap_servers=[self.server], client_id=self.client_id)
        producer.send('card_ordered', bytes(msg, 'utf-8'))

    def topic_subscribe(self):
        pass
