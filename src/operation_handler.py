from fractions import Fraction

from src.errors import BadMoveError
class OperationHandler:
    operators = {
        '+': Fraction.__add__,
        '-': Fraction.__sub__,
        '*': Fraction.__mul__,
        '/': Fraction.__truediv__
    }

    def __init__(self, operands_and_operators):
        self.operands_and_operators = operands_and_operators
        self.result = self.execute()

    def execute(self):
        try:
            return OperationHandler.operators[self.operands_and_operators[1]](self.operands_and_operators[0], self.operands_and_operators[2])
        except ZeroDivisionError:
            raise BadMoveError()

    def result_to_string(self):
        result = self.result

        # Handle improper fractions
        # There's some weird behavior in modulo and floor division where negative numbers
        # are returning unexpected results: -9 // 4 == -3 or -9 % 4 == 3. We're using abs
        # and a modifier to get around this.
        if (abs(result.numerator) > result.denominator and result.denominator != 1):
            negative_modifier = -1 if result.numerator < 0 else 1

            whole = str(negative_modifier * (abs(result.numerator) // result.denominator))
            fraction = str(Fraction(abs(result.numerator) % result.denominator, result.denominator))

            return f'{whole}_{fraction}'
        else:
            return str(result)
