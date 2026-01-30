from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    This snek moves in a circle by saving state
    between turns.
    """

    step: int = 0

    def get_next_action(self) -> Action:
        step_actions = {
            0: Action.RIGHT,
            1: Action.UP,
            2: Action.RIGHT,
            3: Action.DOWN,
            4: Action.RIGHT,
            5: Action.DOWN,
            6: Action.LEFT,
            7: Action.DOWN,
            8: Action.LEFT,
            9: Action.DOWN,
            10: Action.LEFT,
            11: Action.UP,
            12: Action.LEFT,
            13: Action.UP,
            14: Action.RIGHT,
            15: Action.UP,
        }

        self.step = (self.step + 1) % len(step_actions)

        return step_actions[self.step]
