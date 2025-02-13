import sys

from Interpreter import Interpreter
from Lexer import Lexer
from Parser import Parser

#Addition Examples
SIMPLE_ADDITION_FILE = "ExampleCode/SimpleAddition.morph"
COMPLEX_ADDITION_FILE = "ExampleCode/ComplexAddition.morph"

#Boolean Logic Examples
BOOLEAN_LOGIC_FILE_ONE = "ExampleCode/BooleanLogic1.morph"
BOOLEAN_LOGIC_FILE_TWO = "ExampleCode/BooleanLogic2.morph"
BOOLEAN_LOGIC_FILE_THREE = "ExampleCode/BooleanLogic3.morph"
BOOLEAN_LOGIC_FILE_FOUR = "ExampleCode/BooleanLogic4.morph"
BOOLEAN_LOGIC_FILE_FIVE = "ExampleCode/BooleanLogic5.morph"
BOOlEAN_LOGIC_FILE_SIX = "ExampleCode/BooleanLogic6.morph"

class Main:
    @staticmethod
    def run_file(filename):
        try:
            with open(filename, 'r') as file:
                text = file.read().strip()
                lexer = Lexer(text)
                parser = Parser(lexer)
                interpreter = Interpreter(parser)
                result = interpreter.interpret()
                print(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # TODO change this so that Morphlang is an executable or bin
    # if len(sys.argv) != 2:
    #     print("Usage: python Morphlang.py <filename>.morph")
    # else:
    #   Main.run_file(sys.argv[1])

    Main.run_file(BOOlEAN_LOGIC_FILE_SIX)
