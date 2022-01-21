import pytest

from TennisEasy import TennisGameEasy
from TennisScoring.TennisTestData import test_data


@pytest.mark.parametrize("p1_score, p2_score, expected_score", test_data)
def test_tennis_score(p1_score, p2_score, expected_score):
    game = TennisGameEasy("player1", "player2")

    score_points(game, "player1", p1_score)
    score_points(game, "player2", p2_score)

    actual_score = game.get_score()
    assert expected_score == actual_score


def score_points(game: TennisGameEasy, player_name: str, points: int):
    for i in range(points):
        game.WonPoint(player_name)
