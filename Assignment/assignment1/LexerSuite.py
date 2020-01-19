import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):    
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('abc', 'abc,<EOF>', 100))
            
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme('aCBbdc', 'aCBbdc,<EOF>', 101))
            
    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme('*p += q[12 * a] + -24 * b++;', '*p,+=,q,[,12,*,a,],+,-24,*,b++,;,<EOF>', 102))
            
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('abc', 'abc,<EOF>', 100))
            
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme('aCBbdc', 'aCBbdc,<EOF>', 101))
            
    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme('*p += q[12 * a] + -24 * b++;', '*p,+=,q,[,12,*,a,],+,-24,*,b++,;,<EOF>', 102))
            
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('abc', 'abc,<EOF>', 100))
            
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme('aCBbdc', 'aCBbdc,<EOF>', 101))
            
    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme('*p += q[12 * a] + -24 * b++;', '*p,+=,q,[,12,*,a,],+,-24,*,b++,;,<EOF>', 102))
            
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('abc', 'abc,<EOF>', 100))
            
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme('aCBbdc', 'aCBbdc,<EOF>', 101))
            
    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme('*p += q[12 * a] + -24 * b++;', '*p,+=,q,[,12,*,a,],+,-24,*,b++,;,<EOF>', 102))
            
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('abc', 'abc,<EOF>', 100))
            
    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme('aCBbdc', 'aCBbdc,<EOF>', 101))
            
    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme('*p += q[12 * a] + -24 * b++;', '*p,+=,q,[,12,*,a,],+,-24,*,b++,;,<EOF>', 102))
        