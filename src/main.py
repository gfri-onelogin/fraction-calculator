import argparse

from src.constants import DESCRIPTION
from src.errors import BadMoveError, InvalidFractionError
from src.operation_handler import OperationHandler
from src.parser import Parser

def main():
    '''
    This is the entry point into the application and handles command-line input
    parsing.
    '''
    parser = Parser()

    operands_and_operators = parser.operands_and_operators

    try:
        handler = OperationHandler(operands_and_operators)

        print(handler.result_to_string())
    except (BadMoveError, InvalidFractionError) as error:
        print(error.message)

if __name__ == '__main__':
    main()
