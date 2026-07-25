from dataclasses import dataclass

@dataclass
class Human:
    __pos_x: int; __pos_y: int; __speed: int

    def move_right(human): human.__pos_x += human.__speed
    def move_left(human): human.__pos_x -= human.__speed
    def move_up(human): human.__pos_y += human.__speed
    def move_down(human): human.__pos_y -= human.__speed

    def get_position(h) -> tuple[int, int]: return h.__pos_x, h.__pos_y
