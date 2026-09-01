class Human:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(archer, name: str, num_arrows: int):
        super().__init__(name)
        archer.__num_arrows = num_arrows


    def get_num_arrows(archer) -> int: return archer.__num_arrows

    def use_arrows(archer, num: int):
        if num > archer.get_num_arrows(): raise Exception("not enough arrows")
        archer.__num_arrows -= num



class Crossbowman(Archer):
    def __init__(crossbowman, name: str, num_arrows: int):
        super().__init__(name, num_arrows)


    def triple_shot(crossbowman, target: Human) -> str:
        crossbowman.use_arrows(3)
        return target.get_name() + " was shot by 3 crossbow bolts"
