from src.helper.exception import (
    MissingMandatoryInput,
    NotAllowedInputValue,
)


class ModelHelper:
    """
    Helper class to ease the production of dict models compatible with dynamodb items
    from any class that extend this one
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_desired_value(input_object: object, input_object_property_name: str, default_value: object):
        if input_object_property_name in input_object:
            return input_object[input_object_property_name]

        return default_value

    @staticmethod
    def check_mandatory(mandatory: bool, input_object: object, input_object_property_name: str):
        if mandatory and input_object_property_name not in input_object:
            raise MissingMandatoryInput

    @staticmethod
    def check_allowed_values(allowed_values: list, current_value: object):
        if allowed_values is None:
            return

        if current_value not in allowed_values:
            raise NotAllowedInputValue

    @staticmethod
    def get_value(
        input_object: object,
        input_object_property_name: str,
        default_value: object = None,
        mandatory: bool = False,
        allowed_values: list = None,
    ):
        ModelHelper.check_mandatory(
            mandatory=mandatory,
            input_object=input_object,
            input_object_property_name=input_object_property_name,
        )

        desired_value = ModelHelper.get_desired_value(
            input_object=input_object,
            input_object_property_name=input_object_property_name,
            default_value=default_value,
        )

        ModelHelper.check_allowed_values(
            allowed_values=allowed_values,
            current_value=desired_value,
        )

        return desired_value

    @staticmethod
    def clean_dict_key_name(key_name: str):
        private_property_pattern = "__"

        return key_name.split(private_property_pattern)[1] if private_property_pattern in key_name else key_name

    def get_model_dict(self):
        current_model = self.__dict__
        model_dict = dict()

        for key, value in current_model.items():
            model_dict[self.clean_dict_key_name(key_name=key)] = value

        return model_dict
