import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_valid_lowercase_keywords(self):
        """ Test Valid Lowercase Keywords"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "boolean break continue else for float if int return void do while true false string",
                "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>",
                101))

    def test_valid_lowercase_uppercase_keywords(self):
        """ Test Valid Lowercase Uppercase Keywords"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "bOoLean bReAk coNtInuE eLSe fOr fLoaT iF iNt rEtuRn vOId Do wHiLe tRUe fALsE sTRiNg",
                "bOoLean,bReAk,coNtInuE,eLSe,fOr,fLoaT,iF,iNt,rEtuRn,vOId,Do,wHiLe,tRUe,fALsE,sTRiNg,<EOF>",
                102))

    def test_sum_operator(self):
        """ Test Special Characters"""
        self.assertTrue(
            TestLexer.checkLexeme("+ - * / ! % || && != == < > <= >= =",
                                  "+,-,*,/,!,%,||,&&,!=,==,<,>,<=,>=,=,<EOF>",
                                  103))

    def test_inline_comment(self):
        """ Test Inline Comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            // This is an inline comment
            """, "<EOF>", 104))

    def test_block_comment(self):
        """ Test Block Comment"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            /*
             This is a block comment
             We are good
             */
            """, "<EOF>", 105))

    def test_mixed_comments(self):
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

    def test_integer_literal(self):
        """ Test Integer Literal"""
        self.assertTrue(
            TestLexer.checkLexeme("0 1 2 3 123 456 123456 123456789",
                                  "0,1,2,3,123,456,123456,123456789,<EOF>",
                                  107))

    def test_real_literal(self):
        """ Test Real Literal"""
        self.assertTrue(
            TestLexer.checkLexeme(
                "1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 11.0 19e3 0.43E-3 118e-42 12. .0823 1.89e-9 0.000000231 6e24",
                "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,11.0,19e3,0.43E-3,118e-42,12.,.0823,1.89e-9,0.000000231,6e24,<EOF>",
                108))

    def test_string_literal(self):
        """ Test String Literal"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            "" "A" "Lets do this"
            """, r''',A,Lets do this,<EOF>''', 109))

    def test_valid_identifiers(self):
        """ Test Valid Identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            a abc aCBbdc aAsVN a_ a_cd345 a_456 a_456er a_bd_456_ _abc _345 _abc345 _abc_345 _123_bcd __ ____ ____345____ _ABC __AbC __134ABc ABC
            """,
                "a,abc,aCBbdc,aAsVN,a_,a_cd345,a_456,a_456er,a_bd_456_,_abc,_345,_abc345,_abc_345,_123_bcd,__,____,____345____,_ABC,__AbC,__134ABc,ABC,<EOF>",
                110))

    def test_invalid_indentifiers(self):
        """ Test Invalid Identifiers"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            123abc 123_abc 00123_123abc
            """, "123,abc,123,_abc,00123,_123abc,<EOF>", 111))

    def test_invalid_comment(self):
        """ Test Invaliid Comments"""
        self.assertTrue(
            TestLexer.checkLexeme(
                r"""
            // inline comment but
            using multiple lines
            /* Unclosed block comment
            """, "using,multiple,lines,/,*,Unclosed,block,comment,<EOF>", 112))

    def test_invalid_real(self):
        """ Test Invalid Real"""
        self.assertTrue(
            TestLexer.checkLexeme("e-12 e12 . 1e 12e 12.05e .05e ee e01",
                                  "e,-,12,e12,Error Token .", 113))

    def test_array_declare(self):
        """ Test Array Declare"""
        self.assertTrue(
            TestLexer.checkLexeme("""int i[5]""", "int,i,[,5,],<EOF>", 114))

    def test_unclose_string_without_endline(self):
        """ Test Unclosed String without Endline"""
        self.assertTrue(
            TestLexer.checkLexeme('   " Hello World  ',
                                  'Unclosed String:  Hello World  ', 115))

    def test_unclose_string_with_endline(self):
        """ Test Unclosed String with Endline"""
        self.assertTrue(
            TestLexer.checkLexeme('" qwerty\n', 'Unclosed String:  qwerty',
                                  116))

    def test_escape_newline(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('" qwe \n rty"" abc \\n xyz"',
                                  'Unclosed String:  qwe ', 117))

    def test_escape_tab(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('" Tab \\t" qwerty', ' Tab \\t,qwerty,<EOF>',
                                  118))

    def test_escape_backspace(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Backspace \\b"', 'Backspace \\b,<EOF>',
                                  119))

    def test_escape_formfeed(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Formfeed \\f"', 'Formfeed \\f,<EOF>', 120))

    def test_escape_cariage_return(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Return \r"', 'Unclosed String: Return ',
                                  121))

    def test_escape_backsplash(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Backslash \\\\ "', 'Backslash \\\\ ,<EOF>',
                                  122))

    def test_illegal_escape_a(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Illegal \\a"',
                                  'Illegal Escape In String: Illegal \\a',
                                  123))

    def test_illegal_escape_c_d(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Illegal \\c \\d"',
                                  'Illegal Escape In String: Illegal \\c',
                                  124))

    def test_illegal_escape_m(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"Illegal \\m\\n\\c\\s\\d\\f "',
                                  'Illegal Escape In String: Illegal \\m',
                                  125))

    def test_unclose_multi_lines(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('''
"Newline
    multiple lines
"''', 'Unclosed String: Newline', 126))

    def test_single_quote_in_string(self):
        """ Test Single Quote In String"""
        self.assertTrue(
            TestLexer.checkLexeme('" qwer ` ty"', ' qwer ` ty,<EOF>', 127))

    def test_string_good(self):
        """ Test String Error"""
        self.assertTrue(
            TestLexer.checkLexeme(r'''"qwer ' ty"''', r'''qwer ' ty,<EOF>''',
                                  128))

    def test_escape_singlequote(self):
        """ Test Escape"""
        self.assertTrue(
            TestLexer.checkLexeme('''"qwer \' ty"''', '''qwer \' ty,<EOF>''',
                                  129))

    def test_espace_double_quotes(self):
        """ Test Escape String"""
        self.assertTrue(
            TestLexer.checkLexeme('"qwer \" ty"', 'qwer ,ty,Unclosed String: ',
                                  130))

    def test_illegal_escape(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                '''"qwe" 123 __123 "qwe rty"
" qwe \z "
''', '''qwe,123,__123,qwe rty,Illegal Escape In String:  qwe \z''', 131))

    def test_illegal_token_1(self):
        self.assertTrue(
            TestLexer.checkLexeme('!== != & ^ % $ # ... \ ',
                                  '!=,=,!=,Error Token &', 132))

    def test_legal_token(self):
        self.assertTrue(
            TestLexer.checkLexeme('if (a != b) {}', 'if,(,a,!=,b,),{,},<EOF>',
                                  133))

    def test_illegal_token_2(self):
        self.assertTrue(
            TestLexer.checkLexeme('a = a $ 1', 'a,=,a,Error Token $', 134))

    def test_illegal_token_3(self):
        self.assertTrue(
            TestLexer.checkLexeme('''xyz
&a=b''', 'xyz,Error Token &', 135))

    def test_illegal_token_4(self):
        self.assertTrue(
            TestLexer.checkLexeme('#define CONSTANTS', 'Error Token #', 136))

    def test_int_with_many_zeros(self):
        self.assertTrue(
            TestLexer.checkLexeme('1200001213 0000012421 0000004122144',
                                  '1200001213,0000012421,0000004122144,<EOF>',
                                  137))

    def test_float_with_many_zeros(self):
        self.assertTrue(
            TestLexer.checkLexeme('00001.1234567 0e-4 000000001e-40000',
                                  '00001.1234567,0e-4,000000001e-40000,<EOF>',
                                  138))

    def test_illegal_escape_5(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                '''"abc - xyz" "abc \\c xyz"''',
                'abc - xyz,Illegal Escape In String: abc \\c', 139))

    def test_illegal_escape_6(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'"abc - xyz" "abc \qwe"',
                r'abc - xyz,Illegal Escape In String: abc \q', 140))

    def test_illegal_escape_7(self):
        self.assertTrue(
            TestLexer.checkLexeme(r'"qwe \\ rty"', r'qwe \\ rty,<EOF>', 141))

    def test_short_backsplash_escape(self):
        self.assertTrue(TestLexer.checkLexeme('"\\\\"', '\\\\,<EOF>', 142))

    def test_short_backsplash_spacing_escape(self):
        self.assertTrue(TestLexer.checkLexeme('"\\\\ "', '\\\\ ,<EOF>', 143))

    def test_unclose_string_escape(self):
        self.assertTrue(
            TestLexer.checkLexeme('"\\" ', 'Unclosed String: \\" ', 144))

    def test_closed_string_escape(self):
        self.assertTrue(TestLexer.checkLexeme(r'"\""', r'\",<EOF>', 145))

    def test_invalid_close_string(self):
        self.assertTrue(
            TestLexer.checkLexeme(r'''
s = "string
"a = 4''', 's,=,Unclosed String: string', 146))

    def test_complex(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'''
int max(int x, int y) 
{ 
    if (x > y) 
      return x; 
    else
      return y; 
}''', 'int,max,(,int,x,,,int,y,),{,if,(,x,>,y,),return,x,;,else,return,y,;,},<EOF>',
                147))

    def test_other_complex(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'''
void printFibonacci(int n){    
    static int n1=0,n2=1,n3;    
    if(n>0){    
         n3 = n1 + n2;    
         n1 = n2;    
         n2 = n3;    
         printf("%d ",n3);    
         printFibonacci(n-1);    
    }    
}   
''', r'void,printFibonacci,(,int,n,),{,static,int,n1,=,0,,,n2,=,1,,,n3,;,if,(,n,>,0,),{,n3,=,n1,+,n2,;,n1,=,n2,;,n2,=,n3,;,printf,(,%d ,,,n3,),;,printFibonacci,(,n,-,1,),;,},},<EOF>',
                148))

    def test_maybe_other_complex_func(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'''
int main(){  
  int i,j,k,l,n;    
system("cls");  
printf("enter the range=");    
scanf("%d",&n);    
for(i=1;i<=n;i++)    
{    
for(j=1;j<=n-i;j++)    
{    
printf(" ");    
}    
for(k=1;k<=i;k++)    
{    
printf("%d",k);    
}    
for(l=i-1;l>=1;l--)    
{    
printf("%d",l);    
}    
`printf("\n");    
}    
return 0;  
}  ''', 'int,main,(,),{,int,i,,,j,,,k,,,l,,,n,;,system,(,cls,),;,printf,(,enter the range=,),;,scanf,(,%d,,,Error Token &',
                149))

    def test_int_literal_underscore(self):
        self.assertTrue(
            TestLexer.checkLexeme('45654_1234321', '45654,_1234321,<EOF>',
                                  150))

    def test_int_literal_with_id(self):
        self.assertTrue(
            TestLexer.checkLexeme('456qwe456', '456,qwe456,<EOF>', 151))

    def test_int_literal_uppercase_id(self):
        self.assertTrue(
            TestLexer.checkLexeme('214215FNDJ_1234', '214215,FNDJ_1234,<EOF>',
                                  152))

    def test_int_literal(self):
        self.assertTrue(
            TestLexer.checkLexeme('123456765', '123456765,<EOF>', 153))

    def test_int_literal_zero_begin(self):
        self.assertTrue(
            TestLexer.checkLexeme('0987654321', '0987654321,<EOF>', 154))

    def test_seperators_squareB(self):
        self.assertTrue(
            TestLexer.checkLexeme('[I6A0LAxaR5]', '[,I6A0LAxaR5,],<EOF>', 155))

    def test_seperators_paren(self):
        self.assertTrue(
            TestLexer.checkLexeme('(12321_213213)', '(,12321,_213213,),<EOF>',
                                  156))

    def test_seperators_brackets(self):
        self.assertTrue(
            TestLexer.checkLexeme('{oGGdKy3gko}', '{,oGGdKy3gko,},<EOF>', 157))

    def test_seperators_semi(self):
        self.assertTrue(
            TestLexer.checkLexeme('FDiIVDiGl5;', 'FDiIVDiGl5,;,<EOF>', 158))

    def test_seperators_comma(self):
        self.assertTrue(
            TestLexer.checkLexeme('CbWySIaVAE,', 'CbWySIaVAE,,,<EOF>', 159))

    def test_operator_double_plus(self):
        self.assertTrue(TestLexer.checkLexeme('++', '+,+,<EOF>', 160))

    def test_operator_double_subtract(self):
        self.assertTrue(TestLexer.checkLexeme('--', '-,-,<EOF>', 161))

    def test_operator_double_mul(self):
        self.assertTrue(TestLexer.checkLexeme('**', '*,*,<EOF>', 162))

    def test_operator_double_div(self):
        self.assertTrue(TestLexer.checkLexeme('/', '/,<EOF>', 163))

    def test_operator_double_mod(self):
        self.assertTrue(TestLexer.checkLexeme('%', '%,<EOF>', 164))

    def test_operator_eq_not(self):
        self.assertTrue(TestLexer.checkLexeme('!==!', '!=,=,!,<EOF>', 165))

    def test_operator_or_error_token(self):
        self.assertTrue(TestLexer.checkLexeme('|||', '||,Error Token |', 166))

    def test_operator_eq_noteq(self):
        self.assertTrue(TestLexer.checkLexeme('!===', '!=,==,<EOF>', 167))

    def test_operator_less_leq(self):
        self.assertTrue(TestLexer.checkLexeme('<<=', '<,<=,<EOF>', 168))

    def test_operator_greater_geq(self):
        self.assertTrue(TestLexer.checkLexeme('>>=', '>,>=,<EOF>', 169))

    def test_operator_and_error(self):
        self.assertTrue(TestLexer.checkLexeme('&&&', '&&,Error Token &', 170))

    def test_float_with_dot(self):
        self.assertTrue(TestLexer.checkLexeme('123.123', '123.123,<EOF>', 171))

    def test_float_with_dot_and_E(self):
        self.assertTrue(
            TestLexer.checkLexeme('12321.21E3213', '12321.21E3213,<EOF>', 172))

    def test_float_with_dot_and_e_and_minus(self):
        self.assertTrue(
            TestLexer.checkLexeme('65460.123e-1234', '65460.123e-1234,<EOF>',
                                  173))

    def test_float_no_digits_after_dot(self):
        self.assertTrue(TestLexer.checkLexeme('234231.', '234231.,<EOF>', 174))

    def test_float_no_digits_before_dot(self):
        self.assertTrue(
            TestLexer.checkLexeme('.123E-123', '.123E-123,<EOF>', 175))

    def test_float_no_digits_before_dot_1(self):
        self.assertTrue(
            TestLexer.checkLexeme('.123e213', '.123e213,<EOF>', 176))

    def test_float_only_dot(self):
        self.assertTrue(TestLexer.checkLexeme('.', 'Error Token .', 177))

    def test_float_dot_nextto_e(self):
        self.assertTrue(
            TestLexer.checkLexeme('123.e-123', '123.e-123,<EOF>', 178))

    def test_float_dot_nextto_E(self):
        self.assertTrue(
            TestLexer.checkLexeme('435.E654', '435.E654,<EOF>', 179))

    def test_float_with_operator(self):
        self.assertTrue(
            TestLexer.checkLexeme('.4.5*-1.e4', '.4,.5,*,-,1.e4,<EOF>', 180))

    def test_float_with_int(self):
        self.assertTrue(
            TestLexer.checkLexeme('.4.5*-1.e4 4', '.4,.5,*,-,1.e4,4,<EOF>',
                                  181))

    def test_neg_integer(self):
        self.assertTrue(TestLexer.checkLexeme('-456', '-,456,<EOF>', 182))

    def test_none_integer_and_int(self):
        self.assertTrue(
            TestLexer.checkLexeme('_456 75386', '_456,75386,<EOF>', 182))

    def test_integer_and_quote(self):
        self.assertTrue(
            TestLexer.checkLexeme("123'123", "123,Error Token '", 183))

    def test_err_special_char(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" a&&b||c` """,
                                  """a,&&,b,||,c,Error Token `""", 184))

    def test_wrong_op(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" _abc| | """, """_abc,Error Token |""",
                                  185))

    def test_float_wrong_form(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme(".e-12", "Error Token .", 186))

    def test_separators_semicolon(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("a = 23;", "a,=,23,;,<EOF>",
                                              187))

    def test_2_float_conseq(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1e2.1e4", "1e2,.1e4,<EOF>",
                                              188))

    def test_operators_greater(self):
        """test operators"""
        self.assertTrue(
            TestLexer.checkLexeme("(2+1>=3)==true",
                                  "(,2,+,1,>=,3,),==,true,<EOF>", 189))

    def test_unclose_string_and_empty_str(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "" "123a\\n123 """,
                                  """,Unclosed String: 123a\\n123 """, 190))

    def test_unclose_string_and_str(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "123a\\n""123 """,
                                  """123a\\n,Unclosed String: 123 """, 191))

    def test_two_string(self):
        """test normal string"""
        self.assertTrue(
            TestLexer.checkLexeme('"%+,.=?""abbr457@$^"',
                                  '%+,.=?,abbr457@$^,<EOF>', 192))

    def test_comment(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'''
            /* Hello  */ 
            sdads */

            ''', 'sdads,*,/,<EOF>', 193))

    def test_illegal(self):
        self.assertTrue(
            TestLexer.checkLexeme('"abc \\b abc"', 'abc \\b abc,<EOF>', 194))

    def test_nested_block_comments(self):
        self.assertTrue(
            TestLexer.checkLexeme(
                r'''
            /* dsadasdsa
            /* sdadasdsa d
            */ */
            ''', '*,/,<EOF>', 195))

    def test_unclose_single(self):
        self.assertTrue(TestLexer.checkLexeme('"', 'Unclosed String: ', 196))

    def test_backspace(self):
        self.assertTrue(
            TestLexer.checkLexeme('"Hello \b"', 'Hello \b,<EOF>', 197))

    def test_formfeed(self):
        self.assertTrue(
            TestLexer.checkLexeme('"Hello \f"', 'Hello \f,<EOF>', 198))

    def test_tab(self):
        self.assertTrue(
            TestLexer.checkLexeme('"Hello \t"', 'Hello \t,<EOF>', 199))