from src.core.actions import (
    compute_dices_score,
    compute_tiles_score,
    fail_case,
    lauch_n_dices,
    try_to_get_a_tile,
)
from src.core.pikomino_logging import LOGGER
from src.core.models import Game, Player
from src.core.constants import NUMBER_OF_DICE
from src.core.pikomino_types import DiceType


class PikominoGame(Game):
    def __init__(self, players: list[Player]) -> None:
        super().__init__(players)

    def run(self):
        """Run the game."""
        while not self._check_end_condition():
            for player in self.players:
                self._play_turn(player)
        for player_name, score in self._compute_players_score().items():
            LOGGER.info(f"{player_name} got {score} points")
        LOGGER.info("Game finished")
        winner_tuple_name_score = self._get_winner()
        LOGGER.info(f"The winner is {winner_tuple_name_score[0]} with {winner_tuple_name_score[1]} points")

    def _compute_players_score(self) -> dict[Player, int]:
        """Compute the score of each player."""
        return {player.name: compute_tiles_score(player.tiles) for player in self.players}

    def _get_winner(self) -> Player:
        """Get the winner of the game."""
        return max(self._compute_players_score().items(), key=lambda x: x[1])

    def _check_end_condition(self) -> bool:
        """Check if the game is finished."""
        return len(self.tiles) == 0

    def _play_turn(self, player: Player):
        """
        Play a turn for a player.

        Parameters
        ----------
        player: Player
            The player who will play the turn
        """
        choosen_dices: DiceType = []
        is_played_continue = True
        while is_played_continue:
            dices_lauched = lauch_n_dices(NUMBER_OF_DICE - len(choosen_dices))
            choose_result = player.choose_dice_to_keep(
                dices_lauched, choosen_dices, self
            )
            if choose_result is None:
                break
            choosen_dices = [*choosen_dices, *choose_result]

            is_played_continue = player.decide_to_continue(choosen_dices, self)

        if 6 not in choosen_dices or choose_result is None:
            message = fail_case(player, self)
            LOGGER.info(message)
            return

        score = compute_dices_score(choosen_dices)
        tile, message = try_to_get_a_tile(self.tiles, score, self.players)
        LOGGER.info(message)

        if tile is None:
            message = fail_case(player, self)
            LOGGER.info(message)
            return

        player.tiles.append(tile)
        LOGGER.info(f"{player.name} got tile {tile}\n")
