# -*- coding: utf-8 -*-
import unittest
from seismograph.utils import mp

INT_VAL = 123


class ValueTest:
    def __init__(self, value):
        self.value = value


class MPEmptyValueCase(unittest.TestCase):
    def setUp(self):
        self.VALUE_STUB = mp.MPSupportedValue()

    def test_get_value(self):
        self.assertEqual(self.VALUE_STUB.value, None)

    def test_set_value(self):
        self.VALUE_STUB.value = INT_VAL
        self.assertEqual(self.VALUE_STUB.value, INT_VAL)


class MPPrimitiveValueCase(unittest.TestCase):
    def setUp(self):
        self.VALUE_STUB = mp.MPSupportedValue(INT_VAL)

    def test_get_value(self):
        self.assertEqual(self.VALUE_STUB.value, INT_VAL)

    def test_set_value(self):
        new_value = INT_VAL * 2
        self.VALUE_STUB.value = new_value
        self.assertEqual(self.VALUE_STUB.value, new_value)


class MPObjectValueCase(unittest.TestCase):
    def setUp(self):
        self.VALUE_STUB = mp.MPSupportedValue(ValueTest(INT_VAL))

    def test_get_value(self):
        self.assertEqual(self.VALUE_STUB.value, INT_VAL)

    def test_set_value(self):
        new_value = INT_VAL * 2
        self.VALUE_STUB.value = new_value
        self.assertEqual(self.VALUE_STUB.value, new_value)

    def test_set_value_method(self):
        new_value = INT_VAL * 2
        self.VALUE_STUB.set(new_value)
        self.assertEqual(self.VALUE_STUB.value, new_value)


if __name__ == '__main__':
    unittest.main()
