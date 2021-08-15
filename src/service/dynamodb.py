import json

from decimal import Decimal

from src.helper.boto import BotoResourceHelper
from src.helper.exception import (
    CannotGetDataFromDatabase,
    CannotSaveDataIntoDatabase,
)


class DynamoDBService(BotoResourceHelper):
    def __init__(self, table_name: str):
        super().__init__("dynamodb")
        self.__table = self.resource.Table(table_name)

    def find(self, id_name: str, item_id: str) -> dict:
        try:
            result = self.__table.get_item(Key={id_name: item_id})
            return result["Item"] if "Item" in result else None
        except Exception as error:
            raise CannotGetDataFromDatabase(str(error))

    def save(self, item: dict) -> dict:
        try:
            dynamodb_record = json.loads(json.dumps(item), parse_float=Decimal)
            response = self.__table.put_item(Item=dynamodb_record)
            return response
        except Exception as error:
            raise CannotSaveDataIntoDatabase(str(error))
