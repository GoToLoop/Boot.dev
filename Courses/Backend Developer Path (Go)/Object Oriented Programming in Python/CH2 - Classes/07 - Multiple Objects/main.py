#!/usr/bin/env python3

def main() -> None:
    aragorn = Brawler("Aragorn", 4, 4)
    gimli = Brawler("Gimli", 2, 7)
    legolas = Brawler("Legolas", 7, 7)
    frodo = Brawler("Frodo", 3, 2)

    fight(aragorn, gimli)
    fight(legolas, frodo)


class Brawler:
    def __init__(self, name: str, speed: int, strength: int) -> None:
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker: Brawler, defender: Brawler) -> None:
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
