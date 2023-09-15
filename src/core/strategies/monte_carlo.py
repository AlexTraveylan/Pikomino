from dataclasses import dataclass
from src.core.actions import (
    compute_dices_score,
    compute_tile_value,
    compute_tiles_score,
    fail_case,
    lauch_n_dices,
    try_to_get_a_tile,
)
from src.core.constants import NUMBER_OF_DICE

from src.core.models import Game, Player
from src.core.pikomino_types import DicePossibily, DiceType


@dataclass(slots=True)
class MonteCarloPlayer(Player):
    simulations = 100
    threshold = 0.7

    def choose_dice_to_keep(
        self, launched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        possible_dices_to_keep = set(launched_dices) - set(taken_dice_values)

        tree_result: dict[DicePossibily, int] = {}

        if len(possible_dices_to_keep) == 0:
            return None

        for possibility in possible_dices_to_keep:
            for _ in range(self.simulations):
                score = 0
                simulation_game = game.copy()
                simulation_current_player = None
                for player in simulation_game.players:
                    if player.name == self.name:
                        simulation_current_player = player
                        break

                new_dices = [dice for dice in launched_dices if dice == possibility]
                choosen_dices = [*taken_dice_values, *new_dices]

                score = compute_dices_score(choosen_dices)

                others_players = [
                    playr
                    for playr in simulation_game.players
                    if playr != simulation_current_player
                ]
                tile, _ = try_to_get_a_tile(
                    simulation_game.tiles, score, others_players
                )
                if tile is None:
                    score += -1
                else:
                    score += compute_tile_value(possibility)

                tree_result[possibility] = score

        beter_choice: DicePossibily = max(
            [(choice, possibility) for choice, possibility in tree_result.items()],
            key=lambda x: x[1],
        )[0]
        beter_dices = [dice for dice in launched_dices if dice == beter_choice]

        return beter_dices

    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        nb_none = 0
        nb_ok = 0

        # simulate if the player decide to stop
        for _ in range(self.simulations):
            simulation_game = game.copy()
            simulation_current_player: Player = None
            for player in simulation_game.players:
                if player.name == self.name:
                    simulation_current_player = player
                    break

            dices_lauched = lauch_n_dices(NUMBER_OF_DICE - len(choose_result))
            result = simulation_current_player.choose_dice_to_keep(
                dices_lauched, choose_result, simulation_game
            )
            if result is None:
                nb_none += 1
            else:
                nb_ok += 1

        average_stop_score = nb_none / self.simulations
        average_continue_score = nb_ok / self.simulations

        return average_continue_score > average_stop_score
