# ast_nodes.py

class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def to_python(self):
        return '\n'.join(statement.to_python() for statement in self.statements)

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
        operators = {
            '+': '+',
            '-': '-',
            '*': '*',
            '/': '/',
            '<': '<',
            '<=': '<=',
            '>': '>',
            '>=': '>=',
            '=': '==',
            '<>': '!='
        }
        op = operators.get(self.operator, self.operator)
        return f"({self.left.to_python()} {op} {self.right.to_python()})"

class UnaryExpression(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def to_python(self):
        return f"{self.operator}{self.operand.to_python()}"

class LogicalExpression(BinaryExpression):
    # Inherits from BinaryExpression, override as needed
    pass

class PowerExpression(BinaryExpression):
    def to_python(self):
        return f"pow({self.left.to_python()}, {self.right.to_python()})"

class FunctionCall(Expression):
    def __init__(self, function_name, argument=None):
        # Sanitize the function name to create a valid Python function name
        self.function_name = function_name.replace('.', '_')
        self.argument = argument

    def to_python(self):
        # Dynamically construct the function call
        arg_str = self.argument.to_python() if self.argument else ''
        return f"{self.function_name}({arg_str})"


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def to_python(self):
        return self.name

class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def to_python(self):
        if isinstance(self.value, str):
            return repr(self.value)  # Use repr to ensure proper string quoting in Python
        else:
            return str(self.value)

class ConditionalStatement(Statement):
    def __init__(self, condition, true_branch):
        self.condition = condition
        self.true_branch = true_branch

    def to_python(self):
        return f"if {self.condition.to_python()}:\n    {self.true_branch.to_python()}"
