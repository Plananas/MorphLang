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

    def read_number(self):
        """
        Reads a number from the input. Supports both integers and floats.
        Returns an int if no decimal point is found, or a float otherwise.
        """
        number = ''
        # Read the integer part
        while self.current_character is not None and self.current_character.isdigit():
            number += self.current_character
            self.move_next()

        # Check for a decimal point to handle floats
        if self.current_character == '.':
            number += self.current_character
            self.move_next()
            # Ensure that at least one digit follows the decimal point
            if self.current_character is None or not self.current_character.isdigit():
                self.raise_error()  # e.g., "Expected digit after decimal point"
            while self.current_character is not None and self.current_character.isdigit():
                number += self.current_character
                self.move_next()
            return float(number)

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


    def read_identifier(self):
        """
        Reads an identifier from the input. An identifier starts with a letter
        and can contain letters, digits, or underscores.
        """
        identifier = ''
        while self.current_character is not None and (
                self.current_character.isalnum() or self.current_character == '_'):
            identifier += self.current_character
            self.move_next()
        return identifier


    def get_identifier_or_keyword(self):
        """
        Tokenizes an identifier or reserved keyword. If the identifier matches a
        reserved keyword (e.g., 'true', 'false', 'and', 'or', 'not'), return the
        corresponding token. Otherwise, treat it as a variable identifier.
        """
        identifier = self.read_identifier()
        keywords = {
            'true': lambda: Token(Type.TRUE, True),
            'false': lambda: Token(Type.FALSE, False),
            'and': lambda: Token(Type.AND, identifier),
            'or': lambda: Token(Type.OR, identifier),
            'not': lambda: Token(Type.NOT, identifier),
            'print': lambda: Token(Type.PRINT, identifier)
        }

        # Check if the identifier is a reserved keyword.
        if identifier.lower() in keywords:
            return keywords[identifier.lower()]()
        # Otherwise, return it as an identifier token.
        return Token(Type.IDENTIFIER, identifier)



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
                # If it is a newline, return a NEWLINE token.
                if self.current_character == '\n':
                    self.move_next()
                    return Token(Type.NEWLINE, '\n')
                # Otherwise, skip spaces and tabs.
                self.skip_spaces()
                continue

            if self.current_character.isdigit():
                return Token(Type.INTEGER, self.read_number())

            if self.isQuote(self.current_character):
                return Token(Type.STRING, self.read_string())

            if self.current_character.isalpha():
                return self.get_identifier_or_keyword()

            # Handle assignment operator '=' separately:
            if self.current_character == '=':
                self.move_next()
                if self.current_character == '=':
                    self.move_next()
                    return Token(Type.EQUALS, '==')
                else:
                    return Token(Type.ASSIGN, '=')

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
        operators = ['>', '<', '!', '|', '&']
        if current_character in operators:
            return True

        return False

    def isQuote(self, current_character):
        operators = ['"', "'"]
        if current_character in operators:
            return True

        return False
