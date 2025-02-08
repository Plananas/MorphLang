from Token import MUL, DIV, PLUS, MINUS, INTEGER, Token, EOF


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')


    def advance(self):
        """
        Move to the next character in the input and update `current_char`.
        """
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None


    def skip_whitespace(self):
        """
        Skip over whitespace characters.
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()


    def integer(self):
        """
        Extract a multi-digit integer from input.
        """
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return int(num_str)

    def get_next_token(self):
        """
        Lexical analyzer: Extracts tokens from input.
        """
        while self.current_char is not None:

            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # integer
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            # Operators
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        """
        Consume the current token if it matches the expected type.
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def factor(self):
        """
        factor -> INTEGER
        """
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """
        term -> factor ((MUL | DIV) factor)*
        """
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result /= self.factor()

        return result

    def expr(self):
        """
        expr -> term ((PLUS | MINUS) term)*
        """
        self.current_token = self.get_next_token()
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()

        return result
