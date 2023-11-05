grammar Expr;

// Parser Rules
program : (statement | labelStatement)* ;


statement : assignment
          | conditionalStatement
          | functionCall
          | commentStatement
          | statementSequence // Multiple statements on one line
          ;

statementSequence: statement ('.' statement)+

labelStatement : label ':' statement ; // Handling labels for statements

assignment : variable '=' expression ;
conditionalStatement : 'IF' expression relationalOperator expression 'THEN' statement ;

functionCall : 'CALL' functionReference;

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

functionReference : ID '(' expression ')'   // # FuncCallExpr
                  | arrayReference          // # ArrayRefExpr
		  | ID			    // # VarRef 
                  ;

arrayReference : ID '(' expression (',' expression)* ')' ; // Multi-dimensional arrays

expressionList : expression (',' expression)* ;variable : ID ( '%' | '$' )? ;

constant : STRING_LITERAL | NUMBER | REAL_NUMBER ;

commentStatement : 'REM' ~[\r\n]* ; // To capture comments, ignoring newlines

label : ID ; // Label definitions

variable : ID ( '.' ID )? ('$')? ;
constant : STRING | NUMBER ;

commentStatement : 'REM' ~[\r\n]* ; // To capture comments, ignoring newlines

label : ID ; // Label definitions

// Lexer Rules
ID : [a-zA-Z] [a-zA-Z0-9]* ;

// Adjusted rules to account for string identifiers and case-insensitivity
STRING_LITERAL : '"' ( ~["\r\n] | '""' )* '"' ;

NUMBER : '-'? [0-9]+ ;
REAL_NUMBER : NUMBER ('.' [0-9]+)? (E [+-]? [0-9]+)? ;

// Whitespace and comments
WS : [ \t\r\n]+ -> skip ;

// To handle CBASIC's case insensitivity, you would need to either
// handle it in the parser or use a case-insensitive mode in your lexer.

// For simplicity here, this grammar assumes all input is uppercase.
// Otherwise, use a tool or option to convert lowercase letters to uppercase
// before lexing or add lexer rules to match both cases.

arithmeticOperators : '+' | '-' | '*' | '/' ;
relationalOperator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;
logicalOperator : 'AND' | 'OR' | 'NOT' ;

LINE_CONTINUATION : '\\' -> skip ; // For line continuation characte

// To handle CBASIC's case insensitivity, you would need to either
// handle it in the parser or use a case-insensitive mode in your lexer.

// For simplicity here, this grammar assumes all input is uppercase.
// Otherwise, use a tool or option to convert lowercase letters to uppercase
// before lexing or add lexer rules to match both cases.

arithmeticOperators : '+' | '-' | '*' | '/' ;
relationalOperator : '<' | '<=' | '>' | '>=' | '==' | '!=' ;
logicalOperator : 'AND' | 'OR' | 'NOT' ;

LINE_CONTINUATION : '\\' -> skip ; // For line continuation character
