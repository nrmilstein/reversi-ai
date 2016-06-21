from GameValue import GameValue
from GameState import GameState

class Node:
  def __init__(self, game_state = None, prev_move = None):
    self.prev_move = prev_move
    self.game_state = game_state

    self.children = []
    self.value = None
    self.best_child = None

  def evaluate(self, depth, alpha = -GameValue.inf, beta = GameValue.inf):
    del self.children[:]
    game_state = self.game_state
    possible_moves = game_state.get_possible_moves()
    if depth == 0 or not possible_moves:
      self.value = game_state.get_value()
      return

    best_child = None
    best_value = -GameValue.inf
    for move in possible_moves:
      child_node = Node(game_state.move(move), move)
      self.children.append(child_node)
      child_node.evaluate(depth - 1, -beta, -alpha)
      
      child_node_value = -child_node.value
      if child_node_value > best_value:
        best_value = child_node_value
        best_child = child_node

      if child_node_value > alpha:
        alpha = child_node_value
      if alpha >= beta:
        break

    self.value = best_value
    self.best_child = best_child


#  def is_leaf(self):
#    return not self.children

