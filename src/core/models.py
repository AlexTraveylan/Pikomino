from abc import ABC, abstractmethod
from dataclasses import dataclass, field
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


@dataclass(slots=True)
class BasePlayer(ABC):
    name: str
    tiles: TileType = field(default_factory=list)
    strategy_name = Strategy.RANDOM


@dataclass(slots=True)
class Game(ABC):
    players: list[BasePlayer]
    tiles: TileType = field(init=False)

    def __post_init__(self) -> None:
        """Check if the game is playable"""
        if len(self.players) < 2 or len(self.players) > 7:
            raise ValueError("PikominoGame is designed for 2 to 7 players")

        self.tiles = TILES.copy()

    def copy(self):
        """Return a copy of the game"""
        copied_class = self.__class__(self.players.copy())
        copied_class.tiles = self.tiles.copy()
        return copied_class

    @abstractmethod
    def _play_turn(self, player: BasePlayer):
        """Play a turn for a player"""
        raise NotImplementedError


@dataclass(slots=True)
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

    def copy(self):
        """Return a copy of the player"""
        copied_class = self.__class__(self.name)
        copied_class.tiles = self.tiles.copy()
        return copied_class
