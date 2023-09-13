from abc import ABC, abstractmethod
from enum import auto
from strenum import StrEnum

from src.core.constants import DES


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
    def choose_tile_to_keep(self, game: Game) -> tuple[DES, DES]:
        """
        define how the player will choose a tile to keep

        Return
        ------
        tuple[DES, DES]
            Dices chosen to keep, reminder dices
        """
        raise NotImplementedError

    @abstractmethod
    def decide_to_continue(self, choose_result: tuple[DES, DES]) -> bool:
        """
        define the strategy of the player to decide if he wants to continue

        Parameters
        ----------
        choose_result: tuple[DES, DES]
            Dices chosen to keep, reminder dices

        Return
        ------
        bool
            True if the player wants to continue, False otherwise
        """
        raise NotImplementedError
