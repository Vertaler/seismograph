import unittest
from seismograph.utils import colors
import re

STUB_TEXT = "stub"
from ..lib import case

COLOR_CODES = {
    "red":   '\033\[31m',
    "blue":  "\033\[34m",
    "green":  "\033\[32m",
    "yellow": "\033\[33m",
}


class ColorCase(case.BaseTestCase):
    def get_regex(self, color):
        return re.compile( '^' + COLOR_CODES[color] + STUB_TEXT )

    def checkYellow(self):
        self.assertRegexpMatches(colors.yellow(STUB_TEXT), self.get_regex("yellow"))

    def checkGreen(self):
        self.assertRegexpMatches( colors.green(STUB_TEXT) , self.get_regex("green"))

    def checkRed(self):
        self.assertRegexpMatches(colors.red(STUB_TEXT), self.get_regex("red"))

    def checkBlue(self):
        self.assertRegexpMatches(colors.blue(STUB_TEXT), self.get_regex("blue"))

    def runTest(self):
        self.checkBlue()
        self.checkGreen()
        self.checkRed()
        self.checkYellow()


if __name__ == '__main__':
    unittest.main()
