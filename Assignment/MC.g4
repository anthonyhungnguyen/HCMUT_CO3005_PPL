grammar MC;

// Nguyen Phuc Hung
// 1752259

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}


// Parser

program  : decl+ EOF;
decl : varDecl|funcDecl;
// var Declaration
varDecl : PRIMTYPE list_vars SEMI;
list_vars: var (COMMA var)*;
var: ID (LS INTLIT RS)?;

// Function Declaration
funcDecl : funcType ID LB list_param? RB block_s; 
funcType : PRIMTYPE | VOIDTYPE | array_pointer_type | array_type;
array_type : PRIMTYPE ID LS INTLIT RS;
array_pointer_type : PRIMTYPE ID LS RS | PRIMTYPE LS RS; 
list_param: paraDecl (COMMA paraDecl)*;
paraDecl : PRIMTYPE ID (LS RS)?;

// Expression
express: LP express RP
        | LS operands RS
        | <assoc = right> (SUB|LOGNOT) express
        | express (DIV|MUL|MOD) express
        | express (ADD|SUB) express
        | express (LESS|LEQ|GREATER|GEQ) express
        | express (EQ|LOGNOT) express
        | express LOGAND express
        | express LOGOR express
        | <assoc = right>express ASS express
        | operands;

operands: lit|ID|arr_el|func_call;
lit: INTLIT|FLOATLIT|STRINGLIT|BOOLEANLIT;
arr_el: ID LS INTLIT RS;
func_call: ID LB list_express? RB;
list_express: express (COMMA express)*;
statements: if_s|dowhile_s|for_s|break_s|continue_s|return_s|express_s|block_s;
if_s: IF LB express RB statements (ELSE statements)?;
dowhile_s: DO statements WHILE express SEMI;
for_s: FOR LB express SEMI express SEMI express RB statements SEMI;
break_s: BREAK SEMI;
continue_s: CONTINUE SEMI;
return_s: RETURN express? SEMI;
express_s: express SEMI;
block_s: LP varDecl* statements* RP;
// builtInFunc: 'put' (Put LB express RB) | 'get' (Get LB RB) SEMI;



// Lexer

// KW

PRIMTYPE: BOOLEAN|INT|FLOAT|STRING;
VOIDTYPE: VOID;
IF: 'if';
ELSE: 'else';
DO: 'do';
WHILE: 'while';
BOOLEAN: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
FOR: 'for';
// Put: Int|Float|String|Boolean;
// Get: 'Int'|'Float'|'String'|'Boolean';

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
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';' ;
COMMA: ',';

// Token

ID: [_a-zA-Z][_a-zA-Z0-9]* ;

INTLIT: DIGIT+;

FLOATLIT: DIGIT+[.]?DIGIT*EX|DIGIT*[.]DIGIT+EX;

BOOLEANLIT: TRUE|FALSE;

STRINGLIT:  DOUBLEQUOTES STR_CHAR* DOUBLEQUOTES;

// Fragments

fragment DIGIT: [0-9];
fragment EX: ([eE][-]?[0-9]+)?;
fragment FLOAT: 'float';
fragment INT: 'int';
fragment VOID: 'void' ; 
fragment TRUE: 'true';
fragment FALSE: 'false';
fragment STRING: 'string';
fragment DOUBLEQUOTES: '"';
fragment ESCAPE_SEQ: '\\'[btnfr"\\];
fragment ESCAPE_ILLEGAL: '\\' ~[btnfr"\\] | ~'\\';
fragment STR_CHAR: ~[\b\f\r\n\t"\\] | ESCAPE_SEQ;
// fragment Int: 'Int'|'IntLn';
// fragment Float: 'Float'|'FloatLn';
// fragment String: 'String'|'StringLn';
// fragment Boolean: 'Bool'|'BoolLn';

// Comment

LC : '//' ~[\r\n]* -> skip;
BC : '/*' .* '*/' -> skip ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .
            {raise ErrorToken(self.text)}
            ;
UNCLOSE_STRING: DOUBLEQUOTES (ESCAPE_SEQ|~[\r\n"\\])* {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: DOUBLEQUOTES (STR_CHAR|ESCAPE_ILLEGAL)* DOUBLEQUOTES {raise IllegalEscape(self.text)};






