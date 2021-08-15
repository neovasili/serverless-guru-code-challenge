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
        input_parameters["order_id"] = order_id
        order = Order(input_parameters=input_parameters)

        self.__repository.save(order=order)
        self.__logger.info("Created order")

        return order

    def update_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Updating order")
        order.update(input_parameters=input_parameters)

        self.__repository.save(order=order)
        self.__logger.info("Updated order")

        return order

    def accept_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Accepting order")
        order.accept()

        self.__repository.save(order=order)
        self.__logger.info("Order accepted")

        return order

    def start_cooking_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Starting to cook order")
        order.start_cooking()

        self.__repository.save(order=order)
        self.__logger.info("Started to cook order")

        return order

    def ready_to_deliver_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Putting ready to deliver order")
        order.ready_to_deliver()

        self.__repository.save(order=order)
        self.__logger.info("Order ready to deliver")

        return order

    def on_route_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Putting order on route")
        order.on_route()

        self.__repository.save(order=order)
        self.__logger.info("Order on route")

        return order

    def delivered_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Delivering order")
        order.delivered()

        self.__repository.save(order=order)
        self.__logger.info("Order delivered")

        return order

    def cancel_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Canceling order")
        order.cancel()

        self.__repository.save(order=order)
        self.__logger.info("Order canceled")

        return order

    def delete_order(self, input_parameters: dict) -> Order:
        order_id = input_parameters["order_id"]
        order = self.get_order(order_id=order_id)

        if order is None:
            return None

        self.__logger.info("Deleting order")

        self.__repository.delete(order_id=order_id)
        self.__logger.info("Order deleted")

        return order
