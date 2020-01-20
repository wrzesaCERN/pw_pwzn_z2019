import pytest

from tasks.tools.calculator import (
Calculator,
CalculatorError,
EmptyMemory,
NotNumberArgument,
WrongOperation,
)

@pytest.fixture()
def calc():
    return Calculator()


noproblems_test_tab = [
    ("+", 8, 8, 16),
    ("-", 8, 6, 2),
    ("*", 1, 0, 0),
    ("/", 9, 3, 3),
    ("+", 3, 2, 5),
    ("-", 2, 6, -4),
    ("*", 8, 8, 64),
    ("/", 100, 5, 20),
    ("+", 1, 9, 10),
    ("-", 2, 0, 2),
    ("*", 4, 6, 24),
    ("/", 7, 7, 1),
]


@pytest.mark.parametrize("operator,arg1,arg2,expected", noproblems_test_tab)
def test_calculator(operator, arg1, arg2, expected, calc):
    assert calc.run(operator, arg1, arg2) == expected


exceptions_test_tab = [
    ("/", 8, 0, CalculatorError),
    ("*", 8, None, EmptyMemory),
    ("+", 2, "napis", NotNumberArgument),
    (6, "-", 8, WrongOperation)
]


@pytest.mark.parametrize("operator, arg1, arg2, expected", exceptions_test_tab)
def test_afewexeptions(operator, arg1, arg2, expected, calc):
    try:
        calc.run(operator, arg1, arg2)
    except CalculatorError as exc:
        assert type(exc) == expected
    else:
        raise AssertionError


def test_emptyMemory_simpleissiue(calc):
    try:
        calc.in_memory()
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError


def test_emptyMemory_morecomplicatedissiue(calc):
    try:
        calc.run("-", 4, 2)
        calc.memorize()
        assert calc.memory == 2
        calc.clean_memory()
        calc.run("*", 6)
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError


def test_zeroDivision(calc):
    try:
        calc.run("/", 100, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
    else:
        raise AssertionError


def test_operation(calc):
    try:
        calc.run("^", 2, 2)
    except CalculatorError as exc:
        assert type(exc) == WrongOperation
    else:
        raise AssertionError


def test_notNumber(calc):
    try:
        calc.run("+", 3, "nieliczba")
    except CalculatorError as exc:
        assert type(exc) == NotNumberArgument
    else:
        raise AssertionError





