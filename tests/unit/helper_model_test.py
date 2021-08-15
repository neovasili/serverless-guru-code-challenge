import unittest

from src.helper.exception import (
    MissingMandatoryInput,
    NotAllowedInputValue,
)
from src.helper.model import ModelHelper


class TestModelHelper(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_should_return_default_value_when_get_desired_and_does_not_exists_in_input(self):
        self.assertEqual(
            ModelHelper.get_desired_value(
                input_object={"test": "test"},
                input_object_property_name="other",
                default_value="default_value",
            ),
            "default_value",
        )

    def test_should_not_return_default_value_when_get_desired_and_exists_in_input(self):
        self.assertNotEqual(
            ModelHelper.get_desired_value(
                input_object={"test": "test"},
                input_object_property_name="test",
                default_value="default_value",
            ),
            "default_value",
        )

    def test_should_raise_exception_when_check_mandatory_and_mandatory_input_is_missing(self):
        with self.assertRaises(MissingMandatoryInput):
            ModelHelper.check_mandatory(
                mandatory=True,
                input_object={"test": "test"},
                input_object_property_name="other",
            )

    def test_should_raise_exception_when_check_allowed_values_and_value_is_not_allowed(self):
        with self.assertRaises(NotAllowedInputValue):
            ModelHelper.check_allowed_values(
                allowed_values=["test"],
                current_value="other",
            )

    def test_should_allow_when_check_allowed_values_and_value_allowed_values_is_none(self):
        ModelHelper.check_allowed_values(
            allowed_values=None,
            current_value="any",
        )
        self.assertTrue(True)

    def test_should_get_value_from_default_when_not_provided_in_input(self):
        self.assertEqual(
            ModelHelper.get_value(
                input_object={"test": "test"},
                input_object_property_name="other",
                default_value="default_value",
            ),
            "default_value",
        )

    def test_should_get_value_when_provided_in_input(self):
        self.assertEqual(
            ModelHelper.get_value(
                input_object={"test": "test"},
                input_object_property_name="test",
                default_value="default_value",
            ),
            "test",
        )

    def test_should_raise_exception_when_get_value_and_mandatory_input_is_not_provided(self):
        with self.assertRaises(MissingMandatoryInput):
            ModelHelper.get_value(
                input_object={"test": "test"},
                input_object_property_name="other",
                mandatory=True,
            )

    def test_should_raise_exception_when_get_value_and_value_is_not_allowed(self):
        with self.assertRaises(NotAllowedInputValue):
            ModelHelper.get_value(
                input_object={"test": "other"},
                input_object_property_name="test",
                allowed_values=["test"],
            )

    def test_get_model_dict_from_child_class(self):
        class ChildClass(ModelHelper):
            def __init__(self):
                self.__private_attr = "test"
                self.public_attr = "test"

        expected_dict = {
            "private_attr": "test",
            "public_attr": "test",
        }

        self.assertEqual(ChildClass().get_model_dict(), expected_dict)

    def tearDown(self):
        return super().tearDown()
