from abc import ABC, abstractmethod
from enum import auto
from strenum import StrEnum

from src.core.types import DiceType


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
    ...


class Player(ABC):
    """
    Implement this interface to create a player with a new strategy
    """

    def __init__(self, name: str):
        self.name = name
        self.tiles = []
        self.strategy_name = Strategy.RANDOM

    @abstractmethod
    def play_turn(self, game: Game) -> None:
        """
        define how the player will play his turn

        This set attributs of the player and the game
        """
        raise NotImplementedError

    @abstractmethod
    def choose_tile_to_keep(self, game: Game) -> tuple[DiceType, DiceType]:
        """
        define how the player will choose a tile to keep

        Return
        ------
        tuple[DiceType, DiceType]
            Dices chosen to keep, reminder dices
        """
        raise NotImplementedError

    @abstractmethod
    def decide_to_continue(self, choose_result: tuple[DiceType, DiceType]) -> bool:
        """
        define the strategy of the player to decide if he wants to continue

        Parameters
        ----------
        choose_result: tuple[DiceType, DiceType]
            Dices chosen to keep, reminder dices

        Return
        ------
        bool
            True if the player wants to continue, False otherwise
        """
        raise NotImplementedError
