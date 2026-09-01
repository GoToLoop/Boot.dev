from dataclasses import dataclass, astuple

@dataclass(frozen=True)
class Dragon:
    name: str; color: str

    def __str__(dragon) -> str:
        return "I am %s, the %s dragon" % astuple(dragon)
