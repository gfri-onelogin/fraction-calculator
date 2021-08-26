class BadMoveError(ZeroDivisionError):
    def __init__(self):
        self.message = 'While creating the universe was widely regarded as a bad move, dividing by zero would destroy it.'

class InvalidFractionError(Exception):
    def __init__(self, fraction_input):
        self.message = f'"{fraction_input}" is not a valid fraction'
