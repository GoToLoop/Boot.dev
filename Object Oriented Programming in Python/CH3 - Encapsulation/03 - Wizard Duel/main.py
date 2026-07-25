class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(wiz, fireball_damage: int):
        wiz.health -= fireball_damage - wiz.__stamina


    def drink_mana_potion(wiz, potion_mana: int):
        wiz.mana += potion_mana + wiz.__intelligence
