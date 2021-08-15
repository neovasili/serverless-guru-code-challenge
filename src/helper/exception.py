class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__message = message

    def __str__(self):
        return str(self.__message)


class MissingMandatoryInput(CustomException):
    def __init__(self, message: str = None):
        super().__init__("Missing some mandatory input" if message is None else message)


class NotAllowedInputValue(CustomException):
    def __init__(self, message: str = None):
        super().__init__("Current input is not allowed" if message is None else message)