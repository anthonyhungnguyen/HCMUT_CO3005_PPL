import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_200(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))
