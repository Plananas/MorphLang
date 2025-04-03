import sys

from Interpreter import Interpreter
from Lexer import Lexer
from Parser import Parser

#Addition Examples
SIMPLE_ADDITION_FILE = "ExampleCode/SimpleAddition.morph"
COMPLEX_ADDITION_FILE = "ExampleCode/MathExamples.morph"

#Boolean Logic Examples
BOOLEAN_EXAMPLES = "ExampleCode/BooleanExamples.morph"


#String Operations
STRING_CONCATENATION_FILE = "ExampleCode/StringConcatenationExamples.morph"
STRING_CONCATENATION_AND_BOOL_OPERATION = "ExampleCode/StringConcatenationBoolOperation.morph"
STRING_CONCATENATION_AND_BOOL_OPERATION_WITH_NUMBERS = "ExampleCode/StringConcatenationBoolOperationWithNumbers.morph"

#Variable Assignment
VARIABLE_ASSIGNMENT_FILE = "ExampleCode/VariableAssignment.morph"
VARIABLE_ASSIGNMENT_TWO_FILE = "ExampleCode/VariableAssignmentTwo.morph"
VARIABLE_ASSIGNMENT_THREE_FILE = "ExampleCode/VariableAssignmentThree.morph"

#If Statement Logic
IF_STATEMENT_FILE = "ExampleCode/IfStatementLogic.morph"

WHILE_LOOP_FILE = "ExampleCode/WhileLoop.morph"
NESTED = "ExampleCode/Nested.morph"

VOID_FUNCTION = "ExampleCode/VoidFunction.morph"


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

    Morphlang.run_file(BOOLEAN_EXAMPLES)
