import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_1_valid_lowercase_keywords(self):
        """ Test Valid Lowercase Keywords"""
        self.assertTrue(
            TestLexer.test(
                "boolean break continue else for float if int return void do while true false string",
                "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>",
                100))
