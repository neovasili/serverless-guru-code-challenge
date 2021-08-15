from datetime import datetime
from uuid import uuid4


class StringHelper:
    @staticmethod
    def to_bool(value: str) -> bool:
        return value in ["TRUE", "True", "true"]

    @staticmethod
    def create_datetime():
        return datetime.now().isoformat(sep="T", timespec="auto")


class IDHelper:
    @staticmethod
    def create_id():
        return str(uuid4())


class ApiHelper:
    @staticmethod
    def get_input_data(event: dict) -> dict:
        return event["arguments"]

    @staticmethod
    def get_response(event: dict, item: object) -> dict:
        expected_output = event["info"]["selectionSetList"]
        response = dict()
        item_dict = item.get_model()

        for output in expected_output:
            if output in item_dict:
                response[output] = item_dict[output]
            else:
                response[output] = "empty"

        return response