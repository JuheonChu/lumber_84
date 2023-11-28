# CBASICVisitor.py

from visitor.ExprVisitor import ExprVisitor
from visitor.ExprParser import ExprParser
from ast_nodes import *

class CBASICVisitor(ExprVisitor):

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        statements = [self.visit(child) for child in ctx.getChildren() if isinstance(child, ExprParser.StatementContext)]
        return Program(statements)

    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        variable = self.visit(ctx.variable())
        expression = self.visit(ctx.expression())
        return Assignment(variable, expression)

    def visitVariable(self, ctx:ExprParser.VariableContext):
        # Handle potential ID.ID structure if necessary
        variable_name = ctx.ID(0).getText()
        if ctx.ID(1):
            variable_name += '.' + ctx.ID(1).getText()
        return Variable(variable_name)

    def visitConstant(self, ctx:ExprParser.ConstantContext):
        value = ctx.getText()
        # Handle string and number values differently
        if value.startswith('"'):
            value = value.strip('"')  # Remove quotes around strings
        elif '.' in value:
            value = float(value)  # Convert to float if it contains a dot
        else:
            value = int(value)  # Convert to int otherwise
        return Constant(value)

    def visitConditionalStatement(self, ctx:ExprParser.ConditionalStatementContext):
        condition = self.visit(ctx.expression(0))
        true_branch = self.visit(ctx.functionCall())
        return ConditionalStatement(condition, true_branch)

    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        function_name = ctx.ID().getText()
        # Assuming function calls only occur with a single ID and no arguments
        return FunctionCall(function_name)

    def visitUnaryMinusExpr(self, ctx:ExprParser.UnaryMinusExprContext):
        expression = self.visit(ctx.expression())
        return UnaryExpression('-', expression)

    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visit(ctx.expression())

    def visitFuncRefExpr(self, ctx):
        # Directly access the children of the context
        children = [child for child in ctx.getChildren()]

        function_name = children[0].getText()  # The first child should be the ID token

        # Check if the function call has arguments (i.e., if there are more than one child, it should have parentheses and an expression)
        if len(children) > 1:
            # Assuming the third child is the expression inside the parentheses
            argument = self.visit(children[2])  
            return FunctionCall(function_name, argument)
        else:
            # Function reference without arguments
            return Variable(function_name)  # or FunctionCall(function_name, None) depending on your language specificationn
    

    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        return self.visit(ctx.variable())

    def visitArithExpr(self, ctx:ExprParser.ArithExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.arithmeticOperators().getText()
        return BinaryExpression(left, op, right)

    def visitRelExpr(self, ctx:ExprParser.RelExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.relationalOperator().getText()
        return BinaryExpression(left, op, right)

    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.logicalOperator().getText()
        return LogicalExpression(left, op, right)  # Assuming you have a LogicalExpression class

    def visitVisitPowerExpr(self, ctx:ExprParser.VisitPowerExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return PowerExpression(left, right)  # Assuming you have a PowerExpression class


# You need to create classes for UnaryExpression, LogicalExpression, and PowerExpression 

