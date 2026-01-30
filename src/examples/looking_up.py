from sneks.engine.core.action import Action
from sneks.engine.core.direction import Direction
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    """
    This snek wants to go up, unless it sees something
    in front of it. It only knows how to avoid obstacles
    by going right, and will work to go straight up when
    it doesn't see more obstacles.
    """

    def get_next_action(self) -> Action:
        if self.look(Direction.UP) < 20:
            return Action.RIGHT
        return Action.UP
