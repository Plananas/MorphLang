from CharacterType import CharacterType as Type
from Syntax.Assignment import Assignment
from Syntax.BinaryOperator import BinaryOperator
from Syntax.BooleanExpression import BooleanExpression
from Syntax.BooleanOperator import BooleanOperator
from Syntax.BooleanUnaryOperator import BooleanUnaryOperator
from Syntax.Number import Number
from Syntax.Print import Print
from Syntax.String import String
from Syntax.UnaryOperator import UnaryOperator
from Syntax.Variable import Variable
from Syntax.IfStatement import IfStatement


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

    def parse_statement(self):
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
            Type.FLOAT: Number,
            Type.STRING: String,
            Type.TRUE: BooleanExpression,
            Type.FALSE: BooleanExpression
        }

        if token.type in unary_operators:
            self.consume_token(token.type)
            return unary_operators[token.type](token, self.parse_statement())

        elif token.type in constants:
            self.consume_token(token.type)
            return constants[token.type](token)

        elif token.type == Type.LPAREN:
            self.consume_token(Type.LPAREN)
            result = self.create_expression()
            self.consume_token(Type.RPAREN)
            return result

        elif self.current_token.type == Type.PRINT:
            self.consume_token(Type.PRINT)
            # Optionally, if you want parentheses: check and consume LPAREN here.
            expression = self.create_expression()
            # Optionally, if you want to enforce a closing parenthesis, check for RPAREN.
            return Print(expression)

        elif token.type == Type.IDENTIFIER:
            variable_token = self.current_token
            self.consume_token(Type.IDENTIFIER)
            if self.current_token.type == Type.ASSIGN:
                self.consume_token(Type.ASSIGN)
                expression = self.create_expression()
                return Assignment(variable_token, expression)
            else:
                # Not an assignment; treat it as a variable expression
                return Variable(variable_token)

        self.raise_error("an integer, boolean, unary operator, or '('")


    def parse_statements(self, break_tokens=(Type.ELSE, Type.ENDIF)):
        """
        Parses multiple statements separated by newlines.
        """
        statements = []
        while self.current_token.type != Type.EOF and self.current_token.type not in break_tokens:

            # Skip extra newlines
            while self.current_token.type == Type.NEWLINE:
                self.consume_token(Type.NEWLINE)
            if self.current_token.type == Type.EOF:
                break

            if self.current_token.type == Type.IF:
                statements.append(self.parse_if_statement())
            else:
                statement = self.create_expression()
                statements.append(statement)

            # Optionally, consume a newline after each statement
            if self.current_token.type == Type.NEWLINE:
                self.consume_token(Type.NEWLINE)
        return statements

    def parse_if_statement(self):
        self.consume_token(Type.IF)
        condition = self.create_expression()
        then_branch = []
        else_branch = []
        if self.current_token.type == Type.THEN:
            self.consume_token(Type.THEN)
            then_branch = self.parse_statements(break_tokens=(Type.ELSE, Type.ENDIF))

            if self.current_token.type == Type.ELSE:
                self.consume_token(Type.ELSE)
                else_branch = self.parse_statements(break_tokens=(Type.ENDIF,))
            if self.current_token.type == Type.ENDIF:
                self.consume_token(Type.ENDIF)
        return IfStatement(condition, then_branch, else_branch)

    def create_expression(self):
        """
        Parses the current token and creates an expression.
        """
        result = self.parse_statement()

        # Process arithmetic operators (*, /, +, -)
        while self.current_token.type in (Type.MUL, Type.DIV, Type.PLUS, Type.MINUS):
            token = self.current_token
            self.consume_token(token.type)
            result = BinaryOperator(left=result, operator=token, right=self.parse_statement())

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


        if self.current_token.type not in (Type.EOF, Type.RPAREN, Type.NEWLINE, Type.THEN, Type.ENDIF):
            self.raise_error("an operator, newline, or end of expression")

        return result


    def parse(self):
        """
        Parses and evaluates the full arithmetic expression.
        """

        return self.parse_statements()