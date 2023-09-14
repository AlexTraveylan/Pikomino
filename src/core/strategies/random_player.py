from dataclasses import dataclass
from src.core.actions import compute_dices_score
from src.core.models import Game, Player
from src.core.pikomino_types import DiceType


@dataclass(slots=True)
class RandomPlayer(Player):

    def choose_dice_to_keep(
        self, lauched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        possible_values = set(
            [dice for dice in lauched_dices if dice not in taken_dice_values]
        )

        if len(possible_values) == 0:
            return None

        value_choosed = max(possible_values)
        choosed_dices = [dice for dice in lauched_dices if dice == value_choosed]

        return choosed_dices

    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        actual_score = compute_dices_score(choose_result)
        if actual_score > 20:
            return False
        return True


@dataclass(slots=True)
class MonteCarloPlayer(Player):
    pass