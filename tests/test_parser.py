from argparse import ArgumentParser, Namespace
from fractions import Fraction
import pytest
from unittest.mock import MagicMock

from src.parser import Parser

from tests.fixtures import COMPOUND_FRACTION_PAIRS, INVALID_FRACTIONS, OPERATORS, SIMPLE_VALUES_TO_TEST

class TestParser:
    @pytest.mark.parametrize('val1', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('val2', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_simple_input(self, val1, val2, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=[val1, operator, val2])
        argparser_mock.parse_args = MagicMock(return_value=args)

        parser = Parser(argparser_mock)

        assert parser.operands_and_operators == [Fraction(val1), operator, Fraction(val2)]

    @pytest.mark.parametrize('compound_value', COMPOUND_FRACTION_PAIRS)
    @pytest.mark.parametrize('simple_value', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_compound_with_simple_input(self, compound_value, simple_value, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=[compound_value['arg'], operator, simple_value])
        argparser_mock.parse_args = MagicMock(return_value=args)

        parser = Parser(argparser_mock)

        assert parser.operands_and_operators == [compound_value['expected'], operator, Fraction(simple_value)]


    @pytest.mark.parametrize('simple_value', SIMPLE_VALUES_TO_TEST)
    @pytest.mark.parametrize('compound_value', COMPOUND_FRACTION_PAIRS)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_simple_with_compound_input(self, simple_value, compound_value, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=[simple_value, operator, compound_value['arg']])
        argparser_mock.parse_args = MagicMock(return_value=args)

        parser = Parser(argparser_mock)

        assert parser.operands_and_operators == [Fraction(simple_value), operator, compound_value['expected']]

    @pytest.mark.parametrize('val1', COMPOUND_FRACTION_PAIRS)
    @pytest.mark.parametrize('val2', COMPOUND_FRACTION_PAIRS)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_compound_with_compound_input(self, val1, val2, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=[val1['arg'], operator, val2['arg']])
        argparser_mock.parse_args = MagicMock(return_value=args)

        parser = Parser(argparser_mock)

        assert parser.operands_and_operators == [val1['expected'], operator, val2['expected']]

    @pytest.mark.parametrize('operator', OPERATORS)
    def test_div_by_zero_input(self, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=['1/0', operator, '1'])
        argparser_mock.parse_args = MagicMock(return_value=args)

        with pytest.raises(ZeroDivisionError):
            Parser(argparser_mock)

    @pytest.mark.parametrize('input', INVALID_FRACTIONS)
    @pytest.mark.parametrize('operator', OPERATORS)
    def test_with_invalid_fraction_input(self, input, operator):
        argparser_mock = MagicMock(ArgumentParser)
        args = Namespace(input=[input, operator, '1'])
        argparser_mock.parse_args = MagicMock(return_value=args)

        with pytest.raises(TypeError):
            Parser(argparser_mock)

