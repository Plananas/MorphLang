from Syntax.AbstractSyntaxTree import AbstractSyntaxTree


class Assignment(AbstractSyntaxTree):
    def __init__(self, left, right):
        self.left = left
        self.right = right