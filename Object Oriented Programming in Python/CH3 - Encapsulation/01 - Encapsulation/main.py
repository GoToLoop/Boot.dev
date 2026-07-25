class Wizard:
    def __init__(wiz, name: str, stamina: int, intelligence: int):
        wiz.__stamina = stamina
        wiz.__intelligence = intelligence

        wiz.name = name
        wiz.health = 100 * stamina
        wiz.mana = 10 * intelligence
