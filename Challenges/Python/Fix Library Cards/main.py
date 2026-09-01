#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Protocol
from collections.abc import Iterable, Iterator

class MediaCard(Protocol):
    def card_text(self) -> str: ...


@dataclass
class Article:
    title: str; author: str

    def card_text(self, _formatter: str="%s: %s by %s"):
        return _formatter % (type(self).__name__, self.title, self.author)


@dataclass
class Video:
    title: str; minutes: int

    def card_text(self, _formatter: str="%s: %s (%d min)"):
        return _formatter % (type(self).__name__, self.title, self.minutes)


def build_library_cards(items: Iterable[MediaCard]) -> list[str]:
    return [ card.card_text() for card in items ]


if __name__ == "__main__":
    items = (
        Article("Python Tips", "Mia"),
        Video("Debugging 101", 12),
    )

    cards = build_library_cards(items)
    print(cards)

    card: MediaCard = Video("The Matrix", 136)
    print(card, card.card_text())

    zipped: Iterator[tuple[str]] = zip(cards)
