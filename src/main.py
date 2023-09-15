from src.core.strategies.monte_carlo import MonteCarloPlayer
from src.core.strategies.random_player import RandomPlayer, ShitPlayer
from src.core.game import PikominoGame


def main():
    player_1 = MonteCarloPlayer("player_1")
    player_2 = RandomPlayer("player_2")
    game = PikominoGame([player_1, player_2])
    game.run()


if __name__ == "__main__":
    main()
