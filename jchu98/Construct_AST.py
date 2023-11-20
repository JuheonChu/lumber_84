from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.tree.Trees import Trees
import re

class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def to_python(self):
        return '\n'.join(s.to_python() for s in self.statements)

class Statement(Node):
    pass

class Assignment(Statement):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def to_python(self):
        return f"{self.variable.to_python()} = {self.expression.to_python()}"

class Expression(Node):
    pass

class BinaryExpression(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def to_python(self):
        op = {'+': '+', '-': '-', '*': '*', '/': '/'}.get(self.operator, self.operator)
        return f"({self.left.to_python()} {op} {self.right.to_python()})"

class FunctionCall(Expression):
    def __init__(self, function_name, argument=None):
        self.function_name = function_name
        self.argument = argument

    def to_python(self):
        if self.function_name == 'ABS':
            return f"abs({self.argument.to_python()})"
        elif self.function_name == 'CALL':
            return f"{self.argument.to_python()}()"
        # Add more function mappings as necessary

class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def to_python(self):
        return self.name

class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def to_python(self):
        return self.value

class ConditionalStatement(Statement):
    def __init__(self, condition, true_branch):
        self.condition = condition
        self.true_branch = true_branch

    def to_python(self):
        return f"if {self.condition.to_python()}:\n    {self.true_branch.to_python()}"

# A mock function to 'parse' the AST string - you will need to implement real parsing logic based on your AST format
def parse_ast(ast_string):
    # This should be replaced with a real parser
    # For now, we'll just return a hardcoded structure
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')
    expr1 = FunctionCall('ABS', BinaryExpression(Constant(-150), '+', Constant(0)))
    expr2 = BinaryExpression(Constant(100), '+', Constant(250))
    expr3 = BinaryExpression(BinaryExpression(x, '*', y), '/', Constant(3.5))
    assignment1 = Assignment(x, expr1)
    assignment2 = Assignment(y, expr2)
    assignment3 = Assignment(z, expr3)
    condition1 = ConditionalStatement(BinaryExpression(x, '<', y), FunctionCall('CALL', Variable('DISPLAY')))
    condition2 = ConditionalStatement(BinaryExpression((FunctionCall('ABS', BinaryExpression(x, '-', y))), '==', Constant(0)), FunctionCall('CALL', Variable('WARN')))
    tempA = Variable('tempA')
    tempB = Variable('tempB')
    expr4 = Constant(20.5)
    expr5 = BinaryExpression(tempA, '+', Constant(15.3))
    assignment4 = Assignment(tempA, expr4)
    assignment5 = Assignment(tempB, expr5)
    condition3 = ConditionalStatement(BinaryExpression(tempB, '>', Constant(35)), FunctionCall('CALL', Variable('COOLING')))
    val = Variable('val')
    expr6 = FunctionCall('ABS', BinaryExpression(tempA, '-', tempB))
    assignment6 = Assignment(val, expr6)
    name = Variable('name')
    expr7 = Constant('John')
    assignment7 = Assignment(name, expr7)
    return Program([assignment1, assignment2, assignment3, condition1, condition2, assignment4, assignment5, condition3, assignment6, assignment7])

# The function to convert the AST to Python code
def ast_to_python(ast_string):
    ast = parse_ast(ast_string)
    return ast.to_python()




# Read the input file and create a lexer and parser
with open('TEST.BAS', 'r') as file:
    input_stream = InputStream(file.read())

lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

# Get the parse tree
tree = parser.program()

# Example usage
ast_string = tree.toStringTree(recog=parser)

print(ast_string)
# Generate Python code from the AST string
python_code = ast_to_python(ast_string)
print(python_code)
