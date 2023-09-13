from src.core.actions import compute_dices_score
from src.core.models import Player
from src.core.types import ChooseResult, DiceType


class RandomPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def choose_dice_to_keep(
        self, lauched_dices: DiceType, taken_dice_values: DiceType
    ) -> ChooseResult | None:
        possible_values = set(
            [dice for dice in lauched_dices if dice not in taken_dice_values]
        )
        if len(possible_values) == 0:
            return None
        value_choosed = max(possible_values)
        choosed_dices = [dice for dice in lauched_dices if dice == value_choosed]
        reminder_dices = [dice for dice in lauched_dices if dice != value_choosed]

        return ChooseResult(choosed_dices, reminder_dices)

    def decide_to_continue(self, choose_result: DiceType) -> bool:
        actual_score = compute_dices_score(choose_result)
        if actual_score > 20:
            return False
        return True
