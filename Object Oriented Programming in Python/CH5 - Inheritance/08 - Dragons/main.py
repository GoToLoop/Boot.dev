from collections.abc import Iterable
from dataclasses import dataclass

@dataclass
class Unit:
    name: str; pos_x: int; pos_y: int

    def in_area(unit, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x1 <= unit.pos_x <= x2 and y1 <= unit.pos_y <= y2



@dataclass
class Dragon(Unit):
    __fire_range: int

    def breathe_fire(d, x: int, y: int, units: Iterable[Unit]) -> list[Unit]:
        radius = d.__fire_range

        x1 = x - radius; x2 = x + radius
        y1 = y - radius; y2 = y + radius

        return [ unit for unit in units if unit.in_area(x1, y1, x2, y2) ]
