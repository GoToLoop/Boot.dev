from collections.abc import Iterable

class Unit:
    def __init__(unit, name: str, pos_x: int, pos_y: int):
        unit.name = name
        unit.pos_x = pos_x
        unit.pos_y = pos_y


    def in_area(unit, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x1 <= unit.pos_x <= x2 and y1 <= unit.pos_y <= y2



class Dragon(Unit):
    def __init__(dragon, name: str, pos_x: int, pos_y: int, fire_range: int):
        super().__init__(name, pos_x, pos_y)
        dragon.__fire_range = fire_range


    def breathe_fire(d, x: int, y: int, units: Iterable[Unit]) -> list[Unit]:
        radius = d.__fire_range

        x1 = x - radius; x2 = x + radius
        y1 = y - radius; y2 = y + radius

        return [ unit for unit in units if unit.in_area(x1, y1, x2, y2) ]
