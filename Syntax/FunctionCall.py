from Syntax.AbstractSyntaxTree import AbstractSyntaxTree

class FunctionCall(AbstractSyntaxTree):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

