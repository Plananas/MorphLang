import sys

from Interpreter import Interpreter
from Lexer import Lexer
from Parser import Parser


class Morphlang:
    @staticmethod
    def run_file(filename):
        try:
            with open(filename, 'r') as file:
                text = file.read().strip()
                lexer = Lexer(text)
                parser = Parser(lexer)
                interpreter = Interpreter(parser)
                interpreter.interpret()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # TODO change this so that Morphlang is an executable or bin 
    # if len(sys.argv) != 2:
    #     print("Usage: python Morphlang.py <filename>.morph")
    # else:
    #   Main.run_file(sys.argv[1])

    Morphlang.run_file("ExampleCode/InputExample.morph")
