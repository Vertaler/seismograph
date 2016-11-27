import unittest
from seismograph.utils import std

import mock
import sys


class STDCase(unittest.TestCase):
    def setUp(self):
        self.stream_mock = mock.Mock()

    def test_capture_stdout(self):
        with(std.capture_stdout(self.stream_mock)):
            self.assertEqual(sys.stdout, self.stream_mock)

    def test_capture_stderr(self):
        with(std.capture_stderr(self.stream_mock)):
            self.assertEqual(sys.stderr, self.stream_mock)

    def test_capture_output_stdout(self):
        with(std.capture_output(self.stream_mock)):
            self.assertEqual(sys.stdout, self.stream_mock)

    def test_capture_output_stderr(self):
        with(std.capture_output(self.stream_mock)):
            self.assertEqual(sys.stderr, self.stream_mock)


if __name__ == '__main__':
    unittest.main()