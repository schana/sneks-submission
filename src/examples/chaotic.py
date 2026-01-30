import random

from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    This snek lets the chaos of the universe decide its fate.
    """

    def get_next_action(self) -> Action:
        return random.choice(list(Action))
