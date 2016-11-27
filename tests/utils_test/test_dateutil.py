# -*- coding: utf-8 -*-
import calendar
import datetime
import unittest

import mock
from dateutil.relativedelta import relativedelta

from seismograph.utils import dateutils

HANDLER_STUB = lambda x: x
STUB_DATETIME = datetime.datetime.strptime('21.12.1991', '%d.%m.%Y')
STUB_DATE_FORMAT = '%d-----%Y-----%m'
STUB_DATETIME_FORMAT = '%Y***%m***%d***%H***%M***%S'
STUB_DATE = STUB_DATETIME.date()

STUB_SECONDS_DICT = {'seconds': 1}
STUB_MINUTES_DICT = {'minutes': 1}
STUB_HOURS_DICT = {'hours': 1}
STUB_DAYS_DICT = {'days': 1}
STUB_WEEKS_DICT = {'weeks': 1}
STUB_MONTHS_DICT = {'months': 1}
STUB_YEARS_DICT = {'years': 1}
STUB_DELTA_DICT = {'days': 1, 'seconds': 1}

STUB_SECONDS = datetime.timedelta(**STUB_SECONDS_DICT)
STUB_MINUTES = datetime.timedelta(**STUB_MINUTES_DICT)
STUB_HOURS = datetime.timedelta(**STUB_HOURS_DICT)
STUB_DAYS = datetime.timedelta(**STUB_DAYS_DICT)
STUB_WEEKS = relativedelta(**STUB_WEEKS_DICT)
STUB_MONTHS = relativedelta(**STUB_MONTHS_DICT)
STUB_YEARS = relativedelta(**STUB_YEARS_DICT)
STUB_DELTA = datetime.timedelta(**STUB_DELTA_DICT)


class CommonDateutilCase(unittest.TestCase):
    def test_make_result(self):
        self.assertEqual(dateutils._make_result(STUB_DATE, HANDLER_STUB), STUB_DATE)

    def test_date(self):
        params = [STUB_DATE.year, STUB_DATE.month, STUB_DATE.day, HANDLER_STUB]
        self.assertEqual(dateutils.date(*params), STUB_DATE)

    def test_to_date(self):
        self.assertEqual(dateutils.to_date(STUB_DATETIME, HANDLER_STUB), STUB_DATETIME.date())


class MakeCopyCase(unittest.TestCase):
    def test_with_date(self):
        self.assertEqual(dateutils._make_copy(STUB_DATE), STUB_DATE)

    def test_with_datetime(self):
        self.assertEqual(dateutils._make_copy(STUB_DATETIME), STUB_DATETIME)

    def test_with_illegal_type(self):
        not_date = 'Definetilly not date'
        self.assertRaises(TypeError,dateutils._make_copy, not_date)

    def test_with_explicit_class(self):
        self.assertEqual(dateutils._make_copy(STUB_DATETIME, datetime.datetime), STUB_DATETIME)


class ToStringCase(unittest.TestCase):
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


class ArgsToStringCase(unittest.TestCase):
    arg_is_str = lambda self, arg: type(arg) is str
    arg_is_zero = lambda self ,arg: arg == 0

    def test_with_date_args(self):
        wrapped_func = dateutils.date_args_to_string(None)(self.arg_is_str)
        self.assertTrue(wrapped_func(STUB_DATE))

    def test_with_no_date_args(self):
        wrapped_func = dateutils.date_args_to_string(None)(self.arg_is_zero)
        self.assertTrue(wrapped_func(0))

    def test_with_date_kwargs(self):
        wrapped_func = dateutils.date_args_to_string(None)(self.arg_is_str)
        self.assertTrue(wrapped_func(arg=STUB_DATE))

    def test_with_custom_format(self):
        wrapped_func = dateutils.date_args_to_string(STUB_DATE_FORMAT)(self.arg_is_str)
        self.assertTrue(wrapped_func(STUB_DATE))

