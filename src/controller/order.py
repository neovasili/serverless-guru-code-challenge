from aws_lambda_powertools import Logger

from src.controller.repository import OrderRepository
from src.model.order import Order


class OrderController:
    """
    Controller class to manage Orders business logic
    """

    def __init__(self, table_name: str, logger: Logger = None):
        self.__logger = logger if logger else Logger(service="OrderController")
        self.__repository = OrderRepository(table_name=table_name, logger=self.__logger)

    def get_order(self, order_id: str) -> Order:
        order = self.__repository.find(order_id=order_id)

        if order is not None:
            return Order(input_parameters=order)

        return None

    def create_order(self, input_parameters: dict) -> Order:
        order_id = Order.generate_id()
        order = self.get_order(order_id=order_id)

        while order is not None:
            order_id = Order.generate_id()
            order = self.get_order(order_id=order_id)

        self.__logger.info("Creating order")
        order = Order(input_parameters=input_parameters)

        self.__repository.save(order=order)
        self.__logger.info("Created order")

        return order
