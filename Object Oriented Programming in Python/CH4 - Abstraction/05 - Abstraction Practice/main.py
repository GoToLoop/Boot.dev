from random import shuffle
from typing import cast, Literal

Rank = Literal[
    "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King",
]

Suit = Literal["Hearts", "Diamonds", "Clubs", "Spades"]

Card = tuple[Rank, Suit]

RANKS = (
    "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King",
)

SUITS = "Hearts", "Diamonds", "Clubs", "Spades"

DECK = *(
    cast(Card, (rank, suit))
    for suit in SUITS
    for rank in RANKS
),

class DeckOfCards:
    def __init__(self): self.__cards = [*DECK]

    def shuffle_deck(self): shuffle(self.__cards)

    def deal_card(self) -> Card | None:
        return self.__cards.pop() if self.__cards else None

    # don't touch below this line

    def __str__(self) -> str:
        return f"The deck has {len(self.__cards)} cards"
