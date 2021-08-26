from fractions import Fraction
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
        return OperationHandler.operators[self.operands_and_operators[1]](self.operands_and_operators[0], self.operands_and_operators[2])

    def result_to_string(self):
        result = self.result
        if (result.numerator > result.denominator and result.denominator != 1):
            whole = str(result.numerator // result.denominator)
            fraction = str(Fraction(result.numerator % result.denominator, result.denominator))

            return f'{whole}_{fraction}'
        else:
            return str(result)
