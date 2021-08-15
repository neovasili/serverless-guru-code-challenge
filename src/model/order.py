from src.helper.model import (
    ModelHelper,
)
from src.helper.tools import (
    IDHelper,
    StringHelper,
)


class OrderStatus(object):
    PENDING = "pending"
    RECEIVED = "received"
    COOKING = "cooking"
    READY = "ready"
    ON_ROUTE = "on_route"
    DELIVERED = "delivered"
    CANCELED = "canceled"


class Order(ModelHelper):
    """
    Model class to define Orders
    """

    def __init__(self, input_parameters: dict):
        self.__order_id = self.get_value(
            input_object=input_parameters,
            input_object_property_name="order_id",
            default_value=Order.generate_id(),
        )
        self.__user_email = self.get_value(
            input_object=input_parameters,
            input_object_property_name="user_email",
            mandatory=True,
        )
        self.__user_phonenumber = self.get_value(
            input_object=input_parameters,
            input_object_property_name="user_phonenumber",
            mandatory=True,
        )
        self.__user_address = self.get_value(
            input_object=input_parameters,
            input_object_property_name="user_address",
            mandatory=True,
        )
        self.__restaurant_id = self.get_value(
            input_object=input_parameters,
            input_object_property_name="restaurant_id",
            mandatory=True,
        )
        self.__products = self.get_value(
            input_object=input_parameters,
            input_object_property_name="products",
            mandatory=True,
        )
        self.__subtotal = self.get_value(
            input_object=input_parameters,
            input_object_property_name="subtotal",
            mandatory=True,
        )
        self.__tax = self.get_value(
            input_object=input_parameters,
            input_object_property_name="tax",
            mandatory=True,
        )
        self.__delivery_fee = self.get_value(
            input_object=input_parameters,
            input_object_property_name="delivery_fee",
            mandatory=True,
        )
        self.__total = self.get_value(
            input_object=input_parameters,
            input_object_property_name="total",
            mandatory=True,
        )
        self.__status = self.get_value(
            input_object=input_parameters,
            input_object_property_name="status",
            default_value=OrderStatus.PENDING,
            allowed_values=OrderStatus.__dict__.values(),
        )
        self.__created_at = self.get_value(
            input_object=input_parameters,
            input_object_property_name="created_at",
            default_value=StringHelper.create_datetime(),
        )
        self.__last_modified_at = self.get_value(
            input_object=input_parameters,
            input_object_property_name="last_modified_at",
            default_value=StringHelper.create_datetime(),
        )

    @staticmethod
    def generate_id() -> str:
        return IDHelper.create_id()

    def get_model(self) -> dict:
        return self.get_model_dict()
