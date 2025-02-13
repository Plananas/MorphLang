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

    def visit_UnaryOperator(self, node):
        if node.operator.type == Type.MINUS:
            return -self.visit(node.expression)
        elif node.operator.type == Type.PLUS:
            return +self.visit(node.expression)

    def visit_BooleanOperator(self, node):
        if node.operator.type == Type.EQUALS:
            return self.visit(node.left) == self.visit(node.right)
        elif node.operator.type == Type.NOT_EQUALS:
            return self.visit(node.left) != self.visit(node.right)
        elif node.operator.type == Type.LESS_THAN:
            return self.visit(node.left) < self.visit(node.right)
        elif node.operator.type == Type.GREATER_THAN:
            return self.visit(node.left) > self.visit(node.right)
        elif node.operator.type == Type.LESS_THAN_OR_EQUAL:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.operator.type == Type.GREATER_THAN_OR_EQUAL:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.operator.type == Type.AND:
            return self.visit(node.left) and self.visit(node.right)
        elif node.operator.type == Type.OR:
            return self.visit(node.left) or self.visit(node.right)

    def visit_BooleanExpression(self, node):
        if node.token.type == Type.TRUE:
            return True
        elif node.token.type == Type.FALSE:
            return False

    def visit_BooleanUnaryOperator(self, node):
        if node.token.type == Type.NOT:
            return not self.visit(node.expression)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

