from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    def get_next_action(self) -> Action:
        return Action.UP
