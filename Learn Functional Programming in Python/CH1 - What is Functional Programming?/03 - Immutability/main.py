def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    return *documents, f"{len(documents)}. " + document
