import os

from aws_lambda_powertools import Logger

from src.controller.order import OrderController
from src.helper.tools import ApiHelper

logger = Logger(service="UpdateOrder")

ORDERS_TABLE = os.environ.get("ORDERS_TABLE")


@logger.inject_lambda_context
def handler(event, context):
    logger.debug(event)

    response = dict()

    input_data = ApiHelper.get_input_data(event=event)
    operation = ApiHelper.get_operation(event=event)
    order_controller = OrderController(table_name=ORDERS_TABLE, logger=logger)

    operation_router = {
        "updateOrder": order_controller.update_order,
        "acceptOrder": order_controller.accept_order,
        "startCookingOrder": order_controller.start_cooking_order,
        "readyToDeliverOrder": order_controller.ready_to_deliver_order,
        "onRouteOrder": order_controller.on_route_order,
        "deliveredOrder": order_controller.delivered_order,
        "cancelOrder": order_controller.cancel_order,
    }

    try:
        order = operation_router[operation](input_parameters=input_data)
        response = ApiHelper.get_response(event=event, item=order)

    except Exception as e:
        logger.exception(e)

    logger.debug(response)

    return response
