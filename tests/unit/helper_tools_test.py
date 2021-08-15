import logging
import unittest

from src.helper.tools import (
    StringHelper,
)

logging.disable()


class TestStringHelper(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_convert_true_string_to_bool_should_return_true(self):
        self.assertTrue(StringHelper.to_bool("true"))

    def test_convert_capitilized_true_string_to_bool_should_return_true(self):
        self.assertTrue(StringHelper.to_bool("True"))

    def test_convert_uppercase_true_string_to_bool_should_return_true(self):
        self.assertTrue(StringHelper.to_bool("TRUE"))

    def test_convert_python_true_to_bool_should_return_false(self):
        self.assertFalse(StringHelper.to_bool(True))

    def test_convert_python_false_to_bool_should_return_false(self):
        self.assertFalse(StringHelper.to_bool(False))

    def test_should_create_isoformat_datetime_string(self):
        string_datetime = StringHelper.create_datetime()

        self.assertTrue("T" in string_datetime and len(string_datetime) == 26)

    def tearDown(self):
        return super().tearDown()
