import copy
from Move import Move

class GameState:
  # Cell state – Empty: 0. Dark: 1. Light: -1
  # to_move – Dark: 1. Light: -1

  def __init__(self,
      board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0,-1, 1, 0, 0, 0],
        [0, 0, 0, 1,-1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
      ],
      to_move = 1,
      prev_pass = False):
    self.board = board
    self.to_move = to_move
    self.prev_pass = prev_pass

    self._possible_moves = None

  def get_value(self):
    possible_moves = self.get_possible_moves()
    if not possible_moves: # game over
      return GameValue(None, self.get_score())

    value_sum = 0
    for i, row in enumerate(self.board):
      for j, cell in enumerate(row):
        cell_value = cell
        if (i == 0 or i == 7) and (j == 0 or j == 7):
          cell_value *= 2
        value_sum += cell_value

    return GameValue(value_sum, None)

  def get_score(self):
    return sum(sum(cell for cell in row) for row in self.board)

  def get_possible_moves(self):
    if self._possible_moves is None:
      moves = set()
      for i, row in enumerate(self.board):
        for j, cell in enumerate(row):
          if cell == self.to_move:
            dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
                (0, -1), (-1, -1)]
            for dir in dirs:
              probe_i, probe_j = i, j
              try:
                while True:
                  last_color = self.board[probe_i][probe_j]
                  probe_i += dir[0]
                  probe_j += dir[1]
                  if probe_i < 0 or probe_j < 0:
                    raise IndexError
                  if self.board[probe_i][probe_j] == 0:
                    break
                if last_color == -self.to_move:
                  pass
                  moves.add(Move(self.to_move, (probe_i, probe_j)))
              except IndexError:
                pass
      if not moves and not self.prev_pass:
        # If there are no moves, and the previous player didn't pass, then
        # we pass.
        moves.add(Move(self.to_move, None))
      # Otherwise, there are no moves, and moves remains an empty set

      self._possible_moves = moves

    return self._possible_moves

  def move(self, move):
    new_board = copy.deepcopy(self.board)
    if move.location is not None:
      new_board[move.location[0]][move.location[1]] = move.color
      dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
          (0, -1), (-1, -1)]
      for dir in dirs:
        i, j = move.location
        try:
          while True:
            i += dir[0]
            j += dir[1]
            if i < 0 or j < 0:
              raise IndexError
            if new_board[i][j] != -move.color:
              break
          if new_board[i][j] == move.color:
            while True:
              i -= dir[0]
              j -= dir[1]
              if new_board[i][j] == move.color:
                break
              new_board[i][j] = move.color
        except IndexError:
          pass
      return GameState(new_board, -1 * self.to_move)
    else:
      return GameState(new_board, -1 * self.to_move, True)

  def __str__(self):
    result = ""
    for i, row in enumerate(self.board):
      for j, cell in enumerate(row):
        #result += " "
        if cell == 0:
          result += " "
        elif cell == 1:
          result += "\u25cb"
        elif cell == -1:
          result += "\u25cf"
        if j != len(row) - 1:
          result += "|"
      if i != len(self.board) - 1:
        result += "\n"

    return result
  
  def __repr__(self):
    return self.__str__()


