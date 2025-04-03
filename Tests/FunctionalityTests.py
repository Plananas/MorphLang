import unittest
import ExampleFiles
from Morphlang import Morphlang
import io
import sys

class FunctionalityTests(unittest.TestCase):


    def test_boolean_logic(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.BOOLEAN_EXAMPLE_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
            "False\n"
        )
        self.assertEqual(capturedOutput.getvalue(), expected_output)


    def test_mathematical_operations(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.MATH_EXAMPLE_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            '3\n'  # 1 + 2
            '2\n'  # 5 - 3
            '24\n'  # 4 * 6
            '4.0\n'  # 8 / 2
            '20\n'  # (2 + 3) * 4
            '14\n'  # 2 + 3 * 4
            '2.0\n'  # (10 - 4) / 3
            '3.5\n'  # 7 / 2
            '7.8\n'  # 5.5 + 2.3
            '4.5\n'  # 3.0 * 1.5
            '5\n'  # -5 + 10
            '6\n'  # -3 * -2
            '-3.5\n'  # -7 / 2
            '63.0\n'  # ((1 + 5 * 11) + (10 / 2)) + 2
            '282.0\n'  # ((1 + 5 * 11) * (10 / 2)) + 2
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)


    def test_string_concatenation(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.STRING_CONCATENATION_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "HelloWorld\n"
            "Hello World\n"
            "This is a sentence.\n"
            "Non-empty\n"
            "Non-empty\n"
            "\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)


    def test_string_concat_boolean_operations(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.STRING_CONCATENATION_AND_BOOL_OPERATION_File)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "True\n"
            "False\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_variable_assignment(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.VARIABLE_ASSIGNMENT_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "5\n"
            "8\n"
            "16\n"
            "8\n"
            "10\n"
            "11\n"
            "22\n"
            "12\n"
            "Hello, Morph\n"
            "True\n"
            "False\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_if_and_nested_if_statements(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.IF_STATEMENT_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "True block\n"
            "x is greater than 5\n"
            "x is positive\n"
            "x is also greater than 5\n"
            "x is exactly 10\n"
            "y is big\n"
            "Not Else\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)


    def test_while_loops_and_nested_structures(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.WHILE_LOOP_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "0\n"
            "1\n"
            "2\n"
            "inner loop\n"
            "inner loop\n"
            "outer loop\n"
            "inner loop\n"
            "inner loop\n"
            "outer loop\n"
            "even\n"
            "even\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_function_definition_and_usage(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.FUNCTION_EXAMPLE_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "5\n"
            "15\n"
            "15\n"
            "13\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_scope_rules_strict_block_scoping(self):
        capturedOutput = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = capturedOutput

        try:
            Morphlang().run_file(ExampleFiles.SCOPE_EXAMPLE_FILE)
        finally:
            sys.stdout = sys_stdout

        expected_output = (
            "global\n"
            "modified in if\n"
            "defined in if\n"
            "modified in if\n"
            "inside while\n"
            "inside function\n"
            "101\n"
            "102\n"
            "102\n"
            "102\n"
        )

        self.assertEqual(capturedOutput.getvalue(), expected_output)