class DeltaCase(unittest.TestCase):
    def test_minus_delta(self):
        right_value = STUB_DATE - STUB_DELTA
        self.assertEqual(dateutils.minus_delta(STUB_DATE, **STUB_DELTA_DICT), right_value)

    def test_plus_delta(self):
        right_value = STUB_DATE + STUB_DELTA
        self.assertEqual(dateutils.plus_delta(STUB_DATE, **STUB_DELTA_DICT), right_value)

    def test_minus_seconds(self):
        right_value = STUB_DATE - STUB_SECONDS
        self.assertEqual(dateutils.minus_seconds(STUB_DATE, **STUB_SECONDS_DICT), right_value)

    def test_plus_seconds(self):
        right_value = STUB_DATE + STUB_SECONDS
        self.assertEqual(dateutils.plus_seconds(STUB_DATE, **STUB_SECONDS_DICT), right_value)

    def test_minus_minutes(self):
        right_value = STUB_DATE - STUB_MINUTES
        self.assertEqual(dateutils.minus_minutes(STUB_DATE, **STUB_MINUTES_DICT), right_value)

    def test_plus_minutes(self):
        right_value = STUB_DATE + STUB_MINUTES
        self.assertEqual(dateutils.plus_minutes(STUB_DATE, **STUB_MINUTES_DICT), right_value)

    def test_minus_hours(self):
        right_value = STUB_DATE - STUB_HOURS
        self.assertEqual(dateutils.minus_hours(STUB_DATE, **STUB_HOURS_DICT), right_value)

    def test_plus_hours(self):
        right_value = STUB_DATE + STUB_HOURS
        self.assertEqual(dateutils.plus_hours(STUB_DATE, **STUB_HOURS_DICT), right_value)

    def test_minus_days(self):
        right_value = STUB_DATE - STUB_DAYS
        self.assertEqual(dateutils.minus_days(STUB_DATE, **STUB_DAYS_DICT), right_value)

    def test_plus_days(self):
        right_value = STUB_DATE + STUB_DAYS
        self.assertEqual(dateutils.plus_days(STUB_DATE, **STUB_DAYS_DICT), right_value)

    def test_minus_weeks(self):
        right_value = STUB_DATE - STUB_WEEKS
        self.assertEqual(dateutils.minus_weeks(STUB_DATE, **STUB_WEEKS_DICT), right_value)

    def test_plus_weeks(self):
        right_value = STUB_DATE + STUB_WEEKS
        self.assertEqual(dateutils.plus_weeks(STUB_DATE, **STUB_WEEKS_DICT), right_value)

    def test_minus_months(self):
        right_value = STUB_DATE - STUB_MONTHS
        self.assertEqual(dateutils.minus_months(STUB_DATE, **STUB_MONTHS_DICT), right_value)

    def test_plus_months(self):
        right_value = STUB_DATE + STUB_MONTHS
        self.assertEqual(dateutils.plus_months(STUB_DATE, **STUB_MONTHS_DICT), right_value)

    def test_minus_years(self):
        right_value = STUB_DATE - STUB_YEARS
        self.assertEqual(dateutils.minus_years(STUB_DATE, **STUB_YEARS_DICT), right_value)

    def test_plus_years(self):
        right_value = STUB_DATE + STUB_YEARS
        self.assertEqual(dateutils.plus_years(STUB_DATE, **STUB_YEARS_DICT), right_value)


class TransforDateCase(unittest.TestCase):
    def test_to_start_month(self):
        right_value = STUB_DATETIME.replace(day=1)
        self.assertEqual(dateutils.to_start_month(STUB_DATETIME, HANDLER_STUB), right_value)

    def test_to_start_year(self):
        right_value = STUB_DATETIME.replace(day=1, month=1)
        self.assertEqual(dateutils.to_start_year(STUB_DATETIME, HANDLER_STUB), right_value)

    def test_to_end_month(self):
        _, end_day = calendar.monthrange(STUB_DATETIME.year, STUB_DATETIME.month, )
        right_value = STUB_DATETIME.replace(day=end_day)
        self.assertEqual(dateutils.to_end_month(STUB_DATETIME, HANDLER_STUB), right_value)


class CurrentTimeCase(unittest.TestCase):
    @mock.patch('seismograph.utils.dateutils._dt.datetime')
    def test_now(self, mock_datetime):
        mock_datetime.now.return_value = STUB_DATETIME
        self.assertEqual(dateutils.now(HANDLER_STUB), STUB_DATETIME)

    @mock.patch('seismograph.utils.dateutils._dt.date')
    def test_today(self, mock_date):
        mock_date.today.return_value = STUB_DATE
        self.assertEqual(dateutils.today(HANDLER_STUB), STUB_DATE)

if __name__ == '__main__':
    unittest.main()