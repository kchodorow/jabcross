ORTHODOX = 0
SOUTHPAW = 1

class Stance(object):
  def __init__(self, stance: int = SOUTHPAW):
    self._stance = stance
    self.lead = 'right' if SOUTHPAW else 'left'
    self.power = 'left' if SOUTHPAW else 'right'
