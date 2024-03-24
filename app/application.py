from adapters.dotenv import DotenvAdapter
from adapters.kafka import KafkaAdapter
from dto import OrderCardDto


class Application:
    def __init__(self):
        DotenvAdapter().load_env_file()

    def order_physical_card(self, request: OrderCardDto) -> None:
        KafkaAdapter().topic_send(request.to_json())

    def handle_ordered_card(self):
        KafkaAdapter().topic_subscribe()
