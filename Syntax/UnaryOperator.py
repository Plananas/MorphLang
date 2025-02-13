from Syntax.AbstractSyntaxTree import AbstractSyntaxTree
from Token import Token


class UnaryOperator(AbstractSyntaxTree):
    def __init__(self, operator, expression):
        self.token = self.operator = operator
        self.expression = expression
