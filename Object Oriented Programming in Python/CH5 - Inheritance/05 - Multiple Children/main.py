class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.__name = name
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def take_damage(self, damage: int) -> None:
        self.__health -= damage


# don't touch above this line


class Archer(Hero):
    ARROW_DAMAGE = 10

    def __init__(archer, name: str, health: int, num_arrows: int):
        super().__init__(name, health)
        archer.__num_arrows = num_arrows


    def shoot(archer, target: Hero):
        if archer.__num_arrows <= 0: raise Exception("not enough arrows")
        archer.__num_arrows -= 1
        target.take_damage(Archer.ARROW_DAMAGE)
