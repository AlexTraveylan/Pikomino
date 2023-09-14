import io
import random

from src.core.constants import DICE_DICT
from src.core.models import Game, Player
from src.core.pikomino_types import DiceType, TilePossibily, TileType


def lauch_n_dices(n: int) -> DiceType:
    """Lauch n dice and return the result as a list."""
    if n > 8:
        raise ValueError("cannot lauch more than 8 dice")

    return [random.randint(1, 6) for _ in range(n)]


def try_to_get_a_tile(
    remining_tiles: TileType, score: TilePossibily, players: list[Player]
) -> tuple[TilePossibily | None, str]:
    """Try to get a tile from the list of remining tiles."""

    if score in remining_tiles:
        remining_tiles.remove(score)
        return score, f"tile #{score} was taken from the game"

    for player in players:
        disponible_tile_for_player = player.tiles[-1] if len(player.tiles) > 0 else None
        if score == disponible_tile_for_player:
            player.tiles.remove(score)
            return score, f"title #{score} was taken from {player.name}"

    return None, f"failed to get tile for score {score}"


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


def fail_case(player: Player, game: Game) -> str:
    message = io.StringIO()

    if len(player.tiles) == 0:
        return "Nothing happened because the player has no tile\n"

    last_title_from_player = player.tiles[-1]
    game.tiles.append(last_title_from_player)
    message.write(f"{player.name} failed and lost tile #{last_title_from_player}\n")
    player.tiles.remove(last_title_from_player)

    last_title_from_game = game.tiles[-1]
    game.tiles.remove(last_title_from_game)
    message.write(
        f"{player.name} failed and tile #{last_title_from_game} was removed from the game\n"
    )

    return message.getvalue()
