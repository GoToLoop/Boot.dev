from dataclasses import dataclass

@dataclass
class Rectangle:
    length: int; width: int

    def get_area(self) -> int: return self.length * self.width

    def get_perimeter(self) -> int: return self.length + self.width << 1



class Square(Rectangle):
    def __init__(self, length: int): super().__init__(length, length)

    def __eq__(self, other: object):
        if not isinstance(other, Rectangle): return NotImplemented
        return self.length == other.length == other.width
