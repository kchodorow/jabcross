from absl import app
from src.workout import sequence
from src.workout import stance


def main(argv):
  del argv
  s = stance.Stance()
  print('\n'.join(sequence.Sequence(s).GenerateWorkout()))


if __name__ == '__main__':
    app.run(main)