import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, num_balls_drawn):
        if len(self.contents) < num_balls_drawn:
            choices = self.contents
            self.contents = []
        else:
            choices = [
                self.contents.pop(random.randint(0, len(self.contents) - 1))
                for i in range(num_balls_drawn)
            ]

        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    def single_experiment(hat):
        result = hat.draw(num_balls_drawn)
        return {color: result.count(color) for color in set(result)}

    def is_success(result):
        for key, value in expected_balls.items():
            if key not in result or result[key] < value:
                return False
        return True

    success = 0
    for cycle in range(num_experiments):
        result = single_experiment(hat=copy.deepcopy(hat))
        success += 1 if is_success(result) else 0

    return success / num_experiments
