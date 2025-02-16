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


    #Other
    EOF = 98
    UNKNOWN = 99


