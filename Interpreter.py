from NodeVisitor import NodeVisitor
from CharacterType import CharacterType as Type


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator.type == Type.PLUS:
            if isinstance(left, str) and isinstance(right, str):
                # String concatenation
                return left + right
            elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                # Numerical addition
                return left + right
            else:
                raise Exception(
                    "Type Error: '+' operator requires both operands to be of the same type (either both strings or both numbers)")

        elif node.operator.type == Type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.operator.type == Type.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.operator.type == Type.DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Number(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_UnaryOperator(self, node):
        if node.operator.type == Type.MINUS:
            return -self.visit(node.expression)
        elif node.operator.type == Type.PLUS:
                return self.visit(node.left) + self.visit(node.right)

    def visit_BooleanOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator.type in (Type.EQUALS, Type.NOT_EQUALS):
            # Ensure both operands are of the same type
            if type(left) != type(right):
                raise Exception("Type Error: Cannot compare different types")

            if node.operator.type == Type.EQUALS:
                return left == right
            else:
                return left != right

        elif node.operator.type == Type.LESS_THAN:
            return left < right
        elif node.operator.type == Type.GREATER_THAN:
            return left > right
        elif node.operator.type == Type.LESS_THAN_OR_EQUAL:
            return left <= right
        elif node.operator.type == Type.GREATER_THAN_OR_EQUAL:
            return left >= right
        elif node.operator.type in (Type.AND, Type.OR):
            # Convert strings to booleans, an empty string will equal false
            if isinstance(left, str):
                left = bool(left)
            if isinstance(right, str):
                right = bool(right)

            if node.operator.type == Type.AND:
                return left and right
            else:
                return left or right

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

