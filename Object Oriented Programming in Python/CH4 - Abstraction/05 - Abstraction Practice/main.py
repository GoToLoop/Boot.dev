from random import shuffle

Card = tuple[str, str]

class DeckOfCards:
    SUITS = "Hearts", "Diamonds", "Clubs", "Spades"

    RANKS = (
        "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King",
    )

    def __init__(self): self.__cards = self.create_deck()

    def create_deck(self) -> list[Card]:
        return [
            (rank, suit)
            for suit in DeckOfCards.SUITS
            for rank in DeckOfCards.RANKS
        ]


    def shuffle_deck(self): shuffle(self.__cards)

    def deal_card(self) -> Card | None:
        return self.__cards.pop() if self.__cards else None



    # don't touch below this line

    def __str__(self) -> str:
        return f"The deck has {len(self.__cards)} cards"
