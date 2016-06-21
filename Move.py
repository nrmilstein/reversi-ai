class Move:
  # If location is None, then the move is a "pass".
  def __init__(self, color, location):
    self.color = color
    self.location = location
    if location is not None:
      self.row = location[0]
      self.col = location[1]

  @classmethod
  def from_algebraic_string(cls, color, loc):
    try:
      row = int(loc[1]) - 1
      if row > 7:
        raise ValueError
      col = "abcdefgh".index(loc[0])
      return cls(color, (row, col))
    except ValueError:
      raise ValueError("invalid algebraic string") from None

  def is_pass(self):
    return self.location is None
  
  def __eq__(self, other):
    return self.color == other.color and self.location == other.location

  def __hash__(self):
    return hash((self.color, self.location))
  
  def __repr__(self):
    return "Move(" + str(self.color) + ", " + str(self.location) + ")"

  def get_algebraic_string(self):
    if self.is_pass():
      return "Pass"
    return "abcdefgh"[self.col] + str(self.row + 1)


