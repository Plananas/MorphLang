from Token import Token
from CharacterType import CharacterType as Type

class Lexer(object):
    def __init__(self, expression):

        self.expression = expression
        self.position = 0
        self.current_character = self.expression[self.position] if self.expression else None


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


    def move_next(self):
        """
        Moves to the next character in the input and updates `current_char`.
        """
        self.position += 1
        self.current_character = self.expression[self.position] if self.position < len(self.expression) else None


    def get_next_token(self):
        """
        Tokenizes the input string.
        """

        # FIXME Make this better
        while self.current_character is not None:

            if self.current_character.isspace():
                self.skip_spaces()
                continue

            if self.current_character.isdigit():
                return Token(Type.INTEGER, self.read_integer())

            if self.current_character == '+':
                self.move_next()
                return Token(Type.PLUS, '+')
            if self.current_character == '-':
                self.move_next()
                return Token(Type.MINUS, '-')
            if self.current_character == '*':
                self.move_next()
                return Token(Type.MUL, '*')
            if self.current_character == '/':
                self.move_next()
                return Token(Type.DIV, '/')
            if self.current_character == '(':
                self.move_next()
                return Token(Type.LPAREN, '(')
            if self.current_character == ')':
                self.move_next()
                return Token(Type.RPAREN, ')')

            self.raise_error()

        return Token(Type.EOF, None)


    def raise_error(self):
        raise Exception('Invalid input detected')
