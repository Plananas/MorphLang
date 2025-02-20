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

#String Operations
STRING_CONCATENATION_FILE = "ExampleCode/StringConcatenation.morph"
STRING_CONCATENATION_AND_BOOL_OPERATION = "ExampleCode/StringConcatenationBoolOperation.morph"
STRING_CONCATENATION_AND_BOOL_OPERATION_WITH_NUMBERS = "ExampleCode/StringConcatenationBoolOperationWithNumbers.morph"

#Variable Assignment
VARIABLE_ASSIGNMENT_FILE = "ExampleCode/VariableAssignment.morph"
VARIABLE_ASSIGNMENT_TWO_FILE = "ExampleCode/VariableAssignmentTwo.morph"
VARIABLE_ASSIGNMENT_THREE_FILE = "ExampleCode/VariableAssignmentThree.morph"

#If Statement Logic
IF_STATEMENT_FILE = "ExampleCode/IfStatementLogic.morph"


class Main:
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

    Main.run_file(IF_STATEMENT_FILE)
