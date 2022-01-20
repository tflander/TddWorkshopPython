import pytest

from FizzBuzz import fizzbuzz


def test_one():
    assert fizzbuzz(1) == "1"


@pytest.mark.parametrize("test_input,expected", [
    (1, "1"),
    (2, "2"),
    (3, "fizz")
])
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected

