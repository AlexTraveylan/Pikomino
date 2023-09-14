from abc import ABC, abstractmethod
from src.core.constants import TILES
from enum import StrEnum, auto


from src.core.pikomino_types import DiceType, TileType


class Strategy(StrEnum):
    """
    Srategy.RANDOM is typed as Strategy
    Strategy.RANDOM.value is typed as str and equals 'RANDOM'
    """

    RANDOM = auto()
    NORMAL = auto()
    GRAPH = auto()
    AI = auto()


class BasePlayer(ABC):
    def __init__(self, name: str):
        self.name = name
        self.tiles: TileType = []
        self.strategy_name = Strategy.RANDOM


class Game(ABC):
    def __init__(self, players: list[BasePlayer]) -> None:
        if len(players) < 2 or len(players) > 7:
            raise ValueError("PikominoGame is designed for 2 to 7 players")
        self.tiles = TILES.copy()
        self.players = players


class Player(BasePlayer, ABC):
    """
    Implement this interface to create a player with a new strategy
    """

    @abstractmethod
    def choose_dice_to_keep(
        self, lauched_dices: DiceType, taken_dice_values: DiceType, game: Game
    ) -> DiceType | None:
        """
        define how the player will choose dices to keep

        Parameters
        ----------
        lauched_dices: DiceType
            Dices lauched by the player
        taken_dice_values: DiceType
            Dices already taken by the player
        game: Game
            Game instance for have all the information and take the best decision

        Return
        ------
        DiceType | None
            Dices chosen to keep. None if the player cannot choose any dice
        """
        raise NotImplementedError

    @abstractmethod
    def decide_to_continue(self, choose_result: DiceType, game: Game) -> bool:
        """
        define the strategy of the player to decide if he wants to continue

        Parameters
        ----------
        choose_result: ChooseResult
            Dices chosen to keep, reminder dices
        game: Game
            Game instance for have all the information and take the best decision

        Return
        ------
        bool
            True if the player wants to continue, False otherwise
        """
        raise NotImplementedError
