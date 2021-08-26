from argparse import ArgumentParser
DESCRIPTION='''
Calculator that takes fractions as input and performs basic arithmetic operations (+, -, *, /) on them.

Fractions should be of the form <whole>_<numerator>/<denominator>.

Operands and operators should be separated by one or more spaces.
'''

DEFAULT_ARG_PARSER = ArgumentParser(description=DESCRIPTION, prefix_chars='~')
