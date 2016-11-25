# -*- coding: utf-8 -*-
from seismograph.utils import dateutils
from dateutil.relativedelta import relativedelta
import unittest
import datetime

HANDLER_STUB = lambda x: x
STUB_DATETIME = datetime.datetime.strptime('21.12.1991', '%d.%m.%Y')
STUB_DATE_FORMAT = '%d-----%Y-----%m'
STUB_DATETIME_FORMAT = '%Y***%m***%d***%H***%M***%S'
STUB_DATE = STUB_DATETIME.date()

STUB_SECONDS_DICT = {'seconds': 1}
STUB_HOURS_DICT = {'hours': 1}
STUB_DAYS_DICT = {'days': 1}
STUB_WEEKS_DICT = {'weeks':1}
STUB_MONTHS_DICT = {'months' : 1}
STUB_YEARS_DICT = {'years': 1}
STUB_DELTA_DICT = {'days': 1, 'seconds': 1}

STUB_SECONDS = datetime.timedelta(**STUB_SECONDS_DICT)
STUB_HOURS = datetime.timedelta(**STUB_HOURS_DICT)
STUB_DAYS = datetime.timedelta(**STUB_DAYS_DICT)
STUB_WEEKS = relativedelta(**STUB_WEEKS_DICT)
STUB_MONTHS  = relativedelta(**STUB_MONTHS_DICT)
STUB_YEARS   = relativedelta(**STUB_YEARS_DICT)
STUB_DELTA = datetime.timedelta(**STUB_DELTA_DICT)


class DateutilCase(unittest.TestCase):  # TODO Разбить тесты по нескольким кейсам
    def test_make_result(self):
        self.assertEqual(dateutils._make_result(STUB_DATE, HANDLER_STUB), STUB_DATE)

    def test_make_copy_with_date(self):
        self.assertEqual(dateutils._make_copy(STUB_DATE), STUB_DATE)

    def test_make_copy_with_datetime(self):
        self.assertEqual(dateutils._make_copy(STUB_DATETIME), STUB_DATETIME)

    def test_make_copy_with_illegal_type(self):
        not_date = 'Definetilly not date'
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



        # def minus_delta(datetime, **kwargs):
        #     return _make_copy(datetime - _dt.timedelta(**kwargs))
        #
        # def plus_delta(datetime, **kwargs):
        #     return _make_copy(datetime + _dt.timedelta(**kwargs))
        #
        # def minus_seconds(datetime, seconds, *handlers):
        #     return _make_result(minus_delta(datetime, seconds=seconds), *handlers)
        #
        # def plus_seconds(datetime, seconds, *handlers):
        #     return _make_result(plus_delta(datetime, seconds=seconds), *handlers)
        #
        # def minus_minutes(datetime, minutes, *handlers):
        #     return _make_result(minus_delta(datetime, minutes=minutes), *handlers)
        #
        # def plus_minutes(datetime, minutes, *handlers):
        #     return _make_result(plus_delta(datetime, minutes=minutes), *handlers)
        #
        # def minus_hours(datetime, hours, *handlers):
        #     return _make_result(minus_delta(datetime, hours=hours), *handlers)
        #
        # def plus_hours(datetime, hours, *handlers):
        #     return _make_result(plus_delta(datetime, hours=hours), *handlers)
        #
        # def minus_days(datetime, days, *handlers):
        #     return _make_result(minus_delta(datetime, days=days), *handlers)
        #
        # def plus_days(datetime, days, *handlers):
        #     return _make_result(plus_delta(datetime, days=days), *handlers)
        #
        # def minus_weeks(datetime, weeks, *handlers):
        #     return _make_result(minus_delta(datetime, weeks=weeks), *handlers)
        #
        # def plus_weeks(datetime, weeks, *handlers):
        #     return _make_result(plus_delta(datetime, weeks=weeks), *handlers)
        #
        # def minus_months(datetime, months, *handlers):
        #     return _make_result(_make_copy(datetime - relativedelta(months=months)), *handlers)
        #
        # def plus_months(datetime, months, *handlers):
        #     return _make_result(_make_copy(datetime - relativedelta(months=-months)), *handlers)
        #
        # def minus_years(datetime, years, *handlers):
        #     return _make_result(_make_copy(datetime - relativedelta(years=years)), *handlers)
        #
        # def plus_years(datetime, years, *handlers):
        #     return _make_result(_make_copy(datetime - relativedelta(years=-years)), *handlers)
        #
        # def to_start_month(datetime, *handlers):
        #     return _make_result(_make_copy(datetime.replace(day=1)), *handlers)
        #
        # def to_start_year(datetime, *handlers):
        #     return _make_result(_make_copy(datetime.replace(day=1, month=1)), *handlers)
        #
        # def to_end_month(datetime, *handlers):
        #     _, end_day = calendar.monthrange(datetime.year, datetime.month)
        #     return _make_result(_make_copy(datetime.replace(day=end_day)), *handlers)
        #
        # def to_date(date, *handlers):
        #     return _make_result(_dt.date(date.year, date.month, date.day), *handlers)
        #
        # def now(*handlers):
        #     return _make_result(_dt.datetime.now(), *handlers)
        #
        # def date(year, month, day, *handlers):
        #     return _make_result(_dt.date(year, month, day), *handlers)
        #
        # def today(*handlers):
        #     return _make_result(_dt.date.today(), *handlers)
