class Rectangle:
    def overlaps(self, rect: "Rectangle") -> bool:
        return (
            self.get_left_x()   <= rect.get_right_x()  and
            self.get_right_x()  >= rect.get_left_x()   and
            self.get_top_y()    >= rect.get_bottom_y() and
            self.get_bottom_y() <= rect.get_top_y()
        )


    # don't touch below this line

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> int:
        return min(self.__x1, self.__x2)

    def get_right_x(self) -> int:
        return max(self.__x1, self.__x2)

    def get_top_y(self) -> int:
        return max(self.__y1, self.__y2)

    def get_bottom_y(self) -> int:
        return min(self.__y1, self.__y2)

    def __repr__(self) -> str:
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
