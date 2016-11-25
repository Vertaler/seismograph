# -*- coding: utf-8 -*-
from seismograph.utils import mp
from ..lib import case
import datetime

INT_VAL = 123
STRING_VAL = "@3274ghfedsj$"


class MPCase(case.BaseTestCase):
    
    def setUp(self):
        self.VALUE_EMPTY_STUB = mp.MPSupportedValue()
        self.VALUE_INT_STUB = mp.MPSupportedValue(value=INT_VAL)
        self.VALUE_STRING_STUB = mp.MPSupportedValue(value=STRING_VAL)
    
    def test_empty_value(self):
        self.assertEqual(self.VALUE_EMPTY_STUB.value, None)

    def test_int_value(self):
        self.assertEqual(self.VALUE_INT_STUB.value, INT_VAL)

    def test_string_value(self):
        self.assertEqual(self.VALUE_STRING_STUB.value, STRING_VAL)

    def test_property_set_int_to_empty(self):
        ANOTHER_INT = 4234
        self.VALUE_EMPTY_STUB.value = ANOTHER_INT
        self.assertEqual(self.VALUE_EMPTY_STUB.value, ANOTHER_INT)
        pass
    
    def test_property_set_int_to_int(self):
        ANOTHER_INT = 423412323        
        self.VALUE_INT_STUB.value = ANOTHER_INT
        self.assertEqual(self.VALUE_INT_STUB.value, ANOTHER_INT)
        pass
    
    def test_property_set_int_to_string(self):
        ANOTHER_INT = 423489        
        self.VALUE_STRING_STUB.value = ANOTHER_INT
        self.assertEqual(self.VALUE_STRING_STUB.value, ANOTHER_INT)
        pass
    
    def test_property_set_string_to_empty(self):
        ANOTHER_STRING = "4234"
        self.VALUE_EMPTY_STUB.value = ANOTHER_STRING
        self.assertEqual(self.VALUE_EMPTY_STUB.value, ANOTHER_STRING)
        pass
    
    def test_property_set_string_to_int(self):
        ANOTHER_STRING = "423412323 "       
        self.VALUE_INT_STUB.value = ANOTHER_STRING
        self.assertEqual(self.VALUE_INT_STUB.value, ANOTHER_STRING)
        pass
    
    def test_property_set_string_to_string(self):
        ANOTHER_STRING = "423489"        
        self.VALUE_STRING_STUB.value = ANOTHER_STRING
        self.assertEqual(self.VALUE_STRING_STUB.value, ANOTHER_STRING)
        pass
    
    def test_set_int_to_empty(self):
        SET_VALUE = 908790765
        self.VALUE_EMPTY_STUB.set(SET_VALUE)
        self.assertEqual(self.VALUE_EMPTY_STUB.value, SET_VALUE)
        pass
    
    def test_set_string_to_empty(self):
        SET_VALUE = "90879076584092"
        self.VALUE_EMPTY_STUB.set(SET_VALUE)
        self.assertEqual(self.VALUE_EMPTY_STUB.value, SET_VALUE)
        pass
