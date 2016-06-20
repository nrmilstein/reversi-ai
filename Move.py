class Move:
  # If location is None, then the move is a "pass".
  def __init__(self, color, location):
    self.color = color
    self.location = location
  
  def __eq__(self, other):
    return self.color == other.color and self.location == other.location

  def __hash__(self):
    return hash((self.color, self.location))
  
  def __repr__(self):
    return "Move(" + str(self.color) + ", " + str(self.location) + ")"


