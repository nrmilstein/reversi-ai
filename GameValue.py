import math
from functools import total_ordering

@total_ordering
class GameValue:

  # value is for heuristic value, score is for a finished game.
  def __init__(self, value, score):
    self.value = value
    self.score = score

  def __neg__(self):
    return GameValue(
        -self.value if self.value is not None else None,
        -self.score if self.score is not None else None
    )

  def __gt__(self, other):
    if self.score is None and other.score is None:
      return self.value > other.value
    if self.score is not None and other.score is not None:
      return self.score > other.score

    if self.score is not None and other.score is None:
      if self.score > 0:
        return True
      else:
        return self.score > other.value

    if self.score is None and other.score is not None:
      if other.score > 0:
        return False
      else:
        return self.value > other.score

  def __repr__(self):
    return "GameValue(" + str(self.value) + ", " + str(self.score) + ")"

GameValue.inf = GameValue(math.inf, math.inf)
