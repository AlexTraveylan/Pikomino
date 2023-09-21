from src.core.actions import (
    compute_tiles_score,
    find_first_nearest_tile,
    lauch_n_dices,
    compute_dices_score,
    compute_tile_value,
    try_to_get_a_tile,
)
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
def test_compute_dices_score(dices, expected_score):
    result = compute_dices_score(dices)

    assert result == expected_score


@pytest.mark.parametrize(
    "remining_tiles, score, expected_result",
    [
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 21, 21),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 22, 22),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 23, 23),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 24, 24),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 25, 25),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 26, 26),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 27, 27),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 28, 28),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 29, 29),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 30, 30),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 31, 30),
    ],
)
def test_try_to_get_a_tile(remining_tiles, score, expected_result):
    result, message = try_to_get_a_tile(remining_tiles, score, [])

    assert result == expected_result
    assert score not in remining_tiles


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (21, 1),
        (22, 1),
        (23, 1),
        (24, 1),
        (25, 2),
        (26, 2),
        (27, 2),
        (28, 2),
        (29, 3),
        (30, 3),
        (31, 3),
        (32, 3),
        (33, 4),
        (34, 4),
        (35, 4),
        (36, 4),
    ],
)
def test_compute_title_value(test_input, expected):
    value_to_test = compute_tile_value(test_input)

    assert expected == value_to_test


@pytest.mark.parametrize(
    "tiles, expected_score",
    [
        ([21, 22, 23, 24], 4),
        ([21, 22, 23, 24, 25, 26, 27, 28], 12),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 18),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 21),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36], 25),
    ],
)
def test_compute_tile_value(tiles, expected_score):
    result = compute_tiles_score(tiles)

    assert result == expected_score


@pytest.mark.parametrize(
    "remining_tiles, score, expected_result",
    [
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 21, 21),
        ([21, 22, 23, 26, 27, 28, 29, 30], 25, 23),
        ([21, 22, 23, 32], 30, 23),
        ([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 31, 30),
    ],
)
def test_find_first_nearest_tile(remining_tiles, score, expected_result):
    result = find_first_nearest_tile(remining_tiles, score)

    assert result == expected_result
