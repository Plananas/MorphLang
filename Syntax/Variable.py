from Syntax.AbstractSyntaxTree import AbstractSyntaxTree


class Variable(AbstractSyntaxTree):
    def __init__(self, token):
        self.token = token
        self.value = token.value