# import logging
# import random

# # import numpy as np
# from collections import OrderedDict
# from dataclasses import dataclass, field
# from typing import Callable

# logging.basicConfig(level=logging.INFO, format="%(message)s")


# logging.info("This is a log message.")

# # PlayerStrategy = Callable[Player, PikominoGame]

# DICE = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, "worm": 5}
# TILES = list(range(21, 37))
# NUMBER_OF_DICE = 8


# def roll_die():
#     return random.choice(list(DICE.keys()))


# def roll_dice(number):
#     return [roll_die() for _ in range(number)]


# @dataclass
# class Player:
#     strategy_name: str = "random"
#     tiles: list = field(default_factory=list)


# def test_strategy(*args, **kwargs):
#     chosen_dices = [5, 5, 5, "worm", 1]
#     steal_if_possible = True
#     return chosen_dices, steal_if_possible


# def random_strategy(
#     center_tiles: list,
#     current_player_tiles: list,
#     other_players_tiles: list[list],
# ):
#     raise NotImplementedError()
#     # Lancer le dés


# STRATEGIES = {
#     "test": test_strategy,
#     "random": random_strategy,
# }


# class PikominoGame:
#     def __init__(self, players: list[Player]):
#         self.center_tiles = TILES.copy()
#         self.current_player_idx = 0

#     @property
#     def over(self):
#         return not self.center_tiles


# class CantStealError(Exception):
#     pass

# def try_steal(player: Player, total: int, other_players: list[Player]):
#     has_stole = False
#     for other_player in other_players:
#         if other_player.tiles[-1] == total:
#             other_player.tiles.pop()
#             player.tiles.append(total)
#             has_stole = True
#     return player, other_players, has_stole


# def finalize_turn(player, other_players, game, chosen_dices, steal_if_possible):
#     total = sum([DICE[face] for face in chosen_dices])
#     worm_present = "worm" in chosen_dices
#     has_taken = False

#     if worm_present:
#         if steal_if_possible:
#             player, other_players, has_taken = try_steal(player, total, other_players)

#         if not has_taken:
#             player = try_take_center_tile(player, total)


#         total


# def play_turn(
#     player: Player,
#     other_players: list[Player],
#     game: PikominoGame,
# ):
#     player_strategy = STRATEGIES[player.strategy_name]

#     chosen_dices, steal_if_possible = player_strategy(
#         center_tiles=game.center_tiles,
#         current_player_tiles=player.tiles,
#         other_players_tiles=[other_player.tiles for other_player in other_players],
#     )

#     game = finalize_turn(player, other_players, game, chosen_dices, steal_if_possible)

#     return game

#     # self.players[self.current_player_idx] = current_player


# if __name__ == "__main__":
#     players = [Player("test"), Player("test")]
#     game = PikominoGame(players)
