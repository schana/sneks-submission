"""Example Snek that tries to move up while avoiding obstacles."""

from sneks.engine.core.action import Action
from sneks.engine.core.direction import Direction
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    A Snek that prefers moving up but turns right to avoid obstacles.

    Demonstrates using the look() method to detect obstacles.
    """

    def get_next_action(self) -> Action:
        if self.look(Direction.UP) < 20:
            return Action.RIGHT
        return Action.UP
