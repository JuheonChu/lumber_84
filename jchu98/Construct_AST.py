from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# Open and read from the file 'bas.bas'
with open('TEST.BAS', 'r') as file:
    input_stream = InputStream(file.read())

# Lexer separates the characters into tokens according to the grammar we defined.
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Parser builds the Abstract Syntax Tree
parser = ExprParser(token_stream)

tree = parser.program()  # Use the starting rule (assuming it's 'program')

print(tree.toStringTree(recog=parser))

