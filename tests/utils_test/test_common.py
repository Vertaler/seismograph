import sys
import unittest

import mock

from seismograph.exceptions import TimeoutException
from seismograph.utils import common

START_TIME_STUB = 1000
END_TIME_STUB = 5000
RETURN_VALUE_STUB = 5
CUSTOM_EXCEPTION_STUB = ZeroDivisionError
TIMEOUT_STUB = 0.00001
DELAY_STUB = 1
CHAIN_LENGTH_STUB = 5
PATH_STUB = 'PATH_STUB'
LIST_OF_DICTS_STUB = [{'k1': 1, 'k2': 2}]
CORRECT_PATTERN_STUB = {'k1': 1, 'k2': 2}
INCORRECT_PATTERN_STUB = {'k1': 1, 'k2': 5}

DICT1_STUB = {
    'list': [{'k1': {'k2': 5, 'k3': 7}}, {'k1': 1}],
    'dict': {'k1': {'k1': 5}, 'k2': {'k3': '1'}},
    'val': 5,
    'not_in_dict2': 1
}
DICT2_STUB = {
    'list': [{'k1': 5}, {'k3': '1'}],
    'dict': {'k1': {'k3': 5}},
    'val': 4
}
REDUCE_DICT_RESULT = {
    'list': [{}, {'k1': {'k2': 5, 'k3': 7}}],
    'dict': {'k1': {}},
    'val': 5
}

LIST1_STUB = [
    [{'k1': {'k2': 5, 'k3': 7}}, {'k1': 1}],
    {'k1': {'k1': 5}, 'k2': {'k3': '1'}},
    5,
]
LIST2_STUB = [
    [{'k1': 5}, {'k3': '1'}],
    {'k1': {'k3': 5}},
    4
]
REDUCE_LIST_RESULT = [
    5,
    {'k1': {}},
    ([{}, {'k1': {'k3': 7, 'k2': 5}}], [{'k1': 5}, {'k3': '1'}]),
]


class CommonCase(unittest.TestCase):
    @mock.patch('seismograph.utils.common.time')
    def test_measure(self, mock_time):
        mock_time.time.return_value = START_TIME_STUB
        measure_func = common.measure_time()
        mock_time.time.return_value = END_TIME_STUB
        right_value = END_TIME_STUB - START_TIME_STUB
        self.assertEqual(measure_func(), right_value)

    def test_call_to_chain(self):
        mock_func = mock.Mock()
        chain = CHAIN_LENGTH_STUB * [mock_func]
        common.call_to_chain(chain, None)
        self.assertEqual(mock_func.call_count, len(chain))

    def test_call_to_chain_with_internal_func(self):
        mock_obj = mock.Mock()
        mock_obj.mock_func = mock.Mock()
        chain = CHAIN_LENGTH_STUB * [mock_obj]
        common.call_to_chain(chain, 'mock_func')
        self.assertEqual(mock_obj.mock_func.call_count, len(chain))

    def test_get_dict_from_list(self):
        self.assertDictEqual(common.get_dict_from_list(LIST_OF_DICTS_STUB, **CORRECT_PATTERN_STUB),
                             CORRECT_PATTERN_STUB)

    def test_get_dict_from_list_without_pattern(self):
        self.assertEqual(common.get_dict_from_list(LIST_OF_DICTS_STUB), LIST_OF_DICTS_STUB)

    def test_get_fict_from_list_with_incorrect_pattern(self):
        self.assertRaises(LookupError, common.get_dict_from_list, LIST_OF_DICTS_STUB, **INCORRECT_PATTERN_STUB)


class DictReduceCase(unittest.TestCase):
    def setUp(self):
        self.dict1 = dict(DICT1_STUB)

    def test_reduce_dict(self):
        self.assertDictEqual(common.reduce_dict(self.dict1, DICT2_STUB), REDUCE_DICT_RESULT)

    def test_with_different_lists_length(self):
        self.assertRaises(AssertionError, common.reduce_dict, self.dict1, {'list': []})


class ListReduceCase(unittest.TestCase):
    def setUp(self):
        self.list2 = list(LIST2_STUB)

    def test_first_return_value(self):
        result, _ = common.reduce_list(LIST1_STUB, self.list2)
        self.assertListEqual(result, REDUCE_LIST_RESULT)

    def test_second_return_value(self):
        def deepsort(lst):
            result = list(lst)
            map(lambda l: deepsort(l) if isinstance(l, list) else l, result)
            result.sort()
            return result

        expected_result = deepsort(self.list2)
        _, result = common.reduce_list(LIST1_STUB, self.list2)
        self.assertListEqual(result, expected_result)

    def test_with_different_length(self):
        self.assertRaises(AssertionError, common.reduce_list, LIST1_STUB, [])


class PythonPathsCase(unittest.TestCase):
    def test_pythonpaths(self):
        common.pythonpaths(PATH_STUB)(lambda: 0)
        self.assertIn(PATH_STUB, sys.path)

    def tearDown(self):
        sys.path.remove(PATH_STUB)


class WaitingForCase(unittest.TestCase):
    def setUp(self):
        self.mock_func = mock.Mock()

    def test_without_timeout(self):
        self.mock_func.return_value = RETURN_VALUE_STUB
        self.assertEqual(common.waiting_for(self.mock_func), RETURN_VALUE_STUB)

    def test_timeout_exception(self):
        self.mock_func.return_value = None
        self.assertRaises(TimeoutException, common.waiting_for, self.mock_func)

    def test_custom_exception(self):
        self.mock_func.return_value = None
        self.assertRaises(
            CUSTOM_EXCEPTION_STUB,
            common.waiting_for,
            self.mock_func,
            exc_cls=CUSTOM_EXCEPTION_STUB
        )

    def test_with_timout(self):
        self.mock_func.return_value = RETURN_VALUE_STUB
        self.assertEqual(common.waiting_for(self.mock_func, TIMEOUT_STUB), RETURN_VALUE_STUB)

    def test_timeout_exception_with_timeout(self):
        self.mock_func.return_value = None
        self.assertRaises(TimeoutException, common.waiting_for, self.mock_func, TIMEOUT_STUB)

    def test_custom_exception_with_timeout(self):
        self.mock_func.return_value = None
        self.assertRaises(
            CUSTOM_EXCEPTION_STUB,
            common.waiting_for,
            self.mock_func,
            TIMEOUT_STUB,
            CUSTOM_EXCEPTION_STUB
        )

    @mock.patch('seismograph.utils.common.time.sleep')
    def test_delay_works(self, mock_sleep):
        self.mock_func.return_value = None
        try:
            common.waiting_for(self.mock_func, TIMEOUT_STUB, delay=DELAY_STUB)
        except TimeoutException:
            pass
        finally:
            self.assertGreater(mock_sleep.call_count, 0)


if __name__ == '__main__':
    unittest.main()
