from src.core.models import Game, Player
from src.core.constants import TILES


class PikominoGame(Game):
    def __init__(self, players: list[Player]) -> None:
        if len(players) < 2 or len(players) > 7:
            raise ValueError("PikominoGame is designed for 2 to 7 players")

        self.players = players
        self.tiles = TILES.copy()

    def _check_end_condition(self) -> bool:
        """Check if the game is finished."""
        return len(self.tiles) == 0
