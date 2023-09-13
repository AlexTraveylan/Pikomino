from src.core.actions import lauch_n_dices, compute_score
import pytest


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7, 8])
def test_lauch_n_dices(n):
    result = lauch_n_dices(n)

    assert isinstance(result, list)
    assert len(result) == n
    assert all([0 < dice < 7 for dice in result])


@pytest.mark.parametrize(
    "dices, expected_score",
    [
        ([2, 2, 2], 6),
        ([5, 5, 5], 15),
        ([6, 6, 6], 15),
        ([3, 3, 3, 1, 5, 5, 6, 6], 30),
        ([1, 1, 1, 1, 1, 5, 4, 4], 18),
        ([3, 2, 6, 5, 2, 2, 1, 1], 21),
    ],
)
def test_compute_score(dices, expected_score):
    result = compute_score(dices)

    assert result == expected_score
