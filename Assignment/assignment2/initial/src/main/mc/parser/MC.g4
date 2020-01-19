// 1752259
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

// Parser

program: decl+ EOF;
decl: varDecl | funcDecl;
// var Declaration
varDecl: primtype list_vars SEMI;
list_vars: var (COMMA var)*;
var: ID (LS INTLIT RS)?;

// Function Declaration
funcDecl: funcType ID LB list_param? RB block_s;
funcType: primtype | VOIDTYPE | array_pointer_type;
array_pointer_type: primtype LS RS;
list_param: paraDecl (COMMA paraDecl)*;
paraDecl: primtype ID (LS RS)?;

express: express_ass ASS express | express_ass; // right
express_ass: express_ass LOGOR express_or | express_or; // left
express_or: express_or LOGAND express_and | express_and; // left
express_and:
	express_not_or_equal (EQ | NOTEQ) express_not_or_equal
	| express_not_or_equal;
express_not_or_equal:
	express_compare (LESS | LEQ | GREATER | GEQ) express_compare
	| express_compare;
express_compare:
	express_compare (ADD | SUB) express_add_sub
	| express_add_sub; // left
express_add_sub:
	express_add_sub (DIV | MUL | MOD) express_div_mul_mod
	| express_div_mul_mod; // left
express_div_mul_mod:
	(SUB | LOGNOT) express_div_mul_mod
	| express_sub_not; // right
express_sub_not:
	express_paren LS express RS
	| ID LS express RS
	| express_paren;
express_paren: operands | LB express RB;
// a[1][2]
operands: lit | ID | func_call;
lit: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT;
func_call: ID LB list_express? RB;
list_express: express (COMMA express)*;
statements:
	if_s
	| dowhile_s SEMI
	| for_s
	| break_s SEMI
	| continue_s SEMI
	| return_s SEMI
	| express_s SEMI
	| block_s;
if_s: IF LB express RB statements (ELSE statements)?;
dowhile_s: DO statements+ WHILE express;
for_s: FOR LB express SEMI express SEMI express RB statements;
break_s: BREAK;
continue_s: CONTINUE;
return_s: RETURN express?;
express_s: express;
block_s: LP blockmember* RP;
blockmember: varDecl | statements;
primtype: BOOLEANTYPE | INTTYPE | STRINGTYPE | FLOATTYPE;

// Lexer

// KW

IF: 'if';
ELSE: 'else';
DO: 'do';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
FOR: 'for';
FLOATTYPE: 'float';
INTTYPE: 'int';
VOIDTYPE: 'void';
BOOLEANTYPE: 'boolean';
STRINGTYPE: 'string';

// Operators

ADD: '+';
MUL: '*';
LOGNOT: '!';
LOGOR: '||';
NOTEQ: '!=';
LESS: '<';
LEQ: '<=';
ASS: '=';
SUB: '-';
DIV: '/';
MOD: '%';
LOGAND: '&&';
EQ: '==';
GREATER: '>';
GEQ: '>=';

// Seperators

LS: '[';
RS: ']';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';

// Token
BOOLEANLIT: TRUE | FALSE;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

INTLIT: DIGIT+;

FLOATLIT: (DIGIT+ [.]? DIGIT* | DIGIT* [.]DIGIT+) EX?;

STRINGLIT:
	DOUBLEQUOTES STR_CHAR* DOUBLEQUOTES {
    self.text = self.text[1:-1]
};

// Fragments

fragment DIGIT: [0-9];
fragment EX: ([eE][-+]? [0-9]+);
fragment TRUE: 'true';
fragment FALSE: 'false';
fragment DOUBLEQUOTES: '"';
fragment ESCAPE_SEQ: '\\' [btnfr"\\];
fragment ESCAPE_ILLEGAL: '\\' ~[btnfr"\\];
fragment STR_CHAR: ~[\r\n"\\] | ESCAPE_SEQ;

// Comment

LC: '//' ~[\r\n]* -> skip;
BC: '/*' .*? '*/' -> skip;
WS: [ \t\r\n\f]+ -> skip;
// skip spaces, tabs, newlines

UNCLOSE_STRING: DOUBLEQUOTES STR_CHAR*;
ILLEGAL_ESCAPE: DOUBLEQUOTES (STR_CHAR)* ESCAPE_ILLEGAL;
ERROR_CHAR: .;