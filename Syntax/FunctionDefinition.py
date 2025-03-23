from Syntax.AbstractSyntaxTree import AbstractSyntaxTree


class FunctionDefinition(AbstractSyntaxTree):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

