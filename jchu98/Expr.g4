grammar Expr;

// Parser Rules
program : (statement | labelStatement)* ;

statement : assignment
          | conditionalStatement
          | functionCall
          | commentStatement
          | (statement (';' statement)+) // Multiple statements on one line
          ;

labelStatement : label ':' statement ; // Handling labels for statements

assignment : variable '=' expression ;
conditionalStatement : 'IF' expression relationalOperator expression 'THEN' functionCall ;
functionCall : 'CALL' ID '(' (expression (',' expression)*)? ')' ;

expression
   : '-' expression                                 #UnaryMinusExpr
   | '(' expression ')'                            #ParensExpr
   | functionReference                             #FuncRefExpr
   | variable                                      #VarExpr
   | constant                                      #ConstExpr
   | expression arithmeticOperators expression     #ArithExpr
   | expression relationalOperator expression      #RelExpr
   | expression logicalOperator expression         #LogicExpr
   ;

functionReference : ID '(' expression ')'   // E.g.: ABS(150)
                  | ID                      // E.g.: TEMP.A
                  ;

variable : ID ( '.' ID )? ('$')? ;
constant : STRING | NUMBER ;

commentStatement : 'REM' ~[\r\n]* ; // To capture comments, ignoring newlines

label : NUMBER | ID ; // Label definitions, allowing for numbers and identifiers

// Lexer Rules should include the backslash for line continuation
LINE_CONTINUATION : '\\' -> skip; // Skip the continuation character for now

// Adjust existing lexer rules accordingly
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' ( ~["\r\n] )* '"' ;
NUMBER : [0-9]+ ('.' [0-9]+)? ('E' [+-]? [0-9]+)? ; // Support for exponential notation
WS : [ \t\r\n]+ -> skip ;

COLON : ':' ; // Colon for multiple statements on one line

arithmeticOperators : '^' | '*' | '/' | '+' | '-' ;
relationalOperator : '<' | '<=' | '>' | '>=' | '=' | '<>' ;
logicalOperator : 'NOT' | 'AND' | 'OR' | 'XOR' ;

// Lexer Rules
ID : [a-zA-Z_][a-zA-Z0-9_]* ; 
STRING : '"' ( ~["\r\n] )* '"' ; 
NUMBER : [0-9]+ ('.' [0-9]+)? ; 
WS : [ \t\r\n]+ -> skip ; 

