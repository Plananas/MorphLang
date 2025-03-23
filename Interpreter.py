from NodeVisitor import NodeVisitor
from CharacterType import CharacterType as Type


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.GLOBAL_SCOPE = {}


    def visit_BinaryOperator(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator.type == Type.PLUS:
            # Both operands are strings: perform string concatenation.
            if isinstance(left, str) and isinstance(right, str):
                return left + right

            # Both operands are numbers: perform numerical addition.
            elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right

            # If one operand is a string and the other a number, raise an error.
            elif (isinstance(left, str) and isinstance(right, (int, float))) or \
                    (isinstance(right, str) and isinstance(left, (int, float))):
                raise Exception("TypeError: Cannot concatenate a string with a number.")

            # Catch any other unsupported operand types.
            else:
                raise Exception("TypeError: Unsupported operand types for + operator.")

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


    def visit_Assignment(self, node):
        value = self.visit(node.right)
        self.GLOBAL_SCOPE[node.left.value] = value
        return value


    def visit_Variable(self, node):
        variable_name = node.value
        if variable_name in self.GLOBAL_SCOPE:
            return self.GLOBAL_SCOPE[variable_name]
        else:
            raise Exception(f"Name Error: Variable '{variable_name}' is not defined")


    def visit_Print(self, node):
        value = self.visit(node.expression)
        print(value)
        return value


    def visit_Input(self, node):
        prompt_text = self.visit(node.prompt) if node.prompt else ""

        # Read user input from the console.
        user_input = input(prompt_text)
        return user_input


    def visit_IfStatement(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.interpret_code_block(node.then_branch)
        else:
            return self.interpret_code_block(node.else_branch)
        pass


    def visit_WhileLoop(self, node):
        result = None

        while self.visit(node.condition):
            result = self.interpret_code_block(node.body)
        return result


    def visit_FunctionDefinition(self, node):
        function_object = {
            'name': node.name,
            'body': node.body,
            'closure': self.GLOBAL_SCOPE.copy(),
        }

        self.GLOBAL_SCOPE[node.name] = function_object
        return function_object

    def visit_FunctionCall(self, node):

        function_object = self.GLOBAL_SCOPE[node.name]

        # Prepare a new local scope from the function's closure.
        local_scope = function_object['closure'].copy()

        # TODO grab the parameters and add them to the local scope

        # Save the current scope and set the new local scope.
        previous_scope = self.GLOBAL_SCOPE
        self.GLOBAL_SCOPE = local_scope

        # Execute the function body within the new scope.
        result = self.interpret_code_block(function_object['body'])

        # Restore the previous scope.
        self.GLOBAL_SCOPE = previous_scope

        # For a void function, result might be None.
        return result

    def interpret(self):
        # 'tree' is a list of AST nodes (statements)
        tree = self.parser.parse()
        return self.interpret_code_block(tree)

    def interpret_code_block(self, statements):
        result = None
        for statement in statements:
            result = self.interpret_line_of_code(statement)
        return result

    def interpret_line_of_code(self, statement):
        return self.visit(statement)