import os

from aws_lambda_powertools import Logger

from src.controller.order import OrderController
from src.helper.tools import ApiHelper

logger = Logger(service="GetOrder")

ORDERS_TABLE = os.environ.get("ORDERS_TABLE")


@logger.inject_lambda_context
def handler(event, context):
    logger.debug(event)

    response = dict()

    input_data = ApiHelper.get_input_data(event=event)
    order_controller = OrderController(table_name=ORDERS_TABLE, logger=logger)

    try:
        order = order_controller.get_order(order_id=input_data["order_id"])
        response = ApiHelper.get_response(event=event, item=order)

    except Exception as e:
        logger.error(e)

    logger.debug(response)

    return response
