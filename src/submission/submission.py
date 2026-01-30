"""
Submission template for the Sneks competition.

Modify the CustomSnek class to implement your Snek's behavior.
See https://www.sneks.dev/docs for API documentation.
"""

from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    Your custom Snek implementation.

    Override get_next_action() to control your Snek's movement each turn.
    You can add instance variables to track state between turns.

    See https://www.sneks.dev/docs for available methods and helpers.
    """

    def get_next_action(self) -> Action:
        """
        Determine the Snek's next action.

        Returns:
            Action: One of Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT, or Action.MAINTAIN
        """
        return Action.UP
