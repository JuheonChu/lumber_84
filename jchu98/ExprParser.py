# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        87,8,6,1,7,1,7,1,7,3,7,92,8,7,1,7,3,7,95,8,7,1,8,1,8,1,9,1,9,1,9,
        3,9,102,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,0,1,10,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,4,1,0,24,25,2,0,5,5,10,13,2,0,1,1,14,
        18,1,0,19,22,111,0,29,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,41,1,0,
        0,0,8,48,1,0,0,0,10,61,1,0,0,0,12,86,1,0,0,0,14,88,1,0,0,0,16,96,
        1,0,0,0,18,101,1,0,0,0,20,103,1,0,0,0,22,105,1,0,0,0,24,107,1,0,
        0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,1,1,0,0,0,31,29,1,0,0,0,32,36,3,4,2,0,33,36,3,6,3,0,34,
        36,3,8,4,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,
        0,37,38,3,14,7,0,38,39,5,1,0,0,39,40,3,10,5,0,40,5,1,0,0,0,41,42,
        5,2,0,0,42,43,3,10,5,0,43,44,3,22,11,0,44,45,3,10,5,0,45,46,5,3,
        0,0,46,47,3,8,4,0,47,7,1,0,0,0,48,49,5,4,0,0,49,50,5,23,0,0,50,9,
        1,0,0,0,51,52,6,5,-1,0,52,53,5,5,0,0,53,62,3,10,5,8,54,55,5,6,0,
        0,55,56,3,10,5,0,56,57,5,7,0,0,57,62,1,0,0,0,58,62,3,12,6,0,59,62,
        3,14,7,0,60,62,3,16,8,0,61,51,1,0,0,0,61,54,1,0,0,0,61,58,1,0,0,
        0,61,59,1,0,0,0,61,60,1,0,0,0,62,77,1,0,0,0,63,64,10,3,0,0,64,65,
        3,20,10,0,65,66,3,10,5,4,66,76,1,0,0,0,67,68,10,2,0,0,68,69,3,22,
        11,0,69,70,3,10,5,3,70,76,1,0,0,0,71,72,10,1,0,0,72,73,3,24,12,0,
        73,74,3,10,5,2,74,76,1,0,0,0,75,63,1,0,0,0,75,67,1,0,0,0,75,71,1,
        0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,11,1,0,0,0,79,
        77,1,0,0,0,80,81,5,23,0,0,81,82,5,6,0,0,82,83,3,10,5,0,83,84,5,7,
        0,0,84,87,1,0,0,0,85,87,5,23,0,0,86,80,1,0,0,0,86,85,1,0,0,0,87,
        13,1,0,0,0,88,91,5,23,0,0,89,90,5,8,0,0,90,92,5,23,0,0,91,89,1,0,
        0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,5,9,0,0,94,93,1,0,0,0,94,95,
        1,0,0,0,95,15,1,0,0,0,96,97,7,0,0,0,97,17,1,0,0,0,98,102,3,20,10,
        0,99,102,3,22,11,0,100,102,3,24,12,0,101,98,1,0,0,0,101,99,1,0,0,
        0,101,100,1,0,0,0,102,19,1,0,0,0,103,104,7,1,0,0,104,21,1,0,0,0,
        105,106,7,2,0,0,106,23,1,0,0,0,107,108,7,3,0,0,108,25,1,0,0,0,9,
        29,35,61,75,77,86,91,94,101
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'IF'", "'THEN'", "'CALL'", "'-'", 
                     "'('", "')'", "'.'", "'$'", "'^'", "'*'", "'/'", "'+'", 
                     "'<'", "'<='", "'>'", "'>='", "'<>'", "'NOT'", "'AND'", 
                     "'OR'", "'XOR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_conditionalStatement = 3
    RULE_functionCall = 4
    RULE_expression = 5
    RULE_functionReference = 6
    RULE_variable = 7
    RULE_constant = 8
    RULE_operator = 9
    RULE_arithmeticOperators = 10
    RULE_relationalOperator = 11
    RULE_logicalOperator = 12

    ruleNames =  [ "program", "statement", "assignment", "conditionalStatement", 
                   "functionCall", "expression", "functionReference", "variable", 
                   "constant", "operator", "arithmeticOperators", "relationalOperator", 
                   "logicalOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    ID=23
    STRING=24
    NUMBER=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8388628) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(ExprParser.ConditionalStatementContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ExprParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.conditionalStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.functionCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(ExprParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignment




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.variable()
            self.state = 38
            self.match(ExprParser.T__0)
            self.state = 39
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(ExprParser.RelationalOperatorContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ExprParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_conditionalStatement




    def conditionalStatement(self):

        localctx = ExprParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditionalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ExprParser.T__1)
            self.state = 42
            self.expression(0)
            self.state = 43
            self.relationalOperator()
            self.state = 44
            self.expression(0)
            self.state = 45
            self.match(ExprParser.T__2)
            self.state = 46
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_functionCall




    def functionCall(self):

        localctx = ExprParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExprParser.T__3)
            self.state = 49
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArithExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def arithmeticOperators(self):
            return self.getTypedRuleContext(ExprParser.ArithmeticOperatorsContext,0)



    class ConstExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(ExprParser.ConstantContext,0)



    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def relationalOperator(self):
            return self.getTypedRuleContext(ExprParser.RelationalOperatorContext,0)



    class LogicExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def logicalOperator(self):
            return self.getTypedRuleContext(ExprParser.LogicalOperatorContext,0)



    class FuncRefExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionReference(self):
            return self.getTypedRuleContext(ExprParser.FunctionReferenceContext,0)



    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)



    class VarExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(ExprParser.VariableContext,0)



    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)




    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.match(ExprParser.T__4)
                self.state = 53
                self.expression(8)
                pass

            elif la_ == 2:
                localctx = ExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(ExprParser.T__5)
                self.state = 55
                self.expression(0)
                self.state = 56
                self.match(ExprParser.T__6)
                pass

            elif la_ == 3:
                localctx = ExprParser.FuncRefExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.functionReference()
                pass

            elif la_ == 4:
                localctx = ExprParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.variable()
                pass

            elif la_ == 5:
                localctx = ExprParser.ConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.constant()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ArithExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        self.arithmeticOperators()
                        self.state = 65
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.RelExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 68
                        self.relationalOperator()
                        self.state = 69
                        self.expression(3)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.LogicExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 72
                        self.logicalOperator()
                        self.state = 73
                        self.expression(2)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_functionReference




    def functionReference(self):

        localctx = ExprParser.FunctionReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionReference)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(ExprParser.ID)
                self.state = 81
                self.match(ExprParser.T__5)
                self.state = 82
                self.expression(0)
                self.state = 83
                self.match(ExprParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ExprParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_variable




    def variable(self):

        localctx = ExprParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ExprParser.ID)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(ExprParser.T__7)
                self.state = 90
                self.match(ExprParser.ID)


            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(ExprParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_constant




    def constant(self):

        localctx = ExprParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticOperators(self):
            return self.getTypedRuleContext(ExprParser.ArithmeticOperatorsContext,0)


        def relationalOperator(self):
            return self.getTypedRuleContext(ExprParser.RelationalOperatorContext,0)


        def logicalOperator(self):
            return self.getTypedRuleContext(ExprParser.LogicalOperatorContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_operator




    def operator(self):

        localctx = ExprParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.arithmeticOperators()
                pass
            elif token in [1, 14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.relationalOperator()
                pass
            elif token in [19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.logicalOperator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_arithmeticOperators




    def arithmeticOperators(self):

        localctx = ExprParser.ArithmeticOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arithmeticOperators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_relationalOperator




    def relationalOperator(self):

        localctx = ExprParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 507906) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_logicalOperator




    def logicalOperator(self):

        localctx = ExprParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




