import random
from src.core.models import Game

from src.core.constants import DICE_DICT
from src.core.types import DiceType, TileType


def lauch_n_dices(n: int) -> DiceType:
    """Lauch n dice and return the result as a list."""
    if n > 8:
        raise ValueError("cannot lauch more than 8 dice")

    return [random.randint(1, 6) for _ in range(n)]


def try_to_get_a_tile(remining_tiles: TileType, dices: DiceType):
    pass


def compute_score(dices: DiceType):
    """Compute the score of a list of dices."""
    if any([dice > 6 for dice in dices]):
        raise ValueError("dice value cannot be greater than 6")

    return sum([DICE_DICT.get(dice) for dice in dices])
