from fractions import Fraction
import pytest

from src.errors import BadMoveError
from src.operation_handler import OperationHandler
from tests.fixtures import HANDLER_INPUTS

class TestOperationHandler:

    @pytest.mark.parametrize('input', HANDLER_INPUTS)
    def test_predefined_inputs(self, input):
        '''
        The inputs for this are found in the fixtures module and are of the form:
        {
            'input': [operand, operator, operand],
            'expected': result
        }
        '''

        handler = OperationHandler(input['input'])

        assert handler.result_to_string() == input['expected']

    def test_div_by_zero(self):
        input = [Fraction(1, 1), '/', Fraction(0, 1)]

        with pytest.raises(BadMoveError):
            OperationHandler(input)

