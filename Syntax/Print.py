from Syntax.AbstractSyntaxTree import AbstractSyntaxTree


class Print(AbstractSyntaxTree):
    def __init__(self, expression):
        self.expression = expression