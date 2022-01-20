import pytest

from RockPaperScissors import rock_paper_scissors


@pytest.mark.parametrize("gesture1, gesture2, expected", [
    ("rock", "scissors", "rock beats scissors"),
    ("scissors", "paper", "scissors beats paper"),
    ("paper", "rock", "paper beats rock")
])
def test_rock_paper_scissors(gesture1, gesture2, expected):
    assert rock_paper_scissors(gesture1, gesture2) == expected

