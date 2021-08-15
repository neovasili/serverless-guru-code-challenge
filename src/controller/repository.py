from aws_lambda_powertools import Logger

from src.model.order import Order
from src.service.dynamodb import DynamoDBService


class OrderRepository:
    """
    Controller class to manage storage of Orders
    """

    def __init__(self, table_name: str, logger: Logger = None):
        self.__logger = logger if logger else Logger(service="OrderRepository")
        self.__dynamodb_service = DynamoDBService(table_name=table_name)

    def find(self, order_id: str):
        self.__logger.debug(f"Retrieve order with order_id '{order_id}'' from database")
        return self.__dynamodb_service.find(id_name="order_id", item_id=order_id)

    def save(self, order: Order):
        self.__logger.debug(f"Save order with order_id '{order.get_model()['order_id']}'' into database")
        return self.__dynamodb_service.save(item=order.get_model())

    def delete(self, order_id: str):
        self.__logger.debug(f"Delete order with order_id '{order_id}'' from database")
        return self.__dynamodb_service.delete(id_name="order_id", item_id=order_id)
