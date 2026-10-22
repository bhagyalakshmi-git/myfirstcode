import pytest

from calculator import (
    add,
    divide,
    modulo,
    multiply,
    power,
    square_root,
    subtract,
)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(10, 0)


def test_square_root():
    assert square_root(25) == 5


def test_square_root_of_negative_number():
    with pytest.raises(ValueError, match="square root of a negative number"):
        square_root(-1)
