import unittest
from types import ClassType

import mock

from seismograph.utils import pyv

INCORRECT_SYS_VER_STUB = 1
NON_CLASS_TYPE_STUB = 'str'
EXCEPTION_MESSAGE_STUB = 'EXCEPTION_MESSAGE_STUB'
ARGS_COUNT_STUB = 3
FUNC_NAME_STUB = 'FUNC_NAME_STUB'


class PyvTestCase(unittest.TestCase):
    @mock.patch('sys.version_info')
    def test_check_version_sys_info(self, mock_sys_ver):
        mock_sys_ver.return_value = INCORRECT_SYS_VER_STUB
        self.assertRaises(pyv.PyVersionError, pyv.check_py_version)

    def test_check_versions(self):
        pyv.IS_PYTHON_3 = False
        pyv.IS_PYTHON_2 = False
        self.assertRaises(pyv.PyVersionError, pyv.check_py_version)

    def test_classtype_python2(self):
        pyv.IS_PYTHON_2 = True
        self.assertTrue(pyv.is_class_type(ClassType))

    def test_classtype_python2_with_incorrect_type(self):
        pyv.IS_PYTHON_2 = True
        self.assertFalse(pyv.is_class_type(NON_CLASS_TYPE_STUB))

    def test_classtype_python3(self):
        pyv.IS_PYTHON_2 = False
        self.assertTrue(pyv.is_class_type(ClassType))

    def test_classtype_python3_with_incorrect_type(self):
        pyv.IS_PYTHON_2 = False
        self.assertFalse(pyv.is_class_type(NON_CLASS_TYPE_STUB))

    def test_get_exc_message(self):
        exception_mock = mock.Mock()
        exception_mock.message = EXCEPTION_MESSAGE_STUB
        self.assertEqual(pyv.get_exc_message(exception_mock), EXCEPTION_MESSAGE_STUB)

    def test_get_exc_message_without_message_property(self):
        exception_mock = mock.Mock()
        del exception_mock.message
        exception_mock.args = ARGS_COUNT_STUB * [EXCEPTION_MESSAGE_STUB]
        right_value = ''.join(exception_mock.args)
        self.assertEqual(pyv.get_exc_message(exception_mock), right_value)

    def test_get_func_name_with_object(self):
        mock_object = mock.Mock()
        mock_object.func.__name__ = FUNC_NAME_STUB
        mock_object.__func__ = mock_object.func
        self.assertEqual(pyv.get_func_name(mock_object), FUNC_NAME_STUB)

    def test_get_func_name_with_function(self):
        test_obj = mock.Mock()
        test_obj.__name__ = FUNC_NAME_STUB
        self.assertEqual(pyv.get_func_name(test_obj), FUNC_NAME_STUB)


if __name__ == '__main__':
    unittest.main()
