from collections.abc import Callable

def word_count_aggregator() -> Callable[[str], int]:
    count = 0

    def word_counter(doc: str) -> int:
        nonlocal count
        count += len(doc.split())
        return count

    return word_counter
