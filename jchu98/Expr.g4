grammar Expr;

// Parser Rules
program : (statement | labelStatement)* EOF ;

statement
   : assignment
   | conditionalStatement
   | functionCall
   | commentStatement
   | statementSequence // Multiple statements on one line
   ;

statementSequence: statement ('.' statement)+ ;

labelStatement : label ':' statement ; // Handling labels for statements

assignment : variable ASSIGN expression ;

conditionalStatement : 'IF' expression 'THEN' statement ( 'ELSE' statement )? ;

functionCall : 'CALL' functionReference ( LPAREN expressionList? RPAREN )? 


expression
   : expression POWER expression            # PowerExpr
   | expression MULT expression             # MulExpr
   | expression DIV expression              # DivExpr
   | expression PLUS expression             # AddExpr
   | expression MINUS expression            # SubExpr
   | expression relationalOperator expression # RelExpr
   | expression logicalOperator expression    # LogicExpr
   | expression AMPERSAND expression          # ConcatExpr
   | MINUS expression                         # UnaryMinusExpr
   | LPAREN expression RPAREN                 # ParensExpr
   | functionReference                        # FuncRefExpr
   | variable                                 # VarExpr
   | constant                                 # ConstExpr
   ;



relationalOperator
   : LT | LTEQ | GT | GTEQ | EQ | NOTEQ
   ;

logicalOperator
   : AND | OR | NOT | XOR
   ;


functionReference
   : ID LPAREN expressionList? RPAREN // Function calls with parameters
   | ID                              // Function calls without parameters
   ;

arrayReference : ID LPAREN expressionList RPAREN ; // Multi-dimensional arrays

expressionList : expression (COMMA expression)* ;

variable : ID ( PERCENT | DOLLAR )? 


constant
   : HEX_LITERAL // Hexadecimal numbers
   | BIN_LITERAL // Binary numbers
   | STRING_LITERAL
   | NUMBER
   | REAL_NUMBER
   ;

commentStatement : REM ;

label : ID ; // Label definitions

// Lexer rules (Tokens)
LT          : '<' ;
LTEQ        : '<=' ;
GT          : '>' ;
GTEQ        : '>=' ;
EQ          : '==' ;
NOTEQ       : '<>' ;

AND         : 'AND' ;
OR          : 'OR' ;
NOT         : 'NOT' ;
XOR         : 'XOR' ;

POWER       : '^' ;
MULT        : '*' ;
DIV         : '/' ;
PLUS        : '+' ;
MINUS       : '-' ;
AMPERSAND   : '&' ;

ASSIGN      : '=' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
LBRACK      : '[' ;
RBRACK      : ']' ;

SEMI        : ';' ;
COLON       : ':' ;
COMMA       : ',' ;
DOT         : '.' ;
PERCENT     : '%' ;
DOLLAR      : '$' ;

ESCAPE_SEQUENCE : '\\' .; // Defines an escape sequence

ID          : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT         : [0-9]+ ;
FLOAT       : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;
STRING_LITERAL : '"' ( ~["\\] | '\\' . )* '"' ;
HEX_LITERAL : '0x' [0-9A-Fa-f]+ ;
BIN_LITERAL : '0b' ('0' | '1')+ ;
NUMBER      : [0-9]+ ;
REAL_NUMBER : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;

WS          : [ \t\r\n]+ -> skip ;
// Comments
REM             : 'REM' ~[\r\n]* -> skip ;
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;
