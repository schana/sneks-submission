from sneks.core.cell import Cell
from sneks.core.direction import Direction
from sneks.template.submission import Snek


class CustomSnek(Snek):
    """
    This Snek moves towards the closest food without regard for obstacles
    """

    def get_next_direction(self) -> Direction:
        closest_food: Cell = self.get_closest_food()
        return self.get_direction_to_destination(destination=closest_food)
