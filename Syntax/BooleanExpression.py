from Syntax.AbstractSyntaxTree import AbstractSyntaxTree
from Token import Token


class BooleanExpression(AbstractSyntaxTree):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
