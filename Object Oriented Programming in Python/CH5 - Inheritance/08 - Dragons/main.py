from collections.abc import Iterable
from dataclasses import dataclass, InitVar

@dataclass
class Unit:
    name: str; pos_x: int; pos_y: int

    def in_area(unit, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x1 <= unit.pos_x <= x2 and y1 <= unit.pos_y <= y2



@dataclass
class Dragon(Unit):
    fire_range: InitVar[int] # constructor's param only, not a field

    def __post_init__(self, fire_range: int):
        self.__fire_range = fire_range # store it as a private field instead


    def breathe_fire(d, x: int, y: int, units: Iterable[Unit]) -> list[Unit]:
        radius = d.__fire_range

        x1 = x - radius; x2 = x + radius
        y1 = y - radius; y2 = y + radius

        return [ unit for unit in units if unit.in_area(x1, y1, x2, y2) ]
