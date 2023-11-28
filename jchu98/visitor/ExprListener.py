# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:ExprParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:ExprParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#functionCall.
    def enterFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ExprParser#functionCall.
    def exitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ExprParser#ArithExpr.
    def enterArithExpr(self, ctx:ExprParser.ArithExprContext):
        pass

    # Exit a parse tree produced by ExprParser#ArithExpr.
    def exitArithExpr(self, ctx:ExprParser.ArithExprContext):
        pass


    # Enter a parse tree produced by ExprParser#ConstExpr.
    def enterConstExpr(self, ctx:ExprParser.ConstExprContext):
        pass

    # Exit a parse tree produced by ExprParser#ConstExpr.
    def exitConstExpr(self, ctx:ExprParser.ConstExprContext):
        pass


    # Enter a parse tree produced by ExprParser#VisitPowerExpr.
    def enterVisitPowerExpr(self, ctx:ExprParser.VisitPowerExprContext):
        pass

    # Exit a parse tree produced by ExprParser#VisitPowerExpr.
    def exitVisitPowerExpr(self, ctx:ExprParser.VisitPowerExprContext):
        pass


    # Enter a parse tree produced by ExprParser#RelExpr.
    def enterRelExpr(self, ctx:ExprParser.RelExprContext):
        pass

    # Exit a parse tree produced by ExprParser#RelExpr.
    def exitRelExpr(self, ctx:ExprParser.RelExprContext):
        pass


    # Enter a parse tree produced by ExprParser#LogicExpr.
    def enterLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicExpr.
    def exitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass


    # Enter a parse tree produced by ExprParser#FuncRefExpr.
    def enterFuncRefExpr(self, ctx:ExprParser.FuncRefExprContext):
        pass

    # Exit a parse tree produced by ExprParser#FuncRefExpr.
    def exitFuncRefExpr(self, ctx:ExprParser.FuncRefExprContext):
        pass


    # Enter a parse tree produced by ExprParser#ParensExpr.
    def enterParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#ParensExpr.
    def exitParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ExprParser#VarExpr.
    def enterVarExpr(self, ctx:ExprParser.VarExprContext):
        pass

    # Exit a parse tree produced by ExprParser#VarExpr.
    def exitVarExpr(self, ctx:ExprParser.VarExprContext):
        pass


    # Enter a parse tree produced by ExprParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:ExprParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by ExprParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:ExprParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by ExprParser#functionReference.
    def enterFunctionReference(self, ctx:ExprParser.FunctionReferenceContext):
        pass

    # Exit a parse tree produced by ExprParser#functionReference.
    def exitFunctionReference(self, ctx:ExprParser.FunctionReferenceContext):
        pass


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#constant.
    def enterConstant(self, ctx:ExprParser.ConstantContext):
        pass

    # Exit a parse tree produced by ExprParser#constant.
    def exitConstant(self, ctx:ExprParser.ConstantContext):
        pass


    # Enter a parse tree produced by ExprParser#operator.
    def enterOperator(self, ctx:ExprParser.OperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#operator.
    def exitOperator(self, ctx:ExprParser.OperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#arithmeticOperators.
    def enterArithmeticOperators(self, ctx:ExprParser.ArithmeticOperatorsContext):
        pass

    # Exit a parse tree produced by ExprParser#arithmeticOperators.
    def exitArithmeticOperators(self, ctx:ExprParser.ArithmeticOperatorsContext):
        pass


    # Enter a parse tree produced by ExprParser#relationalOperator.
    def enterRelationalOperator(self, ctx:ExprParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#relationalOperator.
    def exitRelationalOperator(self, ctx:ExprParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalOperator.
    def enterLogicalOperator(self, ctx:ExprParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalOperator.
    def exitLogicalOperator(self, ctx:ExprParser.LogicalOperatorContext):
        pass



del ExprParser