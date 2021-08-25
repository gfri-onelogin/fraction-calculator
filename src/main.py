import argparse

from fractions import Fraction
from src.constants import DESCRIPTION
from src.parser import Parser
"""
This is the entry point into the application and handles command-line input
parsing.
"""
def main():
    parser = Parser()

    operands_and_operators = parser.operands_and_operators

    [print(item) for item in operands_and_operators]


if __name__ == '__main__':
    main()
