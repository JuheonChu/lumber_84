from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def parse(tokens):
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(Node(None))
        elif token == ')':
            child = stack.pop()
            if stack:
                stack[-1].children.append(child)
            else:
                return child
        else:
            stack[-1].children.append(Node(token))
    return stack[0]

def tokenize(input_string):
    return input_string.replace('(', ' ( ').replace(')', ' ) ').split()

def traverse(node, line=1):
    output = []
    output.append((node.value, line))
    for child in node.children:
        line += 1
        child_output, line = traverse(child, line)
        output.extend(child_output)
    return output, line



# Open and read from the file 'bas.bas'
with open('TEST.BAS', 'r') as file:
    input_stream = InputStream(file.read())

# Lexer separates the characters into tokens according to the grammar we defined.
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
# Parser builds the Abstract Syntax Tree
parser = ExprParser(token_stream)

tree = parser.program()  # Use the starting rule (assuming it's 'program')


# Construct the tokenized Abstract Syntax Tree 
tokenized_string = tree.toStringTree(recog=parser) 

tokens = tokenize(tokenized_string)
ast = parse(tokens)
output, _ = traverse(ast)


for node, line in output[1:]:  # skip the root
    print(f"{node},{line}")



