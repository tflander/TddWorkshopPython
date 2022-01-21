import pytest

from RomanCalculator import *


@pytest.mark.parametrize("left_operand, right_operand, expected", [
    ("I", "I", "II"),
    ("II", "I", "III")
])
def test_add(left_operand, right_operand, expected):
    assert roman_add(left_operand, right_operand) == expected

