from sneks.core.direction import Direction
from sneks.template.submission import Snek


class CustomSnek(Snek):
    def get_next_direction(self) -> Direction:
        return Direction.UP
