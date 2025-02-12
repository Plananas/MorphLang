from Token import LPAREN, MUL, DIV, PLUS, MINUS, INTEGER, RPAREN, Token, EOF


class Interpreter:
    def __init__(self, expression):
        self.expression = expression
        self.position = 0
        self.current_character = self.expression[self.position] if self.expression else None
        self.current_token = None


    def raise_error(self):
        raise Exception('Invalid input detected')


    def move_next(self):
        """
        Moves to the next character in the input and updates `current_char`.
        """
        self.position += 1
        self.current_character = self.expression[self.position] if self.position < len(self.expression) else None


    def skip_spaces(self):
        """
        Skips whitespace characters.
        """
        while self.current_character is not None and self.current_character.isspace():
            self.move_next()


    def read_integer(self):
        """
        Extracts a multi-digit integer from the input.
        """
        number = ''
        while self.current_character is not None and self.current_character.isdigit():
            number += self.current_character
            self.move_next()
        return int(number)


    def get_next_token(self):
        """
        Tokenizes the input string.
        """
        while self.current_character is not None:

            if self.current_character.isspace():
                self.skip_spaces()
                continue

            if self.current_character.isdigit():
                return Token(INTEGER, self.read_integer())

            if self.current_character == '+':
                self.move_next()
                return Token(PLUS, '+')
            if self.current_character == '-':
                self.move_next()
                return Token(MINUS, '-')
            if self.current_character == '*':
                self.move_next()
                return Token(MUL, '*')
            if self.current_character == '/':
                self.move_next()
                return Token(DIV, '/')
            if self.current_character == '(':
                self.move_next()
                return Token(LPAREN, '(')
            if self.current_character == ')':
                self.move_next()
                return Token(RPAREN, ')')

            self.raise_error()

        return Token(EOF, None)


    def consume_token(self, expected_type):
        """
        Validates and consumes the current token.
        """
        if self.current_token.type == expected_type:
            self.current_token = self.get_next_token()
        else:
            self.raise_error()


    def parse_number(self):
        """
        Parses and returns an integer value.
        """
        token = self.current_token

        if token.type == INTEGER:
            self.consume_token(INTEGER)
            return token.value

        elif token.type == LPAREN:
            self.consume_token(LPAREN)
            result = self.parse_arithmetic()
            self.consume_token(RPAREN)
            return result

        self.raise_error()


    def parse_arithmetic(self):
        """
        Parses arithmetic expressions.
        """
        result = self.parse_number()

        while self.current_token.type in (MUL, DIV, PLUS, MINUS):
            

            token = self.current_token
            if token.type == MUL:
                self.consume_token(MUL)
                result *= self.parse_number()
            elif token.type == DIV:
                self.consume_token(DIV)
                result /= self.parse_number()
            elif token.type == PLUS:
                self.consume_token(PLUS)
                result += self.parse_arithmetic()
            elif token.type == MINUS:
                self.consume_token(MINUS)
                result -= self.parse_arithmetic()

        return result


    def evaluate_expression(self):
        """
        Parses and evaluates the full arithmetic expression.
        """
        self.current_token = self.get_next_token()

        result = self.parse_arithmetic()

        return result

