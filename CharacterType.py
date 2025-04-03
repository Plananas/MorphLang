from enum import Enum

class CharacterType(Enum):
    INTEGER = 1

    #Binary Operations
    PLUS = 2
    MINUS = 3
    MUL = 4
    DIV = 5
    LPAREN = 6
    RPAREN = 7

    #Boolean Operations
    EQUALS = 8
    NOT_EQUALS = 9
    LESS_THAN = 10
    GREATER_THAN = 11
    NOT = 12
    AND = 13
    OR = 14
    GREATER_THAN_OR_EQUAL = 15
    LESS_THAN_OR_EQUAL = 16

    #Boolean Expressions
    TRUE = 17
    FALSE = 18

    #String Operations
    STRING = 19

    #Variables
    IDENTIFIER = 20
    ASSIGN = 21

    PRINT = 22
    NEWLINE = 23

    FLOAT = 24

    IF = 25
    THEN = 26
    ELSE = 27
    ENDIF = 28

    WHILE = 29
    END_WHILE = 30

    INPUT = 31

    FUNCTION = 32
    END_FUNCTION = 33
    COMMA = 34

    LBRACE = 35
    RBRACE = 36

    RETURN = 37

    COMMENT = 38

    #Other
    EOF = 98
    UNKNOWN = 99


