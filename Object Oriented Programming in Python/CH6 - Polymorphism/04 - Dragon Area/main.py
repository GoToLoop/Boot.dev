class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line

from typing import override
from dataclasses import dataclass, field

@dataclass
class Dragon(Unit):
    name: str; pos_x: int; pos_y: int # center

    height: int; width: int; fire_range: int # dimensions

    __hit_box: "Rectangle" = field(init=False, repr=False)

    def __post_init__(self):
        cx = self.pos_x; cy = self.pos_y # center coords
        rad_x = self.width >> 1; rad_y = self.height >> 1 # radii

        self.__hit_box = Rectangle(
            cx - rad_x, cy - rad_y, # bottom-left coords (x1, y1)
            cx + rad_x, cy + rad_y  # top-right   coords (x2, y2)
        )

        print(self) # debug


    @override
    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return Rectangle(x1, y1, x2, y2).overlaps(self.__hit_box)


# don't touch below this line


class Rectangle:
    def overlaps(self, rect: "Rectangle") -> bool:
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> float:
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self) -> float:
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self) -> float:
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self) -> float:
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
