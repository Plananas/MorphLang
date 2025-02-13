from NodeVisitor import NodeVisitor
from CharacterType import CharacterType as Type


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser


    def visit_BinaryOperator(self, node):
        if node.operator.type == Type.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.operator.type == Type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.operator.type == Type.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.operator.type == Type.DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Number(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

