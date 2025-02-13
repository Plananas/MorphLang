from Syntax.AbstractSyntaxTree import AbstractSyntaxTree

class BinaryOperator(AbstractSyntaxTree):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
