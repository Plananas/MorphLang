from Syntax.AbstractSyntaxTree import AbstractSyntaxTree
from Token import Token


class BooleanUnaryOperator(AbstractSyntaxTree):
    def __init__(self, operator, expression):
        self.token = self.operator = operator
        self.expression = expression
