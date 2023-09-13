import pytest

from src.core.constants import compute_title_value


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
    value_to_test = compute_title_value(test_input)

    assert expected == value_to_test
