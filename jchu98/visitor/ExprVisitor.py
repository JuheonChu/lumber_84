# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:ExprParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionCall.
    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ArithExpr.
    def visitArithExpr(self, ctx:ExprParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ConstExpr.
    def visitConstExpr(self, ctx:ExprParser.ConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#VisitPowerExpr.
    def visitVisitPowerExpr(self, ctx:ExprParser.VisitPowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#RelExpr.
    def visitRelExpr(self, ctx:ExprParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LogicExpr.
    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FuncRefExpr.
    def visitFuncRefExpr(self, ctx:ExprParser.FuncRefExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ParensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#VarExpr.
    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:ExprParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#functionReference.
    def visitFunctionReference(self, ctx:ExprParser.FunctionReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#constant.
    def visitConstant(self, ctx:ExprParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operator.
    def visitOperator(self, ctx:ExprParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithmeticOperators.
    def visitArithmeticOperators(self, ctx:ExprParser.ArithmeticOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalOperator.
    def visitRelationalOperator(self, ctx:ExprParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalOperator.
    def visitLogicalOperator(self, ctx:ExprParser.LogicalOperatorContext):
        return self.visitChildren(ctx)



del ExprParser