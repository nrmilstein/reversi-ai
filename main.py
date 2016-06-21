#!/usr/bin/env python3

import random
from GameState import GameState
from Node import Node
from Move import Move

DEPTH = 3

player_color = None
while player_color is None:
  try:
    player_color_str = input("Play as light or dark? ")[0].lower()
    if player_color_str == "b" or player_color_str == "d":
      player_color = 1
    elif player_color_str == "w" or player_color_str == "l":
      player_color = -1
    else:
      raise RuntimeError
  except (IndexError, RuntimeError):
    print('Invalid color, please enter "dark" or "light"')

game_state = GameState()
print(game_state)
print()

while True:
  if not game_state.get_possible_moves():
    print("Game over. Score: " + str(game_state.get_score()))
    break

  if game_state.to_move == player_color:
    player_move = None

    possible_moves = game_state.get_possible_moves()
    if len(possible_moves) == 1 and next(iter(possible_moves)).is_pass():
      player_move = next(iter(possible_moves))
      print("The only possible move is a pass.")
    else:
      while player_move is None:
        player_move = random.choice(list(possible_moves))
        print("Randomly selected move: " + player_move.get_algebraic_string())
        #player_move_str = input("Your move? ").lower()
        #try:
        #  potential_move = Move.from_algebraic_string(player_color, player_move_str)
        #except ValueError:
        #  print("Invalid move string.")
        #else:
        #  if potential_move not in possible_moves:
        #    print("That move is not possible.")
        #  else:
        #    player_move = potential_move

    game_state = game_state.move(player_move)
  else:
    node = Node(game_state)
    node.evaluate(DEPTH)
    print("Current value: " + str(node.value))
    best_move = node.best_child.prev_move
    print("Computer move: " + best_move.get_algebraic_string())
    game_state = node.best_child.game_state
  print(game_state)
  print("Current score: " + str(game_state.get_score()))
  print()



    




  


#node = Node(game_state)
#node.evaluate(5)
#
#probe_node = node
#for i in range(5):
#  probe_node = probe_node.best_child
#  print(probe_node.prev_move)
#  print(probe_node.game_state)
#  print("Game value: " + str(probe_node.game_state.get_value()))
#  print("Node value: " + str(probe_node.value))
#  print()
#
#
#
#
