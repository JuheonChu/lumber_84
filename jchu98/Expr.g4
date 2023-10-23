grammar Expr;

// Parser Rules
program : (statement)* ;

statement : assignment | conditionalStatement | functionCall ;

assignment : variable '=' expression ;
conditionalStatement : 'IF' expression relationalOperator expression 'THEN' functionCall ;
functionCall : 'CALL' ID ;

expression
   : '-' expression                                #UnaryMinusExpr
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

operator : arithmeticOperators 
         | relationalOperator 
         | logicalOperator ;

arithmeticOperators : '^' | '*' | '/' | '+' | '-' ;
relationalOperator : '<' | '<=' | '>' | '>=' | '=' | '<>' ;
logicalOperator : 'NOT' | 'AND' | 'OR' | 'XOR' ;

// Lexer Rules
ID : [a-zA-Z_][a-zA-Z0-9_]* ; 
STRING : '"' ( ~["\r\n] )* '"' ; 
NUMBER : [0-9]+ ('.' [0-9]+)? ; 
WS : [ \t\r\n]+ -> skip ; 

