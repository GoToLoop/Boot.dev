from typing import final, override
from collections.abc import Iterable

@final
class Influencer:
    def __init__(self, num_selfies: int, num_bio_links: int) -> None:
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    @override
    def __repr__(self) -> str:
        return f"({self.num_selfies}, {self.num_bio_links})"


# don't touch above this line

def vanity(influencer: Influencer) -> int:
    return 5 * influencer.num_bio_links + influencer.num_selfies

def vanity_sort(influencers: Iterable[Influencer]) -> list[Influencer]:
    return sorted(influencers, key=vanity)
