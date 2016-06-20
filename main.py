#!/usr/bin/env python3

from GameState import GameState
import random

game_state = GameState()
print(game_state)

for i in range(100):
  moves = game_state.get_possible_moves()
  print(moves)
  next_move = random.choice(list(moves))
  print("Chosen move: " + str(next_move))
  game_state = game_state.move(next_move)
  print(game_state)
  print()

