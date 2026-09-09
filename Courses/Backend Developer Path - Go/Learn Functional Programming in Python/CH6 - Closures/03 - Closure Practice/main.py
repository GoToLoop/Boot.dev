from collections.abc import Callable, Collection

def new_collection(initial_docs: Collection[str]) -> Callable[[str], list[str]]:
    docs = list(initial_docs)
    return lambda doc: docs.append(doc) or docs
