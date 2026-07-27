class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length; self.width = width

    def get_area(self) -> int: return self.length * self.width

    def get_perimeter(self) -> int: return self.length + self.width << 1



class Square(Rectangle):
    def __init__(self, length: int): super().__init__(length, length)
