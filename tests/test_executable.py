import pytest
import os

from cli_test_helpers import ArgvContext
from unittest.mock import patch

from tests.fixtures import COMPLEX_VALUES_TO_TEST, OPERATORS, SIMPLE_VALUES_TO_TEST
class TestExecutable:
    '''
    These tests work by running the actual executable built by pyinstaller. Make sure
    you've actually built it and are in the project root directory. You can build the
    executable by running `./build.sh`. Take a peek if you're curious what it's doing.

    Note: We're not actually verifying that we're getting the correct output. That's
    something for another time. This just verifies that the program is exiting normally.

    Look into `subprocess.run` for these tests instead of `os.system`. `subprocess.run`
    returns a `CompletedProcess` object that contains the exit code and the output when
    `capture_output=True`.

    https://docs.python.org/3/library/subprocess.html#subprocess.run
    '''

    def test_entrypoint(self):
        exit_status = os.system('./fraction-calculator ~~help')

        assert exit_status == 0

    @pytest.mark.parametrize('val1', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('val2', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_simple_input(self, val1, val2, operator):
        exit_status = os.system(f'./fraction-calculator {val1} {operator} {val2}')

        assert exit_status == 0

    @pytest.mark.parametrize('value', COMPLEX_VALUES_TO_TEST)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_complex_input(self, value, operator):
        exit_status = os.system(f'./fraction-calculator {value} {operator} {value}')

        assert exit_status == 0
