from abc import ABC, abstractmethod
from enum import auto
from strenum import StrEnum
from src.core.constants import TILES

from src.core.types import ChooseResult, DiceType, TileType


class Strategy(StrEnum):
    """
    Srategy.RANDOM is typed as Strategy
    Strategy.RANDOM.value is typed as str and equals 'RANDOM'
    """

    RANDOM = auto()
    NORMAL = auto()
    GRAPH = auto()
    AI = auto()


class Game:
    # Not really pep8 compliant but i like it.
    def __init__(self) -> None:
        self.tiles = TILES.copy()


class Player(ABC):
    """
    Implement this interface to create a player with a new strategy
    """

    def __init__(self, name: str):
        self.name = name
        self.tiles: TileType = []
        self.strategy_name = Strategy.RANDOM

    @abstractmethod
    def choose_dice_to_keep(
        self, lauched_dices: DiceType, taken_dice_values: DiceType
    ) -> ChooseResult | None:
        """
        define how the player will choose dices to keep

        Return
        ------
        ChooseResult | None
            Dices chosen to keep, reminder dices. None if the player cannot choose any dice
        """
        raise NotImplementedError

    @abstractmethod
    def decide_to_continue(self, choose_result: DiceType) -> bool:
        """
        define the strategy of the player to decide if he wants to continue

        Parameters
        ----------
        choose_result: ChooseResult
            Dices chosen to keep, reminder dices

        Return
        ------
        bool
            True if the player wants to continue, False otherwise
        """
        raise NotImplementedError
