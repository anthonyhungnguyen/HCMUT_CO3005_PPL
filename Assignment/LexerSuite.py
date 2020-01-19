import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_1_valid_lowercase_keywords(self):
        """ Test Valid Lowercase Keywords"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "boolean break continue else for float if int return void do while true false string",
                "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>",
                101))

    def test_2_valid_lowercase_uppercase_keywords(self):
        """ Test Valid Lowercase Uppercase Keywords"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "bOoLean bReAk coNtInuE eLSe fOr fLoaT iF iNt rEtuRn vOId Do wHiLe tRUe fALsE sTRiNg",
                "bOoLean,bReAk,coNtInuE,eLSe,fOr,fLoaT,iF,iNt,rEtuRn,vOId,Do,wHiLe,tRUe,fALsE,sTRiNg,<EOF>",
                102))

    def test_3_valid_special_characters(self):
        """ Test Special Characters"""
        self.assertTrue(
            TestLexer.checkLexeme("+ - * / ! % || && != == < > <= >= =",
                                  "+,-,*,/,!,%,||,&&,!=,==,<,>,<=,>=,=,<EOF>",
                                  103))

    def test_4_inline_comment(self):
        """ Test Inline Comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            // This is an inline comment
            """, "<EOF>", 104))

    def test_5_block_comment(self):
        """ Test Block Comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            /*
             This is a block comment
             We are good
             */
            """, "<EOF>", 105))

    def test_6_mixed_comments(self):
        """ Test Mixed Comments"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            // This is an inline comment
            /*
                This is a block comment
                We are so good
                // This is for nested inline comment
            */
            """, "<EOF>", 106))

    def test_7_integer_literal(self):
        """ Test Integer Literal"""
        self.assertTrue(
            TestLexer.checkLexeme("0 1 2 3 123 456 123456 123456789",
                                  "0,1,2,3,123,456,123456,123456789,<EOF>",
                                  107))

    def test_8_real_literal(self):
        """ Test Real Literal"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 11.0 19e3 0.43E-3 118e-42 12. .0823 1.89e-9 0.000000231 6e24",
                "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,11.0,19e3,0.43E-3,118e-42,12.,.0823,1.89e-9,0.000000231,6e24,<EOF>",
                108))

    # def test_9_string_literal(self):
    #     """ Test String Literal"""
    #     self.assertTrue(
    #         TestLexer.checkLexeme(
    #             r"""
    #         "" "A" "Lets do this"
    #         """, ",A,Lets do this,<EOF>", 109))

    def test_10_valid_identifiers(self):
        """ Test Valid Identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            a abc aCBbdc aAsVN a_ a_cd345 a_456 a_456er a_bd_456_ _abc _345 _abc345 _abc_345 _123_bcd __ ____ ____345____ _ABC __AbC __134ABc ABC
            """,
                "a,abc,aCBbdc,aAsVN,a_,a_cd345,a_456,a_456er,a_bd_456_,_abc,_345,_abc345,_abc_345,_123_bcd,__,____,____345____,_ABC,__AbC,__134ABc,ABC,<EOF>",
                110))

    def test_11_invalid_indentifiers(self):
        """ Test Invalid Identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            123abc 123_abc 00123_123abc
            """, "123,abc,123,_abc,00123,_123abc,<EOF>", 111))

    def test_12_invalid_comment(self):
        """ Test Invaliid Comments"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            // inline comment but
            using multiple lines
            /* Unclosed block comment
            """, "using,multiple,lines,/,*,Unclosed,block,comment,<EOF>", 112))

    def test_13_invalid_real(self):
        """ Test Invalid Real"""
        self.assertTrue(
            TestLexer.checkLexeme("e-12 e12 . 1e 12e 12.05e .05e ee e01",
                                  "e,-,12,e12,Error Token .", 113))

#     #Recheck 14

    def test_14_array_declare(self):
        """ Test Array Declare"""
        self.assertTrue(
            TestLexer.checkLexeme(r"""
            int i[5]
            """, "int,i,[,5,],<EOF>", 114))

    def test_15_unclose_string_without_endline(self):
        """ Test Unclosed String without Endline"""
        self.assertTrue(
            TestLexer.checkLexeme(r"""   " Hello World  """,
                                  'Unclosed String: " Hello World  ', 115))

    def test_16_unclose_string_with_endline(self):
        """ Test Unclosed String with Endline"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''
" qwerty
''', r'''Illegal Escape In String: " qwerty

''', 116))

    def test_17_escape(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
" qwe \n rty"
" abc \\n xyz"
            """, r'''" qwe \n rty"," abc \\n xyz",<EOF>''', 117))

    def test_18_escape(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''
" Tab \t " qwerty''', r'" Tab \t ",qwerty,<EOF>', 118))

    def test_19_escape(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''
"Backspace \b"''', r'"Backspace \b",<EOF>', 119))

    def test_20_escape(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''
"Formfeed \f"''', r'"Formfeed \f",<EOF>', 120))

    def test_21_escape(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''
"Return \r"''', r'"Return \r",<EOF>', 121))


#     def test_22_escape(self):
#         """ Test Escape String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(r'''
# "Backslash  \\"''', r'"Backslash  \\",<EOF>', 122))

#     def test_23_illegal_escape(self):
#         """ Test Escape String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(
#                 r'''
# "Illegal \a"''', r'''Illegal Escape In String: "Illegal \a"''', 123))

#     def test_24_illegal_escape(self):
#         """ Test Escape String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(
#                 r'''
# "Illegal \c \d"''', r'''Illegal Escape In String: "Illegal \c \d"''', 124))

#     def test_25_illegal_escape(self):
#         """ Test Escape String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(
#                 r'''
# "Illegal \m\n\c\s\d\\f "''', r'''Illegal Escape In String: "Illegal \m''',
#                 125))

#     def test_26_unclose_multi_lines(self):
#         """ Test Escape String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(
#                 r'''
# "Newline
#     multiple lines
# "''', r'''Illegal Escape In String: "Newline

#     multiple lines

# "''', 126))

#     def test_27_single_quote_in_string(self):
#         """ Test Single Quote In String"""
#         self.assertTrue(
#             TestLexer.checkLexeme(r'''
# " qwer ` ty"''', r'''" qwer ` ty",<EOF>''', 127))

#     def test_28_string_error(self):
#         """ Test String Error"""
#         self.assertTrue(
#             TestLexer.checkLexeme(r'''"qwer ' ty"''', "Unclosed String:  abc ",
#                                   128))

# def test_29_escape_singlequote(self):
#     """ Test Escape"""
#     self.assertTrue(
#         TestLexer.checkLexeme(r'''"qwer \\' ty"''',
#                               r'''"qwer \\' ty",<EOF>''', 129))

# def test_30_espace_double_quotes(self):
#     """ Test Escape String"""
#     self.assertTrue(
#         TestLexer.checkLexeme('''"qwer \" ty"''', '''"qwer \" ty"''', 130))