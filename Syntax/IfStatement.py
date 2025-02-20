from Syntax.AbstractSyntaxTree import AbstractSyntaxTree

class IfStatement(AbstractSyntaxTree):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch