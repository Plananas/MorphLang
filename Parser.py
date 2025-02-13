from BinaryOperator import BinaryOperator
from CharacterType import CharacterType as Type
from Number import Number
from Token import Token

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def raise_error(self):
        raise Exception('Invalid input detected')


    def consume_token(self, expected_type):
        """
        Validates and consumes the current token.
        """
        if self.current_token.type == expected_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.raise_error()


    def parse_number(self):
        """
        Parses and returns an integer value.
        """
        token = self.current_token

        if token.type == Type.INTEGER:
            self.consume_token(Type.INTEGER)
            return Number(token)

        elif token.type == Type.LPAREN:
            self.consume_token(Type.LPAREN)
            #Recursively start the process again for the stuff in brackets
            result = self.create_expression()
            self.consume_token(Type.RPAREN)
            return result

        self.raise_error()


    def create_expression(self):
        """
        Parses arithmetic expressions.
        """
        result = self.parse_number()

        while self.current_token.type in (Type.MUL, Type.DIV, Type.PLUS, Type.MINUS):

            token = self.current_token
            if token.type == Type.MUL:
                self.consume_token(Type.MUL)
            elif token.type == Type.DIV:
                self.consume_token(Type.DIV)
            elif token.type == Type.PLUS:
                self.consume_token(Type.PLUS)
            elif token.type == Type.MINUS:
                self.consume_token(Type.MINUS)

            result = BinaryOperator(left=result, operator=token, right=self.parse_number())

        return result


    def parse(self):
        """
        Parses and evaluates the full arithmetic expression.
        """

        return self.create_expression()