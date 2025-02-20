from Syntax.AbstractSyntaxTree import AbstractSyntaxTree

class WhileLoop(AbstractSyntaxTree):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body