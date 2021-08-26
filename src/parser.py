from fractions import Fraction
import re

from src.constants import DEFAULT_ARG_PARSER, DESCRIPTION
from src.errors import BadMoveError, InvalidFractionError

class Parser:
    '''
    This class handles taking in arguments and ensuring they're valid, then
    converting them to Fractions that can be operated on by the OperationHandler
    '''
    operators = {
        '+': Fraction.__add__,
        '-': Fraction.__sub__,
        '*': Fraction.__mul__,
        '/': Fraction.__truediv__
    }
    # Examples:
    # * 1_1/2
    # * -1_1/2
    whole_with_fraction_pattern = re.compile('(-)?\\d+_\\d+/\\d+$')
    # Examples:
    # * 1
    # * -1
    # * 9/2
    # * -9/2
    fraction_pattern = re.compile('(-)?\\d+(/\\d+)?$')

    def __init__(self, argparser=DEFAULT_ARG_PARSER):
        self.parser = argparser

        self.parser.add_argument('input', nargs='+', help='the input of the form "<operand> <operator> <operand>"')

        self.args = self._parse()

        self.operands_and_operators = list(map(self._parse_argument, self.args))

    def _parse(self):
        args = vars(self.parser.parse_args())['input']

        # This indicates that the user has passed in a quoted string.
        if (len(args) == 1):
            return args[0].split()
        elif (len(args) != 3 and not self._is_globbed(args)):
            raise ValueError(f'{args} is not of the form <operand> <operator> <operand>.');
        elif (self._is_globbed(args)):
            return self._glob_corrected_args(args)
        else:
            return args

    def _parse_argument(self, string_input):
        if (string_input in Parser.operators.keys()):
            return string_input
        else:
            try:
                return self._parse_fraction(string_input)
            except ZeroDivisionError:
                raise BadMoveError()

    def _parse_fraction(self, string_input):
        if (Parser.whole_with_fraction_pattern.match(string_input)):
            return self._parse_whole_with_fraction(string_input)
        elif (Parser.fraction_pattern.match(string_input)):
            return Fraction(string_input)
        else:
            raise InvalidFractionError(string_input)

    def _parse_whole_with_fraction(self, string):
        split_string = string.split('_')
        if (split_string[0].startswith('-')):
            return Fraction(split_string[0]) - Fraction(split_string[1])
        else:
            return Fraction(split_string[0]) + Fraction(split_string[1])

    def _is_globbed(self, args):
        '''
        This and _glob_corrected_args only exist because shells such as zsh and bash
        expand the `*` operator to the files in the current directory. This checks
        if that is the case by looking for the README.
        '''
        try:
            return True if args.index('README.md') else False
        except ValueError:
            return False

    def _glob_corrected_args(self, args):
        '''
        Huge assumption that we'll only be using this with args that are verified
        to be globbed (_is_globbed).
        '''
        return [ args[0], '*', args[-1] ]
