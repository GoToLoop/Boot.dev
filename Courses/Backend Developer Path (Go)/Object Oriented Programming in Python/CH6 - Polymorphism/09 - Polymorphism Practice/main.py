from dataclasses import dataclass, field
from typing import Literal

Rank = Literal[
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
]

Suit = Literal["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = (
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
)

SUITS = "Clubs", "Diamonds", "Hearts", "Spades"

@dataclass(order=True, frozen=True)
class Card[R: Rank, S: Suit]:

    rank: R = field(compare=False)
    suit: S = field(compare=False)
    indices: tuple[int, int] = field(init=False)

    def __post_init__(self):
        object.__setattr__(
            self, "indices",
            ( RANKS.index(self.rank), SUITS.index(self.suit) )
        )

        print(repr(self))


    # don't touch below this line

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
