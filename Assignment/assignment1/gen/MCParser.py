# Generated from C:/Users/Admin/Desktop/Computer Science/Junior/Principles of Programming Languages (CO3005)/Assignment/assignment1/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0103\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\6\28\n\2\r\2\16\29\3\2\3")
        buf.write("\2\3\3\3\3\5\3@\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5I\n")
        buf.write("\5\f\5\16\5L\13\5\3\6\3\6\3\6\3\6\5\6R\n\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7X\n\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b`\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tk\n\t\3\n\3\n\3\n\7\n")
        buf.write("p\n\n\f\n\16\ns\13\n\3\13\3\13\3\13\3\13\5\13y\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0087")
        buf.write("\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u009e\n\f\f\f\16")
        buf.write("\f\u00a1\13\f\3\r\3\r\3\r\3\r\5\r\u00a7\n\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00b3\n")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\7\21\u00ba\n\21\f\21\16\21")
        buf.write("\u00bd\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00c7\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00d0\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u00eb\n\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\32\3\32\7\32\u00f4\n\32\f\32\16\32")
        buf.write("\u00f7\13\32\3\32\7\32\u00fa\n\32\f\32\16\32\u00fd\13")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\2\3\26\34\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\t\4\2\22")
        buf.write("\22\30\30\4\2\21\21\31\32\4\2\20\20\30\30\4\2\25\26\35")
        buf.write("\36\4\2\22\22\34\34\3\2(+\4\2\13\f\16\17\2\u010c\2\67")
        buf.write("\3\2\2\2\4?\3\2\2\2\6A\3\2\2\2\bE\3\2\2\2\nM\3\2\2\2\f")
        buf.write("S\3\2\2\2\16_\3\2\2\2\20j\3\2\2\2\22l\3\2\2\2\24t\3\2")
        buf.write("\2\2\26\u0086\3\2\2\2\30\u00a6\3\2\2\2\32\u00a8\3\2\2")
        buf.write("\2\34\u00aa\3\2\2\2\36\u00af\3\2\2\2 \u00b6\3\2\2\2\"")
        buf.write("\u00c6\3\2\2\2$\u00c8\3\2\2\2&\u00d1\3\2\2\2(\u00d7\3")
        buf.write("\2\2\2*\u00e2\3\2\2\2,\u00e5\3\2\2\2.\u00e8\3\2\2\2\60")
        buf.write("\u00ee\3\2\2\2\62\u00f1\3\2\2\2\64\u0100\3\2\2\2\668\5")
        buf.write("\4\3\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:")
        buf.write(";\3\2\2\2;<\7\2\2\3<\3\3\2\2\2=@\5\6\4\2>@\5\f\7\2?=\3")
        buf.write("\2\2\2?>\3\2\2\2@\5\3\2\2\2AB\5\64\33\2BC\5\b\5\2CD\7")
        buf.write("%\2\2D\7\3\2\2\2EJ\5\n\6\2FG\7&\2\2GI\5\n\6\2HF\3\2\2")
        buf.write("\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\t\3\2\2\2LJ\3\2\2\2")
        buf.write("MQ\7\'\2\2NO\7\37\2\2OP\7(\2\2PR\7 \2\2QN\3\2\2\2QR\3")
        buf.write("\2\2\2R\13\3\2\2\2ST\5\16\b\2TU\7\'\2\2UW\7!\2\2VX\5\22")
        buf.write("\n\2WV\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\"\2\2Z[\5\62\32")
        buf.write("\2[\r\3\2\2\2\\`\5\64\33\2]`\7\r\2\2^`\5\20\t\2_\\\3\2")
        buf.write("\2\2_]\3\2\2\2_^\3\2\2\2`\17\3\2\2\2ab\5\64\33\2bc\7\'")
        buf.write("\2\2cd\7\37\2\2de\7 \2\2ek\3\2\2\2fg\5\64\33\2gh\7\37")
        buf.write("\2\2hi\7 \2\2ik\3\2\2\2ja\3\2\2\2jf\3\2\2\2k\21\3\2\2")
        buf.write("\2lq\5\24\13\2mn\7&\2\2np\5\24\13\2om\3\2\2\2ps\3\2\2")
        buf.write("\2qo\3\2\2\2qr\3\2\2\2r\23\3\2\2\2sq\3\2\2\2tu\5\64\33")
        buf.write("\2ux\7\'\2\2vw\7\37\2\2wy\7 \2\2xv\3\2\2\2xy\3\2\2\2y")
        buf.write("\25\3\2\2\2z{\b\f\1\2{|\7!\2\2|}\5\26\f\2}~\7\"\2\2~\u0087")
        buf.write("\3\2\2\2\177\u0080\7\37\2\2\u0080\u0081\5\30\r\2\u0081")
        buf.write("\u0082\7 \2\2\u0082\u0087\3\2\2\2\u0083\u0084\t\2\2\2")
        buf.write("\u0084\u0087\5\26\f\13\u0085\u0087\5\30\r\2\u0086z\3\2")
        buf.write("\2\2\u0086\177\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0085")
        buf.write("\3\2\2\2\u0087\u009f\3\2\2\2\u0088\u0089\f\n\2\2\u0089")
        buf.write("\u008a\t\3\2\2\u008a\u009e\5\26\f\13\u008b\u008c\f\t\2")
        buf.write("\2\u008c\u008d\t\4\2\2\u008d\u009e\5\26\f\n\u008e\u008f")
        buf.write("\f\b\2\2\u008f\u0090\t\5\2\2\u0090\u009e\5\26\f\t\u0091")
        buf.write("\u0092\f\7\2\2\u0092\u0093\t\6\2\2\u0093\u009e\5\26\f")
        buf.write("\b\u0094\u0095\f\6\2\2\u0095\u0096\7\33\2\2\u0096\u009e")
        buf.write("\5\26\f\7\u0097\u0098\f\5\2\2\u0098\u0099\7\23\2\2\u0099")
        buf.write("\u009e\5\26\f\6\u009a\u009b\f\4\2\2\u009b\u009c\7\27\2")
        buf.write("\2\u009c\u009e\5\26\f\4\u009d\u0088\3\2\2\2\u009d\u008b")
        buf.write("\3\2\2\2\u009d\u008e\3\2\2\2\u009d\u0091\3\2\2\2\u009d")
        buf.write("\u0094\3\2\2\2\u009d\u0097\3\2\2\2\u009d\u009a\3\2\2\2")
        buf.write("\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\27\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a7")
        buf.write("\5\32\16\2\u00a3\u00a7\7\'\2\2\u00a4\u00a7\5\34\17\2\u00a5")
        buf.write("\u00a7\5\36\20\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3\2\2")
        buf.write("\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\31\3")
        buf.write("\2\2\2\u00a8\u00a9\t\7\2\2\u00a9\33\3\2\2\2\u00aa\u00ab")
        buf.write("\7\'\2\2\u00ab\u00ac\7\37\2\2\u00ac\u00ad\7(\2\2\u00ad")
        buf.write("\u00ae\7 \2\2\u00ae\35\3\2\2\2\u00af\u00b0\7\'\2\2\u00b0")
        buf.write("\u00b2\7!\2\2\u00b1\u00b3\5 \21\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\7")
        buf.write("\"\2\2\u00b5\37\3\2\2\2\u00b6\u00bb\5\26\f\2\u00b7\u00b8")
        buf.write("\7&\2\2\u00b8\u00ba\5\26\f\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc!\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c7\5$\23")
        buf.write("\2\u00bf\u00c7\5&\24\2\u00c0\u00c7\5(\25\2\u00c1\u00c7")
        buf.write("\5*\26\2\u00c2\u00c7\5,\27\2\u00c3\u00c7\5.\30\2\u00c4")
        buf.write("\u00c7\5\60\31\2\u00c5\u00c7\5\62\32\2\u00c6\u00be\3\2")
        buf.write("\2\2\u00c6\u00bf\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c1")
        buf.write("\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7#\3\2\2\2\u00c8")
        buf.write("\u00c9\7\3\2\2\u00c9\u00ca\7!\2\2\u00ca\u00cb\5\26\f\2")
        buf.write("\u00cb\u00cc\7\"\2\2\u00cc\u00cf\5\"\22\2\u00cd\u00ce")
        buf.write("\7\4\2\2\u00ce\u00d0\5\"\22\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0%\3\2\2\2\u00d1\u00d2\7\5\2\2\u00d2")
        buf.write("\u00d3\5\"\22\2\u00d3\u00d4\7\6\2\2\u00d4\u00d5\5\26\f")
        buf.write("\2\u00d5\u00d6\7%\2\2\u00d6\'\3\2\2\2\u00d7\u00d8\7\n")
        buf.write("\2\2\u00d8\u00d9\7!\2\2\u00d9\u00da\5\26\f\2\u00da\u00db")
        buf.write("\7%\2\2\u00db\u00dc\5\26\f\2\u00dc\u00dd\7%\2\2\u00dd")
        buf.write("\u00de\5\26\f\2\u00de\u00df\7\"\2\2\u00df\u00e0\5\"\22")
        buf.write("\2\u00e0\u00e1\7%\2\2\u00e1)\3\2\2\2\u00e2\u00e3\7\7\2")
        buf.write("\2\u00e3\u00e4\7%\2\2\u00e4+\3\2\2\2\u00e5\u00e6\7\b\2")
        buf.write("\2\u00e6\u00e7\7%\2\2\u00e7-\3\2\2\2\u00e8\u00ea\7\t\2")
        buf.write("\2\u00e9\u00eb\5\26\f\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7%\2\2\u00ed")
        buf.write("/\3\2\2\2\u00ee\u00ef\5\26\f\2\u00ef\u00f0\7%\2\2\u00f0")
        buf.write("\61\3\2\2\2\u00f1\u00f5\7#\2\2\u00f2\u00f4\5\6\4\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00fb\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f8\u00fa\5\"\22\2\u00f9\u00f8\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7")
        buf.write("$\2\2\u00ff\63\3\2\2\2\u0100\u0101\t\b\2\2\u0101\65\3")
        buf.write("\2\2\2\269?JQW_jqx\u0086\u009d\u009f\u00a6\u00b2\u00bb")
        buf.write("\u00c6\u00cf\u00ea\u00f5\u00fb")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'do'", "'while'", "'break'", 
                     "'continue'", "'return'", "'for'", "'float'", "'int'", 
                     "'void'", "'boolean'", "'string'", "'+'", "'*'", "'!'", 
                     "'||'", "'!='", "'<'", "'<='", "'='", "'-'", "'/'", 
                     "'%'", "'&&'", "'=='", "'>'", "'>='", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "DO", "WHILE", "BREAK", 
                      "CONTINUE", "RETURN", "FOR", "FLOATTYPE", "INTTYPE", 
                      "VOIDTYPE", "BOOLEANTYPE", "STRINGTYPE", "ADD", "MUL", 
                      "LOGNOT", "LOGOR", "NOTEQ", "LESS", "LEQ", "ASS", 
                      "SUB", "DIV", "MOD", "LOGAND", "EQ", "GREATER", "GEQ", 
                      "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", "COMMA", 
                      "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
                      "LC", "BC", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_varDecl = 2
    RULE_list_vars = 3
    RULE_var = 4
    RULE_funcDecl = 5
    RULE_funcType = 6
    RULE_array_pointer_type = 7
    RULE_list_param = 8
    RULE_paraDecl = 9
    RULE_express = 10
    RULE_operands = 11
    RULE_lit = 12
    RULE_arr_el = 13
    RULE_func_call = 14
    RULE_list_express = 15
    RULE_statements = 16
    RULE_if_s = 17
    RULE_dowhile_s = 18
    RULE_for_s = 19
    RULE_break_s = 20
    RULE_continue_s = 21
    RULE_return_s = 22
    RULE_express_s = 23
    RULE_block_s = 24
    RULE_primtype = 25

    ruleNames =  [ "program", "decl", "varDecl", "list_vars", "var", "funcDecl", 
                   "funcType", "array_pointer_type", "list_param", "paraDecl", 
                   "express", "operands", "lit", "arr_el", "func_call", 
                   "list_express", "statements", "if_s", "dowhile_s", "for_s", 
                   "break_s", "continue_s", "return_s", "express_s", "block_s", 
                   "primtype" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    DO=3
    WHILE=4
    BREAK=5
    CONTINUE=6
    RETURN=7
    FOR=8
    FLOATTYPE=9
    INTTYPE=10
    VOIDTYPE=11
    BOOLEANTYPE=12
    STRINGTYPE=13
    ADD=14
    MUL=15
    LOGNOT=16
    LOGOR=17
    NOTEQ=18
    LESS=19
    LEQ=20
    ASS=21
    SUB=22
    DIV=23
    MOD=24
    LOGAND=25
    EQ=26
    GREATER=27
    GEQ=28
    LS=29
    RS=30
    LB=31
    RB=32
    LP=33
    RP=34
    SEMI=35
    COMMA=36
    ID=37
    INTLIT=38
    FLOATLIT=39
    BOOLEANLIT=40
    STRINGLIT=41
    LC=42
    BC=43
    WS=44
    ERROR_CHAR=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.decl()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FLOATTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                    break

            self.state = 57
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MCParser.VarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MCParser.FuncDeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.funcDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def list_vars(self):
            return self.getTypedRuleContext(MCParser.List_varsContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.primtype()
            self.state = 64
            self.list_vars()
            self.state = 65
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_varsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_vars" ):
                listener.enterList_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_vars" ):
                listener.exitList_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_vars" ):
                return visitor.visitList_vars(self)
            else:
                return visitor.visitChildren(self)




    def list_vars(self):

        localctx = MCParser.List_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.var()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 68
                self.match(MCParser.COMMA)
                self.state = 69
                self.var()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MCParser.ID)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 76
                self.match(MCParser.LS)
                self.state = 77
                self.match(MCParser.INTLIT)
                self.state = 78
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcType(self):
            return self.getTypedRuleContext(MCParser.FuncTypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_s(self):
            return self.getTypedRuleContext(MCParser.Block_sContext,0)


        def list_param(self):
            return self.getTypedRuleContext(MCParser.List_paramContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.funcType()
            self.state = 82
            self.match(MCParser.ID)
            self.state = 83
            self.match(MCParser.LB)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FLOATTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 84
                self.list_param()


            self.state = 87
            self.match(MCParser.RB)
            self.state = 88
            self.block_s()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def array_pointer_type(self):
            return self.getTypedRuleContext(MCParser.Array_pointer_typeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncType" ):
                listener.enterFuncType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncType" ):
                listener.exitFuncType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncType" ):
                return visitor.visitFuncType(self)
            else:
                return visitor.visitChildren(self)




    def funcType(self):

        localctx = MCParser.FuncTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcType)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.array_pointer_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_array_pointer_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_pointer_type" ):
                listener.enterArray_pointer_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_pointer_type" ):
                listener.exitArray_pointer_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pointer_type" ):
                return visitor.visitArray_pointer_type(self)
            else:
                return visitor.visitChildren(self)




    def array_pointer_type(self):

        localctx = MCParser.Array_pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_pointer_type)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.primtype()
                self.state = 96
                self.match(MCParser.ID)
                self.state = 97
                self.match(MCParser.LS)
                self.state = 98
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.primtype()
                self.state = 101
                self.match(MCParser.LS)
                self.state = 102
                self.match(MCParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParaDeclContext)
            else:
                return self.getTypedRuleContext(MCParser.ParaDeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_param" ):
                listener.enterList_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_param" ):
                listener.exitList_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = MCParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.paraDecl()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 107
                self.match(MCParser.COMMA)
                self.state = 108
                self.paraDecl()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_paraDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParaDecl" ):
                listener.enterParaDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParaDecl" ):
                listener.exitParaDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaDecl" ):
                return visitor.visitParaDecl(self)
            else:
                return visitor.visitChildren(self)




    def paraDecl(self):

        localctx = MCParser.ParaDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paraDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.primtype()
            self.state = 115
            self.match(MCParser.ID)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 116
                self.match(MCParser.LS)
                self.state = 117
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressContext,i)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def LOGNOT(self):
            return self.getToken(MCParser.LOGNOT, 0)

        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def LEQ(self):
            return self.getToken(MCParser.LEQ, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def GEQ(self):
            return self.getToken(MCParser.GEQ, 0)

        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def LOGAND(self):
            return self.getToken(MCParser.LOGAND, 0)

        def LOGOR(self):
            return self.getToken(MCParser.LOGOR, 0)

        def ASS(self):
            return self.getToken(MCParser.ASS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpress" ):
                listener.enterExpress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpress" ):
                listener.exitExpress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress" ):
                return visitor.visitExpress(self)
            else:
                return visitor.visitChildren(self)



    def express(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.ExpressContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_express, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LB]:
                self.state = 121
                self.match(MCParser.LB)
                self.state = 122
                self.express(0)
                self.state = 123
                self.match(MCParser.RB)
                pass
            elif token in [MCParser.LS]:
                self.state = 125
                self.match(MCParser.LS)
                self.state = 126
                self.operands()
                self.state = 127
                self.match(MCParser.RS)
                pass
            elif token in [MCParser.LOGNOT, MCParser.SUB]:
                self.state = 129
                _la = self._input.LA(1)
                if not(_la==MCParser.LOGNOT or _la==MCParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self.express(9)
                pass
            elif token in [MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLEANLIT, MCParser.STRINGLIT]:
                self.state = 131
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 134
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 135
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self.express(9)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 137
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 138
                        _la = self._input.LA(1)
                        if not(_la==MCParser.ADD or _la==MCParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 139
                        self.express(8)
                        pass

                    elif la_ == 3:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 140
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 141
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.LEQ) | (1 << MCParser.GREATER) | (1 << MCParser.GEQ))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 142
                        self.express(7)
                        pass

                    elif la_ == 4:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 143
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 144
                        _la = self._input.LA(1)
                        if not(_la==MCParser.LOGNOT or _la==MCParser.EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 145
                        self.express(6)
                        pass

                    elif la_ == 5:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 146
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 147
                        self.match(MCParser.LOGAND)
                        self.state = 148
                        self.express(5)
                        pass

                    elif la_ == 6:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 149
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 150
                        self.match(MCParser.LOGOR)
                        self.state = 151
                        self.express(4)
                        pass

                    elif la_ == 7:
                        localctx = MCParser.ExpressContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_express)
                        self.state = 152
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 153
                        self.match(MCParser.ASS)
                        self.state = 154
                        self.express(2)
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(MCParser.LitContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def arr_el(self):
            return self.getTypedRuleContext(MCParser.Arr_elContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MCParser.Func_callContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperands" ):
                listener.enterOperands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperands" ):
                listener.exitOperands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operands)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(MCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.arr_el()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(MCParser.BOOLEANLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit" ):
                listener.enterLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit" ):
                listener.exitLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = MCParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arr_el

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr_el" ):
                listener.enterArr_el(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr_el" ):
                listener.exitArr_el(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_el" ):
                return visitor.visitArr_el(self)
            else:
                return visitor.visitChildren(self)




    def arr_el(self):

        localctx = MCParser.Arr_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arr_el)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MCParser.ID)
            self.state = 169
            self.match(MCParser.LS)
            self.state = 170
            self.match(MCParser.INTLIT)
            self.state = 171
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def list_express(self):
            return self.getTypedRuleContext(MCParser.List_expressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MCParser.ID)
            self.state = 174
            self.match(MCParser.LB)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LOGNOT) | (1 << MCParser.SUB) | (1 << MCParser.LS) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 175
                self.list_express()


            self.state = 178
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_express

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_express" ):
                listener.enterList_express(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_express" ):
                listener.exitList_express(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_express" ):
                return visitor.visitList_express(self)
            else:
                return visitor.visitChildren(self)




    def list_express(self):

        localctx = MCParser.List_expressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_express)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.express(0)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 181
                self.match(MCParser.COMMA)
                self.state = 182
                self.express(0)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_s(self):
            return self.getTypedRuleContext(MCParser.If_sContext,0)


        def dowhile_s(self):
            return self.getTypedRuleContext(MCParser.Dowhile_sContext,0)


        def for_s(self):
            return self.getTypedRuleContext(MCParser.For_sContext,0)


        def break_s(self):
            return self.getTypedRuleContext(MCParser.Break_sContext,0)


        def continue_s(self):
            return self.getTypedRuleContext(MCParser.Continue_sContext,0)


        def return_s(self):
            return self.getTypedRuleContext(MCParser.Return_sContext,0)


        def express_s(self):
            return self.getTypedRuleContext(MCParser.Express_sContext,0)


        def block_s(self):
            return self.getTypedRuleContext(MCParser.Block_sContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = MCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statements)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.if_s()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.dowhile_s()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.for_s()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.break_s()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.continue_s()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.return_s()
                pass
            elif token in [MCParser.LOGNOT, MCParser.SUB, MCParser.LS, MCParser.LB, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLEANLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 194
                self.express_s()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 195
                self.block_s()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementsContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_s" ):
                listener.enterIf_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_s" ):
                listener.exitIf_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_s" ):
                return visitor.visitIf_s(self)
            else:
                return visitor.visitChildren(self)




    def if_s(self):

        localctx = MCParser.If_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MCParser.IF)
            self.state = 199
            self.match(MCParser.LB)
            self.state = 200
            self.express(0)
            self.state = 201
            self.match(MCParser.RB)
            self.state = 202
            self.statements()
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 203
                self.match(MCParser.ELSE)
                self.state = 204
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def statements(self):
            return self.getTypedRuleContext(MCParser.StatementsContext,0)


        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_dowhile_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDowhile_s" ):
                listener.enterDowhile_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDowhile_s" ):
                listener.exitDowhile_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_s" ):
                return visitor.visitDowhile_s(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_s(self):

        localctx = MCParser.Dowhile_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dowhile_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MCParser.DO)
            self.state = 208
            self.statements()
            self.state = 209
            self.match(MCParser.WHILE)
            self.state = 210
            self.express(0)
            self.state = 211
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statements(self):
            return self.getTypedRuleContext(MCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_s" ):
                listener.enterFor_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_s" ):
                listener.exitFor_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_s" ):
                return visitor.visitFor_s(self)
            else:
                return visitor.visitChildren(self)




    def for_s(self):

        localctx = MCParser.For_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MCParser.FOR)
            self.state = 214
            self.match(MCParser.LB)
            self.state = 215
            self.express(0)
            self.state = 216
            self.match(MCParser.SEMI)
            self.state = 217
            self.express(0)
            self.state = 218
            self.match(MCParser.SEMI)
            self.state = 219
            self.express(0)
            self.state = 220
            self.match(MCParser.RB)
            self.state = 221
            self.statements()
            self.state = 222
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_s" ):
                listener.enterBreak_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_s" ):
                listener.exitBreak_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_s" ):
                return visitor.visitBreak_s(self)
            else:
                return visitor.visitChildren(self)




    def break_s(self):

        localctx = MCParser.Break_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MCParser.BREAK)
            self.state = 225
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_s" ):
                listener.enterContinue_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_s" ):
                listener.exitContinue_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_s" ):
                return visitor.visitContinue_s(self)
            else:
                return visitor.visitChildren(self)




    def continue_s(self):

        localctx = MCParser.Continue_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MCParser.CONTINUE)
            self.state = 228
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_s" ):
                listener.enterReturn_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_s" ):
                listener.exitReturn_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_s" ):
                return visitor.visitReturn_s(self)
            else:
                return visitor.visitChildren(self)




    def return_s(self):

        localctx = MCParser.Return_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MCParser.RETURN)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LOGNOT) | (1 << MCParser.SUB) | (1 << MCParser.LS) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 231
                self.express(0)


            self.state = 234
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpress_s" ):
                listener.enterExpress_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpress_s" ):
                listener.exitExpress_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress_s" ):
                return visitor.visitExpress_s(self)
            else:
                return visitor.visitChildren(self)




    def express_s(self):

        localctx = MCParser.Express_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_express_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.express(0)
            self.state = 237
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(MCParser.VarDeclContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_s" ):
                listener.enterBlock_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_s" ):
                listener.exitBlock_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_s" ):
                return visitor.visitBlock_s(self)
            else:
                return visitor.visitChildren(self)




    def block_s(self):

        localctx = MCParser.Block_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(MCParser.LP)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FLOATTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 240
                self.varDecl()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.LOGNOT) | (1 << MCParser.SUB) | (1 << MCParser.LS) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 246
                self.statements()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANTYPE(self):
            return self.getToken(MCParser.BOOLEANTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimtype" ):
                listener.enterPrimtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimtype" ):
                listener.exitPrimtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimtype" ):
                return visitor.visitPrimtype(self)
            else:
                return visitor.visitChildren(self)




    def primtype(self):

        localctx = MCParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FLOATTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.express_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def express_sempred(self, localctx:ExpressContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




