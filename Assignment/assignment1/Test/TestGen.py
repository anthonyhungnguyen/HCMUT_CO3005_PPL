import os, xlrd

# Path
path = os.path.dirname(os.path.abspath(__file__))
# Lexer Test Gen
# Open excel file
lexerFileOK = True
try:
    wb = xlrd.open_workbook('{}\\testLexer.xlsx'.format(path))
    sheet = wb.sheet_by_index(0)
except (xlrd.XLRDError, IOError):
    lexerFileOK = False
# Empty test.txt file

file = open('{}\\LexerSuite.py'.format(path), 'w')
file.write("""import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):""")
file.close()

# Write to file testLexer
if (lexerFileOK):
    for i in range(1, sheet.nrows):
        test_number = i + 99
        test = sheet.cell_value(i, 0)
        expect = sheet.cell_value(i, 1)
        structure = """    
    def test_{}(self):
        self.assertTrue(TestLexer.checkLexeme('{}', '{}', {}))
        """.format(test_number, test, expect, test_number)
        # Write function to file
        file = open('LexerSuite.py', 'a')
        file.write(structure)
        file.close()
else:
    print('Double check your file.')

# Parser Test Gen
# Open excel file
parserFileOk = True
try:
    wb = xlrd.open_workbook('{}\\testParser.xlsx'.format(path))
    sheet = wb.sheet_by_index(0)
except (xlrd.XLRDError, IOError):
    parserFileOk = False

# Empty test.txt file

file = open('{}\\ParserSuite.py'.format(path), 'w')
file.write("""import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):  """)
file.close()

# Write to file testParser
if (parserFileOk):
    for i in range(1, sheet.nrows):
        test_number = i + 199
        test = r'"""' + sheet.cell_value(i, 0) + r'"""'
        expect = r'"' + sheet.cell_value(i, 1) + r'"'
        structure = """    
    def test_{}(self):
        input = {}
        expect = {}
        self.assertTrue(TestParser.checkParser(input, expect, {}))
        """.format(test_number, test, expect, test_number)
        # Write function to file
        file = open('ParserSuite.py', 'a')
        file.write(structure)
        file.close()
else:
    print('Double check your file.')