from dataclasses import dataclass
from typing import ClassVar, Final, override

@dataclass
class Siege:
    max_speed: int
    efficiency: int

    def get_trip_cost(self, distance: int, food_price: int) -> float:
        return distance / self.efficiency * food_price


    def get_cargo_volume(self) -> int: ...



@dataclass
class BatteringRam(Siege):
    load_weight: int
    bed_area: int

    LOAD_COST_FACTOR: ClassVar[Final] = 0.01

    @override
    def get_trip_cost(self, distance: int, food_price: int) -> float:
        return (
            super().get_trip_cost(distance, food_price)
            + self.LOAD_COST_FACTOR * self.load_weight
        )

    @override
    def get_cargo_volume(self) -> int: return self.bed_area << 1



@dataclass
class Catapult(Siege):
    cargo_volume: int

    @override
    def get_cargo_volume(self) -> int: return self.cargo_volume
