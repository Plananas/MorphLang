from CharacterType import CharacterType as Type
from Syntax.Assignment import Assignment
from Syntax.BinaryOperator import BinaryOperator
from Syntax.BooleanExpression import BooleanExpression
from Syntax.BooleanOperator import BooleanOperator
from Syntax.BooleanUnaryOperator import BooleanUnaryOperator
from Syntax.FunctionCall import FunctionCall
from Syntax.FunctionDefinition import FunctionDefinition
from Syntax.Input import Input
from Syntax.Number import Number
from Syntax.Print import Print
from Syntax.Return import Return
from Syntax.String import String
from Syntax.UnaryOperator import UnaryOperator
from Syntax.Variable import Variable
from Syntax.IfStatement import IfStatement
from Syntax.WhileLoop import WhileLoop


class Parser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def parse(self):
        """
        Parses the full program.
        """
        return self.parse_statements()


    def parse_statements(self, break_tokens=(Type.ELSE, Type.ENDIF, Type.END_WHILE, Type.END_FUNCTION)):
        """
        Parses a block of statements until a break token or EOF is reached.
        """
        statements = []
        while self.current_token.type != Type.EOF and self.current_token.type not in break_tokens:

            while self.current_token.type == Type.NEWLINE:
                self.consume_token(Type.NEWLINE)

            if self.current_token.type in break_tokens or self.current_token.type == Type.EOF:
                break

            if self.current_token.type == Type.WHILE:
                statements.append(self.parse_while_loop())

            elif self.current_token.type == Type.IF:
                statements.append(self.parse_if_statement())

            elif self.current_token.type == Type.FUNCTION:
                statements.append(self.parse_function_definition())

            else:
                statements.append(self.parse_statement())

            if self.current_token.type == Type.NEWLINE:
                self.consume_token(Type.NEWLINE)

        return statements


    def parse_statement(self):
        """
        Parses a single statement such as print, input, assignment, return, or function call.
        """
        token = self.current_token

        if token.type == Type.RETURN:

            return self.parse_return_statement()

        if token.type == Type.PRINT:
            self.consume_token(Type.PRINT)

            return Print(self.create_expression())

        if token.type == Type.INPUT:
            self.consume_token(Type.INPUT)
            prompt_expr = None

            if self.current_token.type == Type.LPAREN:
                self.consume_token(Type.LPAREN)
                prompt_expr = self.create_expression()
                self.consume_token(Type.RPAREN)

            return Input(prompt_expr)

        if token.type == Type.IDENTIFIER:
            var_token = self.current_token
            self.consume_token(Type.IDENTIFIER)

            if self.current_token.type == Type.LPAREN:

                return self.parse_function_call(FunctionCall(var_token.value, ''))

            elif self.current_token.type == Type.ASSIGN:
                self.consume_token(Type.ASSIGN)

                return Assignment(var_token, self.create_expression())

            return Variable(var_token)

        return self.create_expression()


    def parse_if_statement(self):
        """
        Parses an if else statement with conditional branches.
        """
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


    def parse_while_loop(self):
        """
        Parses a while-do loop with a condition and body.
        """
        self.consume_token(Type.WHILE)
        condition = self.create_expression()
        body = []

        if self.current_token.type == Type.THEN:
            self.consume_token(Type.THEN)
            body = self.parse_statements(break_tokens=(Type.END_WHILE,))

            if self.current_token.type == Type.END_WHILE:
                self.consume_token(Type.END_WHILE)

        return WhileLoop(condition, body)


    def parse_function_definition(self):
        """
        Parses a function definition including name, parameters, and body.
        """
        self.consume_token(Type.FUNCTION)
        name = self.current_token.value
        self.consume_token(Type.IDENTIFIER)
        parameters = []
        self.consume_token(Type.LPAREN)

        if self.current_token.type != Type.RPAREN:
            parameters.append(self.current_token.value)
            self.consume_token(Type.IDENTIFIER)

            while self.current_token.type == Type.COMMA:
                self.consume_token(Type.COMMA)
                parameters.append(self.current_token.value)
                self.consume_token(Type.IDENTIFIER)

        self.consume_token(Type.RPAREN)
        self.consume_token(Type.LBRACE)
        body = self.parse_statements(break_tokens=(Type.RBRACE,))
        self.consume_token(Type.RBRACE)

        return FunctionDefinition(name, parameters, body)


    def parse_function_call(self, function_expression):
        """
        Parses a function call with arguments.
        """
        self.consume_token(Type.LPAREN)
        arguments = []

        if self.current_token.type != Type.RPAREN:
            arguments.append(self.create_expression())

            while self.current_token.type == Type.COMMA:
                self.consume_token(Type.COMMA)
                arguments.append(self.create_expression())

        self.consume_token(Type.RPAREN)

        return FunctionCall(function_expression.name, arguments)


    def parse_return_statement(self):
        """
        Parses a return statement with an optional expression.
        """
        self.consume_token(Type.RETURN)
        expression = None

        if self.current_token.type not in (Type.NEWLINE, Type.RBRACE):
            expression = self.create_expression()

        return Return(expression)


    def create_expression(self):
        """
        Parses the top-level expression.
        """
        return self.parse_boolean_or()


    def parse_boolean_or(self):
        """
        Parses a logical OR expression.
        """
        node = self.parse_boolean_and()

        while self.current_token.type == Type.OR:
            token = self.current_token
            self.consume_token(token.type)
            node = BooleanOperator(left=node, operator=token, right=self.parse_boolean_and())

        return node


    def parse_boolean_and(self):
        """
        Parses a logical AND expression.
        """
        node = self.parse_equality()

        while self.current_token.type == Type.AND:
            token = self.current_token
            self.consume_token(token.type)
            node = BooleanOperator(left=node, operator=token, right=self.parse_equality())

        return node

    def parse_equality(self):
        """
        Parses equality expressions.
        """
        node = self.parse_comparison()

        while self.current_token.type in (Type.EQUALS, Type.NOT_EQUALS):
            token = self.current_token
            self.consume_token(token.type)
            node = BooleanOperator(left=node, operator=token, right=self.parse_comparison())

        return node


    def parse_comparison(self):
        """
        Parses relational comparison expressions.
        """
        node = self.parse_term()

        while self.current_token.type in (
            Type.LESS_THAN, Type.LESS_THAN_OR_EQUAL,
            Type.GREATER_THAN, Type.GREATER_THAN_OR_EQUAL
        ):
            token = self.current_token
            self.consume_token(token.type)
            node = BooleanOperator(left=node, operator=token, right=self.parse_term())

        return node

    def parse_term(self):
        """
        Parses addition and subtraction expressions.
        """
        node = self.parse_factor()

        while self.current_token.type in (Type.PLUS, Type.MINUS):
            token = self.current_token
            self.consume_token(token.type)
            node = BinaryOperator(left=node, operator=token, right=self.parse_factor())

        return node


    def parse_factor(self):
        """
        Parses multiplication and division expressions.
        """
        node = self.parse_unary()

        while self.current_token.type in (Type.MUL, Type.DIV):
            token = self.current_token
            self.consume_token(token.type)
            node = BinaryOperator(left=node, operator=token, right=self.parse_unary())

        return node


    def parse_unary(self):
        """
        Parses unary operators
        """
        if self.current_token.type in (Type.PLUS, Type.MINUS, Type.NOT):
            token = self.current_token
            self.consume_token(token.type)

            if token.type == Type.NOT:

                return BooleanUnaryOperator(token, self.parse_unary())

            else:

                return UnaryOperator(token, self.parse_unary())

        return self.parse_primary()


    def parse_primary(self):
        """
        Parses primary expressions such as variables
        """
        token = self.current_token

        if token.type == Type.INTEGER or token.type == Type.FLOAT:
            self.consume_token(token.type)

            return Number(token)

        elif token.type == Type.STRING:
            self.consume_token(token.type)

            return String(token)

        elif token.type in (Type.TRUE, Type.FALSE):
            self.consume_token(token.type)

            return BooleanExpression(token)

        elif token.type == Type.IDENTIFIER:
            var_token = token
            self.consume_token(Type.IDENTIFIER)

            if self.current_token.type == Type.LPAREN:

                return self.parse_function_call(FunctionCall(var_token.value, ''))

            return Variable(var_token)

        elif token.type == Type.LPAREN:
            self.consume_token(Type.LPAREN)
            expr = self.create_expression()
            self.consume_token(Type.RPAREN)

            return expr

        elif token.type == Type.INPUT:

            return self.parse_statement()

        self.raise_error("primary expression")


    def consume_token(self, expected_type):
        """
        Advances the current token if it matches the expected type, else raises a syntax error.
        """

        if self.current_token.type == expected_type:
            self.current_token = self.lexer.get_next_token()

        else:
            self.raise_error(expected_type)


    def raise_error(self, expected_type=None):
        """
        Raises a syntax error with detailed information about the unexpected token.
        """
        error_message = f"Syntax Error: Unexpected token '{self.current_token.value}' ({self.current_token.type})"

        if expected_type:
            error_message += f", expected: {expected_type}"

        error_message += f" at position {self.lexer.position}"

        raise Exception(error_message)