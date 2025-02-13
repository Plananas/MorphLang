from Syntax.AbstractSyntaxTree import AbstractSyntaxTree

class BooleanOperator(AbstractSyntaxTree):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
