import random
from typing import List
from absl import app

ORTHODOX = 0
SOUTHPAW = 1

LEAD = [1, 3, 5]
POWER = [2, 4, 6]

DIRECTIONS = ['forward', 'back', 'lead', 'power']
STEP_TYPE = ['step', 'half-step', 'shuffle']
DIRECTIONAL_DODGES = ['slip', 'weave']

# TODO
HEIGHT = ['low', 'high']
FOCUS = ['speed', 'power']
SPICY = ['dip', 'block', 'shovel']


class Stance(object):
  def __init__(self, stance: int = SOUTHPAW):
    self._stance = stance
    self.lead = 'right' if SOUTHPAW else 'left'
    self.power = 'left' if SOUTHPAW else 'right'


class Workout(object):
  def __init__(self, stance: Stance):
    self._stance = stance

  def GetRandomPunch(self) -> str:
    return str(random.randint(1, 7))

  def GetRandomFootwork(self) -> str:
    if random.random() < .6:
      direction = random.choice(DIRECTIONS)
      if direction == 'lead':
        direction = self._stance.lead
      elif direction == 'power':
        direction = self._stance.power
      step_type = random.choice(STEP_TYPE)
      return '%s %s' % (direction, step_type)
    direction = self._stance.lead if random.random() < .5 else self._stance.power
    return '%s %s' % (direction, random.choice(DIRECTIONAL_DODGES))

  def GetRandomMove(self) -> str:
    if random.random() < .4:
      return self.GetRandomPunch()
    return self.GetRandomFootwork()

  def GenerateWorkout(self) -> List[str]:
    return [self.GetRandomMove() for i in range(random.randint(2, 6))]


def main(argv):
  del argv
  stance = Stance()
  print('\n'.join(Workout(stance).GenerateWorkout()))


if __name__ == '__main__':
    app.run(main)