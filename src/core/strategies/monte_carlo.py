from dataclasses import dataclass
from src.core.actions import (
    compute_dices_score,
    compute_tiles_score,
    fail_case,
    lauch_n_dices,
    try_to_get_a_tile,
)
from src.core.constants import NUMBER_OF_DICE

from src.core.models import Game, Player
from src.core.pikomino_types import DiceType


@dataclass(slots=True)
class MonteCarloPlayer(Player):
    simulations = 10

    def choose_dice_to_keep(
        self, launched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        best_score = -1
        best_choice = None

        possible_dices_to_keep = set(launched_dices) - set(taken_dice_values)

        for possibility in possible_dices_to_keep:
            total_score = 0
            for _ in range(self.simulations):
                simulation_game = game.copy()
                simulation_game._play_turn(self.copy())
                score = compute_tiles_score(simulation_game)
                total_score += score

            average_score = total_score / self.simulations
            if average_score > best_score:
                best_score = average_score
                best_choice = possibility

        return best_choice

    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        stop_score = 0
        continue_score = 0

        for _ in range(self.simulations):
            simulation_game = game.copy()
            simulation_player = self.copy()
            if 6 not in choose_result or choose_result is None:
                message = fail_case(simulation_player, simulation_game)
                stop_score += compute_tiles_score(simulation_game)
                continue

            score = compute_dices_score(choose_result)
            tile, message = try_to_get_a_tile(
                simulation_player.tiles, score, simulation_game.players
            )

            if tile is None:
                message = fail_case(simulation_player, simulation_game)
                stop_score += compute_tiles_score(simulation_game)
                continue

            simulation_player.tiles.append(tile)
            stop_score += compute_tiles_score(simulation_game)

        # Simulez le score si le joueur décide de continuer
        for _ in range(self.simulations):
            simulation_game = game.copy()
            simulation_player = self.copy()
            choosen_dices: DiceType = choose_result.copy()

            dices_lauched = lauch_n_dices(NUMBER_OF_DICE - len(choosen_dices))
            next_choose_result = simulation_player.choose_dice_to_keep(
                dices_lauched, choosen_dices, simulation_game
            )

            if next_choose_result is None:
                stop_score += compute_tiles_score(simulation_game)
                continue
            choosen_dices = [*choosen_dices, *next_choose_result]

            if 6 not in choose_result or choose_result is None:
                message = fail_case(simulation_player, simulation_game)
                stop_score += compute_tiles_score(simulation_game)
                continue

            score = compute_dices_score(choose_result)
            tile, message = try_to_get_a_tile(
                simulation_player.tiles, score, simulation_game.players
            )

            if tile is None:
                message = fail_case(simulation_player, simulation_game)
                stop_score += compute_tiles_score(simulation_game)
                continue

            simulation_player.tiles.append(tile)

            continue_score += compute_tiles_score(simulation_game)

        average_stop_score = stop_score / self.simulations
        average_continue_score = continue_score / self.simulations

        return average_continue_score > average_stop_score
