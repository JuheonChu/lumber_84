# Construct_AST.py

from antlr4 import *
from visitor.ExprLexer import ExprLexer
from visitor.ExprParser import ExprParser
from CBASICVisitor import CBASICVisitor
from ast_nodes import *

# Main script to run the conversion

def ast_to_python(tree):
    visitor = CBASICVisitor()
    return visitor.visit(tree).to_python()

# Read the input file and create a lexer and parser
with open('TEST.BAS', 'r') as file:
    input_stream = InputStream(file.read())

lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

# Get the parse tree
tree = parser.program()

# Generate Python code from the AST
python_code = ast_to_python(tree)
print(python_code)

