from typing import Literal

Soldier = dict[Literal["damage", "attacks_per_second"], int]
Result = Literal["soldier 1 wins", "soldier 2 wins", "both soldiers die"]


def fight_soldiers(soldier_one: Soldier, soldier_two: Soldier) -> Result:
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)

    if soldier_one_dps > soldier_two_dps: return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps: return "soldier 2 wins"

    return "both soldiers die"


def get_soldier_dps(soldier: Soldier) -> int:
    return soldier['damage'] * soldier['attacks_per_second']
