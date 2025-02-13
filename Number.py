from AbstractSyntaxTree import AbstractSyntaxTree
from Token import Token


class Number(AbstractSyntaxTree):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
