import unittest
from seismograph.utils import common
from seismograph.exceptions import TimeoutException
import mock
import sys

START_TIME_STUB = 1000
END_TIME_STUB = 5000
RETURN_VALUE_STUB = 5
CUSTOM_EXCEPTION_STUB = ZeroDivisionError
TIMEOUT_STUB = 0.00001
DELAY_STUB = 1
CHAIN_LENGTH_STUB = 5
PATH_STUB = 'PATH_STUB'


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

class PythonPathsCase(unittest.TestCase):
    def test_pythonpaths(self):
        common.pythonpaths(PATH_STUB)(lambda: 0)
        self.assertIn(PATH_STUB, sys.path)

    def tearDown(self):
        try:
            sys.path.remove(PATH_STUB)
        except:
            pass

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
        except:
            self.assertGreater(mock_sleep.call_count, 0)


            # def waiting_for(func, timeout=None, exc_cls=None, message=None, delay=None, args=None, kwargs=None):
            #     args = args or tuple()
            #     kwargs = kwargs or dict()
            #
            #     timeout = timeout or 0
            #     message = message or 'Timeout "{}" exceeded'.format(timeout)
            #
            #     if timeout:
            #         t_start = time.time()
            #
            #         while time.time() <= t_start + timeout:
            #             result = func(*args, **kwargs)
            #
            #             if result:
            #                 return result
            #
            #             if delay:
            #                 time.sleep(delay)
            #         else:
            #             if exc_cls:
            #                 raise exc_cls(message)
            #             raise TimeoutException(message)
            #
            #     result = func(*args, **kwargs)
            #
            #     if result:
            #         return result
            #     if exc_cls:
            #         raise exc_cls(message)
            #     raise TimeoutException(message)
