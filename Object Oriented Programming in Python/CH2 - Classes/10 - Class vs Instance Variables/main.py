#!/usr/bin/env python3

class Dragon:
    def __init__(dragon, element = "ice"): dragon.element = element

    def get_breath_damage(dragon) -> int:
        if dragon.element == "fire": return 300
        if dragon.element == "ice": return 150
        return 0



def main() -> None:
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()
