import random

from src.core.constants import DICE_DICT
from src.core.types import DiceType, TilePossibily, TileType


def lauch_n_dices(n: int) -> DiceType:
    """Lauch n dice and return the result as a list."""
    if n > 8:
        raise ValueError("cannot lauch more than 8 dice")

    return [random.randint(1, 6) for _ in range(n)]


def try_to_get_a_tile(remining_tiles: TileType, score: int) -> TileType | None:
    """Try to get a tile from the list of remining tiles."""
    if score in remining_tiles:
        remining_tiles.remove(score)
        return score
    return None


def compute_dices_score(dices: DiceType):
    """Compute the score of a list of dices."""
    return sum([DICE_DICT.get(dice) for dice in dices])


def compute_tile_value(tile_index: TilePossibily) -> int:
    """
    Compute the value of a tite based on its index.
    """
    return (tile_index - 17) // 4


def compute_tiles_score(tiles: TileType) -> int:
    """
    Compute the score of a list of tiles.
    """
    return sum([compute_tile_value(tile) for tile in tiles])
