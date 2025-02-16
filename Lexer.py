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


    def read_string(self):
        """
        Extracts a string from a string input.
        """
        quote_char = self.current_character  # e.g., " or '
        self.move_next()  # Skip the opening quote
        string = ''
        while self.current_character is not None and self.current_character != quote_char:
            string += self.current_character
            self.move_next()
        if self.current_character != quote_char:
            self.raise_error()  # Or handle unterminated string error
        self.move_next()  # Skip the closing quote
        return string


    def move_next(self):
        """
        Moves to the next character in the input and updates `current_char`.
        """
        self.position += 1
        self.current_character = self.expression[self.position] if self.position < len(self.expression) else None


    def get_boolean_token(self):
        """
        Tokenizes the boolean operator.
        """
        operator = ''
        while self.current_character is not None and self.isBooleanOperator(self.current_character):
            operator += self.current_character
            self.move_next()

        if operator == '==':
            return Token(Type.EQUALS, operator)
        elif operator == '!=':
            return Token(Type.NOT_EQUALS, operator)
        elif operator == '<':
            return Token(Type.LESS_THAN, operator)
        elif operator == '>':
            return Token(Type.GREATER_THAN, operator)
        elif operator == '<=':
            return Token(Type.LESS_THAN_OR_EQUAL, operator)
        elif operator == '>=':
            return Token(Type.GREATER_THAN_OR_EQUAL, operator)
        elif operator == '!':
            return Token(Type.NOT, operator)
        elif operator == '&':
            return Token(Type.AND, operator)
        elif operator == '&&':
            return Token(Type.AND, operator)
        elif operator == '|':
            return Token(Type.OR, operator)
        elif operator == '||':
            return Token(Type.OR, operator)

        self.raise_error()


    def get_alpha_token(self):
        """
        Tokenizes the alpha character.
        This will be used for variable declarations, and boolean expressions.
        """
        string = ''
        while self.current_character is not None and self.current_character.isalpha():
            string += self.current_character
            self.move_next()
        if string.lower() == 'true':
            return Token(Type.TRUE, True)

        elif string.lower() == 'false':
            return Token(Type.FALSE, False)

        elif string.lower() == 'and':
            return Token(Type.AND, string)

        elif string.lower() == 'or':
            return Token(Type.OR, string)

        elif string.lower() == 'not':
            return Token(Type.NOT, string)

        self.raise_error()

    def get_next_token(self):
        """
        Tokenizes the input string.
        """
        # Mapping for single-character tokens.
        single_char_tokens = {
            '+': Type.PLUS,
            '-': Type.MINUS,
            '*': Type.MUL,
            '/': Type.DIV,
            '(': Type.LPAREN,
            ')': Type.RPAREN,
        }

        while self.current_character is not None:
            if self.current_character.isspace():
                self.skip_spaces()
                continue

            if self.current_character.isdigit():
                return Token(Type.INTEGER, self.read_integer())

            if self.isQuote(self.current_character):
                return Token(Type.STRING, self.read_string())

            if self.current_character.isalpha():
                return self.get_alpha_token()

            if self.isBooleanOperator(self.current_character):
                return self.get_boolean_token()

            # Check for single-character tokens using the mapping.
            if self.current_character in single_char_tokens:
                token_type = single_char_tokens[self.current_character]
                char = self.current_character
                self.move_next()
                return Token(token_type, char)

            self.raise_error()

        return Token(Type.EOF, None)


    def raise_error(self):
        raise Exception('Invalid input detected')


    def isBooleanOperator(self, current_character):
        operators = ['=', '>', '<', '!', '|', '&']
        if current_character in operators:
            return True

        return False

    def isQuote(self, current_character):
        operators = ['"', "'"]
        if current_character in operators:
            return True

        return False
