class Wizard:
    def __init__(wiz, name: str, stamina: int, intelligence: int):
        wiz.name = name

        wiz.__stamina = stamina
        wiz.__intelligence = intelligence

        wiz.mana = intelligence * 10
        wiz.health = stamina * 100


    def cast_fireball(wiz, target: "Wizard", cost: int, damage: int):
        if cost > wiz.mana: raise Exception(wiz.name + " cannot cast fireball")
        wiz.mana -= cost
        target.get_fireballed(damage)


    def is_alive(wiz) -> bool: return wiz.health > 0


    def get_fireballed(wiz, fireball_damage: int):
        wiz.health -= fireball_damage - wiz.__stamina


    def drink_mana_potion(wiz, potion_mana: int):
        wiz.mana += potion_mana + wiz.__intelligence
