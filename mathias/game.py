# from pikomino import *


# def test_roll_dice():
#     roll = roll_die()
#     assert roll in DICE.keys()

#     roll_5 = roll_dice(5)
#     assert len(roll_5) == 5
#     for die in roll_5:
#         assert die in DICE.keys()


# def stratgy(player, game):
#     pass


# def test_game():
#     player_0 = Player(strategy=basic_strategy)

#     game = PikominoGame([player_0])

#     while not game.over:
#         game.play_turn()

#         game.next_player()


# # Test dice rolling and selection
# def test_dice_rolling_and_selection():
#     game = PikominoGame()
#     player = game.players[0]
#     dice_roll = game.roll(player)
#     assert len(dice_roll) == 8
#     choice = dice_roll[0]
#     game.select_dice(player, choice, dice_roll)
#     assert choice in player['chosen_dice']
#     assert player['dice_left'] == 8 - dice_roll.count(choice)

# # Test tile acquisition and return
# def test_tile_acquisition_and_return():
#     game = PikominoGame()
#     player = game.players[0]
#     player['chosen_dice'] = [5, 5, 5, 5, "worm"]
#     game.finalize_turn(player)
#     assert 25 in player['tiles']
#     player['chosen_dice'] = [5, 5, 5, 5]
#     game.finalize_turn(player)
#     assert 36 not in game.CENTER_TILES
#     assert 25 in game.CENTER_TILES

# # Test end of game
# def test_end_of_game():
#     game = PikominoGame()
#     game.CENTER_TILES = []
#     assert game.game_over()
#     game.CENTER_TILES = [21]
#     player = game.players[0]
#     player["tiles"] = [22]
#     player['chosen_dice'] = [5,5,5,"worm",1]
#     game.finalize_turn(player)
#     assert game.game_over()

# test_dice_rolling_and_selection()
# test_tile_acquisition_and_return()
# test_end_of_game()
