from CharacterType              import CharacterType as Type
from Syntax.BinaryOperator      import BinaryOperator
from Syntax.BooleanExpression import BooleanExpression
from Syntax.BooleanOperator import BooleanOperator
from Syntax.BooleanUnaryOperator import BooleanUnaryOperator
from Syntax.Number              import Number
from Syntax.String              import String
from Syntax.UnaryOperator       import UnaryOperator


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def raise_error(self, expected_type=None):
        """
        Raises an error with a detailed message about the unexpected token.
        """
        error_message = f"Syntax Error: Unexpected token '{self.current_token.value}' ({self.current_token.type})"

        if expected_type:
            error_message += f", expected: {expected_type}"

        error_message += f" at position {self.lexer.position}"

        raise Exception(error_message)


    def consume_token(self, expected_type):
        """
        Validates and consumes the current token.
        """
        if self.current_token.type == expected_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.raise_error(expected_type)

    def parse_character(self):
        """
        Parses and returns an integer, boolean, unary, or grouped expression.
        """
        token = self.current_token

        unary_operators = {
            Type.PLUS: UnaryOperator,
            Type.MINUS: UnaryOperator,
            Type.NOT: BooleanUnaryOperator
        }
        constants = {
            Type.INTEGER: Number,
            Type.STRING: String,
            Type.TRUE: BooleanExpression,
            Type.FALSE: BooleanExpression
        }

        if token.type in unary_operators:
            self.consume_token(token.type)
            return unary_operators[token.type](token, self.parse_character())

        elif token.type in constants:
            self.consume_token(token.type)
            return constants[token.type](token)

        elif token.type == Type.LPAREN:
            self.consume_token(Type.LPAREN)
            result = self.create_expression()
            self.consume_token(Type.RPAREN)
            return result

        self.raise_error("an integer, boolean, unary operator, or '('")

    def create_expression(self):
        """
        Parses expressions with arithmetic and boolean operators.
        """
        result = self.parse_character()

        # Process arithmetic operators (*, /, +, -)
        while self.current_token.type in (Type.MUL, Type.DIV, Type.PLUS, Type.MINUS):
            token = self.current_token
            self.consume_token(token.type)
            result = BinaryOperator(left=result, operator=token, right=self.parse_character())

        # Process chained boolean comparisons (e.g., 5 - 4 == 3 * 2 == !false)
        boolean_operators = {
            Type.EQUALS: BooleanOperator,
            Type.NOT_EQUALS: BooleanOperator,
            Type.LESS_THAN: BooleanOperator,
            Type.GREATER_THAN: BooleanOperator,
            Type.AND: BooleanOperator,
            Type.OR: BooleanOperator
        }

        while self.current_token.type in boolean_operators:
            token = self.current_token
            self.consume_token(token.type)
            right_expr = self.create_expression()

            # Wrap into another BooleanOperator if necessary
            result = BooleanOperator(left=result, operator=token, right=right_expr)

        # Ensure the expression ends correctly (prevents invalid tokens at the end)
        if self.current_token.type not in (Type.EOF, Type.RPAREN):
            self.raise_error("an operator or end of expression")

        return result


    def parse(self):
        """
        Parses and evaluates the full arithmetic expression.
        """

        return self.create_expression()