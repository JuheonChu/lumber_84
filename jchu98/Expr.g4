grammar Expr;

// Parser Rules
program : (statement | labelStatement)* ;

statement
   : assignment
   | conditionalStatement
   | functionCall
   | commentStatement
   | statementSequence // Multiple statements on one line
   ;

statementSequence: statement ('.' statement)+ ;

labelStatement : label ':' statement ; // Handling labels for statements

assignment : variable '=' expression ;

conditionalStatement : 'IF' expression 'THEN' statement ;

functionCall : 'CALL' functionReference;

expression
   : expression '^' expression            # PowerExpr
   | expression '*' expression            # MulExpr
   | expression '/' expression            # DivExpr
   | expression '+' expression            # AddExpr
   | expression '-' expression            # SubExpr
   | expression relationalOperator expression # RelExpr
   | expression logicalOperator expression    # LogicExpr
   | expression '&' expression                # ConcatExpr
   | '-' expression                           # UnaryMinusExpr
   | '(' expression ')'                       # ParensExpr
   | functionReference                        # FuncRefExpr
   | variable                                 # VarExpr
   | constant                                 # ConstExpr
   ;

functionReference
   : ID '(' expressionList? ')' // Function calls and array references
   | ID                        // Variable reference
   ;

arrayReference : ID '(' expressionList ')' ; // Multi-dimensional arrays

expressionList : expression (',' expression)* ;

variable : ID ( '%' | '$' )? ;

constant
   : HEX_LITERAL // Hexadecimal numbers
   | BIN_LITERAL // Binary numbers
   | STRING_LITERAL
   | NUMBER
   | REAL_NUMBER
   ;

commentStatement : 'REM' ~[\r\n]* ; // To capture comments, ignoring newlines

label : ID ; // Label definitions

// Lexer Rules
HEX_LITERAL : '0' ('x' | 'X') [0-9a-fA-F]+ ;
BIN_LITERAL : '0' ('b' | 'B') [01]+ ;

STRING_LITERAL : '"' (~["\r\n])* '"';
NUMBER : [0-9]+ ;
REAL_NUMBER : [0-9]+ '.' [0-9]* | '.' [0-9]+ ;

relationalOperator
   : '<'
   | '<='
   | '>'
   | '>='
   | '=='
   | '!='
   ;

logicalOperator
   : 'AND'
   | 'OR'
   | 'NOT'
   | 'XOR'
   ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;

ASSIGN : '=' ;
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
POWER : '^' ;
AND_OP : '&&' ;
OR_OP : '||' ;
NOT_OP : '!' ;
XOR_OP : '^^' ;

LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACK : '[' ;
RBRACK : ']' ;

SEMI : ';' ;
COLON : ':' ;
COMMA : ',' ;
DOT : '.' ;
AMPERSAND : '&' ;

WS : [ \t\r\n]+ -> skip ; // Skip whitespace

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

