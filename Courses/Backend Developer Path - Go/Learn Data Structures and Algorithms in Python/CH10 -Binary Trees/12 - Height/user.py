from random import seed, shuffle
from typing import override

USER_NAMES = (
    "Blake", "Ricky", "Shelley", "Dave", "George", "John", "James", "Mitch",
    "Williamson", "Burry", "Vennett", "Shipley", "Geller", "Rickert", "Carrell",
    "Baum", "Brownfield", "Lippmann", "Moses"
)

class User:
    def __init__(self, id: int):
        self.id: int = id
        self.user_name: str = USER_NAMES[id % len(USER_NAMES)] + f"#{id}"


    @override
    def __eq__(self, other: object):
        return isinstance(other, User) and self.id == other.id


    def __lt__(self, other: "User"): return self.id < other.id

    def __gt__(self, other: "User"): return self.id > other.id

    @override
    def __repr__(self): return ''.join(self.user_name)


def get_users(num: int):
    ids = list(range(3 * num))
    seed(1)
    shuffle(ids)
    return tuple( User(id) for id in ids[:num] )
