from dataclasses import dataclass
import random
from src.core.actions import compute_dices_score
from src.core.models import Game, Player
from src.core.pikomino_types import DiceType


@dataclass(slots=True)
class ShitPlayer(Player):
    def _get_better_score(
        self, possible_values: DiceType, lauched_dices: DiceType
    ) -> int:
        scores_possibility: dict[int, int] = {}

        for value in possible_values:
            scores_possibility[value] = (
                len([dice for dice in lauched_dices if dice == value]) * value
            )

        better_choice = max(scores_possibility.items(), key=lambda x: x[1])

        return better_choice[0]

    def choose_dice_to_keep(
        self, lauched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        possible_values = set(
            [dice for dice in lauched_dices if dice not in taken_dice_values]
        )

        if len(possible_values) == 0:
            return None

        value_choosed = self._get_better_score(possible_values, lauched_dices)
        choosed_dices = [dice for dice in lauched_dices if dice == value_choosed]

        return choosed_dices

    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        actual_score = compute_dices_score(choose_result)
        other_players = game.other_players(self)
        other_players_last_tiles = [
            player.tiles[-1] for player in other_players if len(player.tiles) > 0
        ]

        if actual_score in other_players_last_tiles:
            return True
        if actual_score > 29:
            return True

        return False


@dataclass(slots=True)
class RandomPlayer(Player):
    def choose_dice_to_keep(
        self, launched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        possible_dices_to_keep = set(launched_dices) - set(taken_dice_values)

        if len(possible_dices_to_keep) == 0:
            return None

        choice = random.choice(list(possible_dices_to_keep))
        choosed_dices = [dice for dice in launched_dices if dice == choice]

        return choosed_dices

    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        actual_score = compute_dices_score(choose_result)
        if actual_score > 20:
            return random.choice([True, False])
        return True
