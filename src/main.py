from src.operation_handler import OperationHandler
from src.parser import Parser
"""
This is the entry point into the application and handles command-line input
parsing.
"""
def main():
    parser = Parser()

    operands_and_operators = parser.operands_and_operators

    handler = OperationHandler(operands_and_operators)

    print(handler.result_to_string())

if __name__ == '__main__':
    main()
