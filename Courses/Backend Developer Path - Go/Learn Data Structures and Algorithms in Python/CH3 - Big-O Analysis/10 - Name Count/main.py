from collections.abc import Iterable

def count_names(
    influencers_audiences: Iterable[Iterable[str]], target_name: str
) -> int:
    return sum(
        1
        for followers in influencers_audiences
        for user_name in followers
        if user_name == target_name
    )
