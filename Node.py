import math

class Node:
  def __init__(self, move = None, game_state = None, value = None,
      children = None):
    self.move = move
    self.game_state = game_state
    self.value = value
    self.children = set()

  def get_best_move(self, depth):
    game_state = self.game_state
    possible_moves = game_state.get_possible_moves()
    if not possible_moves:
      return ([self.move], None, game_state.get_score())
    if depth == 0:
      return ([self.move], game_state.get_value(), None)

    best_move = None
    best_value = (-math.inf, None)
    for move in possible_moves:
      node = Node(move, game_state.move(move))
      move_tuple = node.get_best_move(depth - 1)
      
      
      




    


  def is_leaf(self):
    return not self.children

  

