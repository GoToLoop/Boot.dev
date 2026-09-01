class Human:
    def sprint_right(h):
        h.__raise_if_cannot_sprint(); h.__use_sprint_stamina()
        h.move_right(); h.move_right()


    def sprint_left(h):
        h.__raise_if_cannot_sprint(); h.__use_sprint_stamina()
        h.move_left(); h.move_left()


    def sprint_up(h):
        h.__raise_if_cannot_sprint(); h.__use_sprint_stamina()
        h.move_up(); h.move_up()


    def sprint_down(h):
        h.__raise_if_cannot_sprint(); h.__use_sprint_stamina()
        h.move_down(); h.move_down()


    def __use_sprint_stamina(h): h.__stamina -= 1


    def __raise_if_cannot_sprint(h):
        if h.__stamina <= 0: raise Exception("not enough stamina to sprint")


    # don't touch below this line

    def move_right(self) -> None:
        self.__pos_x += self.__speed

    def move_left(self) -> None:
        self.__pos_x -= self.__speed

    def move_up(self) -> None:
        self.__pos_y += self.__speed

    def move_down(self) -> None:
        self.__pos_y -= self.__speed

    def get_position(self) -> tuple[int, int]:
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x: int, pos_y: int, speed: int, stamina: int) -> None:
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
