import sys

from Interpreter import Interpreter


SIMPLE_ADDITION_FILE = "ExampleCode/SimpleAddition.morph"


class Main:
    @staticmethod
    def run_file(filename):
        try:
            with open(filename, 'r') as file:
                text = file.read().strip()  # Read the entire file
                interpreter = Interpreter(text)
                result = interpreter.expr()
                print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # TODO change this so that Morphlang is an executable
    # if len(sys.argv) != 2:
    #     print("Usage: python Morphlang.py <filename>.morph")
    # else:
    #   Main.run_file(sys.argv[1])

    Main.run_file(SIMPLE_ADDITION_FILE)
