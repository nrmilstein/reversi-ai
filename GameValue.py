class GameValue:
  # value is for heuristic value, score is for a finished game.
  def __init__(self, value, score):
    self.value = value
    self.score = score

  def __cmp__(self, other):
    if self.score is None and other.score is None:
      return self.value - other.value
    if self.score is not None and other.score is not None:
      return self.score - other.score

    if self.score is not None and other.score is None:
      if self.score > 0:
        return self.score
      else
        return self.score - other.value

    if self.score is None and other.score is not None:
      if other.score > 0:
        return -1 * other.score
      else
        return self.value - other.score



