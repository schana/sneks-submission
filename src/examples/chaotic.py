"""Example Snek that moves randomly."""

import random

from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    A Snek that picks a random action each turn.

    Demonstrates the simplest possible implementation.
    """

    def get_next_action(self) -> Action:
        return random.choice(list(Action))
