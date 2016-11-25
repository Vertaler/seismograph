# -*- coding: utf-8 -*-
from seismograph.utils import dateutils
from ..lib import case
import datetime

HANDLER_STUB = lambda x: x
STUB_DATETIME = datetime.datetime.strptime("21.12.1991", "%d.%m.%Y")
STUB_DATE_FORMAT = '%d-----%Y-----%m'
STUB_DATETIME_FORMAT = '%Y***%m***%d***%H***%M***%S'
STUB_DATE = STUB_DATETIME.date()


class DateutilCase(case.BaseTestCase):  # TODO Разбить тесты по нескольким кейсам
    def test_make_result(self):
        self.assertEqual(dateutils._make_result(STUB_DATE, HANDLER_STUB), STUB_DATE)

    def test_make_copy_with_date(self):
        self.assertEqual(dateutils._make_copy(STUB_DATE), STUB_DATE)

    def test_make_copy_with_datetime(self):
        self.assertEqual(dateutils._make_copy(STUB_DATETIME), STUB_DATETIME)

    def test_make_copy_with_illegal_type(self):
        not_date = "Definetilly not date"
        callable = lambda: dateutils._make_copy(not_date)
        self.assertRaises(TypeError, callableObj=callable)

    def test_make_copy_with_explicit_class(self):
        self.assertEqual(dateutils._make_copy(STUB_DATETIME, datetime.datetime), STUB_DATETIME)

    def test_date_to_string(self):
        right_value = STUB_DATE.strftime(dateutils.DEFAULT_DATE_FORMAT)
        self.assertEqual(dateutils.to_string(STUB_DATE), right_value)

    def test_datetime_to_string(self):
        right_value = STUB_DATETIME.strftime(dateutils.DEFAULT_DATETIME_FORMAT)
        self.assertEqual(dateutils.to_string(STUB_DATETIME), right_value)

    def test_date_to_string_with_custom_format(self):
        right_value = STUB_DATE.strftime(STUB_DATE_FORMAT)
        self.assertEqual(dateutils.to_string(STUB_DATE, STUB_DATE_FORMAT), right_value)

    def test_datetime_to_string_with_custom_format(self):
        right_value = STUB_DATETIME.strftime(STUB_DATETIME_FORMAT)
        self.assertEqual(dateutils.to_string(STUB_DATETIME, STUB_DATETIME_FORMAT), right_value)

    def test_date_args_to_string(self):
        arg_is_str = lambda arg: type(arg) is str
        wrapped_func = dateutils.date_args_to_string(None)(arg_is_str)
        self.assertTrue(wrapped_func(STUB_DATE))

    def test_date_args_to_string_with_custom_format(self):
        arg_is_str = lambda arg: type(arg) is str
        wrapped_func = dateutils.date_args_to_string(STUB_DATE_FORMAT)(arg_is_str)
        self.assertTrue(wrapped_func(STUB_DATE))
