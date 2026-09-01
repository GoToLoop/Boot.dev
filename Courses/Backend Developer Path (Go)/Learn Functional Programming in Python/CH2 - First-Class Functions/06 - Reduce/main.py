from functools import reduce
from collections.abc import Sequence

def join(doc_so_far: str, sentence: str) -> str:
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences: Sequence[str], n: int) -> str:
    return reduce(join, sentences[:abs(n)]) + '.' if n and sentences else ""
