import argparse
from fractions import Fraction
import re

from src.constants import DESCRIPTION

class Parser:
    operators = {
        '+': Fraction.__add__,
        '-': Fraction.__sub__,
        '*': Fraction.__mul__,
        '/': Fraction.__truediv__
    }
    whole_with_fraction_pattern = re.compile('(\-)?\d+_\d+/\d+')
    fraction_pattern = re.compile('(\-)?\d+(/\d+)?')

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)

        self.parser.add_argument('input', nargs='+', help='the input of the form "<operand> <operator> <operand>"')
        self.args = self._parse()

        self.operands_and_operators = map(self._parse_argument, self.args)

    def _parse(self):
        return vars(self.parser.parse_args())['input']

    def _validate_input(self, input):
        raise NotImplementedError('purple')

    def _parse_argument(self, string_input):
        if (string_input in Parser.operators.keys()):
            return string_input
        else:
            return self._parse_fraction(string_input)

    def _parse_fraction(self, string_input):
        if (Parser.whole_with_fraction_pattern.match(string_input)):
            return parse_whole_with_fraction(string_input)
        elif (Parser.fraction_pattern.match(string_input)):
            return Fraction(string_input)
        else:
            raise TypeError(f'{string_input} is not a valid fraction')

    def _parse_whole_with_fraction(self, string):
        split_string = string.split('_')
        if (split_string[0].startswith('-')):
            return Fraction(split_string[0]) - Fraction(split_string[1])
        else:
            return Fraction(split_string[0]) + Fraction(split_string[2])
