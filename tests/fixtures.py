from fractions import Fraction

SIMPLE_VALUES_TO_TEST = [ '0', '-0', '1', '-1', '2', '-2', '1/2', '-1/2', '9/16', '-9/16', '13/5', '-13/5', '8/4', '-8/4' ]

INVALID_FRACTIONS = [ '1/_2', '_1', 'purple' ]

COMPLEX_VALUES_TO_TEST = [ '1_1/2', '-1_1/2', '1_7/2', '-1_7/2' ]

COMPOUND_FRACTION_PAIRS = [
    { 'arg': '1_1/2', 'expected': Fraction(3, 2) },
    { 'arg': '-1_1/2', 'expected': Fraction(-3, 2) },
    { 'arg': '9_16/8', 'expected': Fraction(11, 1) },
    { 'arg': '-9_16/8', 'expected': Fraction(-11, 1) },
    { 'arg': '1_19/6', 'expected': Fraction(25, 6) },
    { 'arg': '-1_19/6', 'expected': Fraction(-25, 6) }
]

OPERATORS = [ '+', '-', '*', '/' ]
