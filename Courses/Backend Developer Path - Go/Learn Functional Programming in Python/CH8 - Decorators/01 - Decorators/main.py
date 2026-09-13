from collections.abc import Callable

def file_type_aggregator(
    func_to_decorate: Callable[[str, str], str],
) -> Callable[[str, str], tuple[str, dict[str, int]]]:
    # A map of file types to their counts
    counts: dict[str, int] = {}

    def wrapper(doc: str, file_type: str) -> tuple[str, dict[str, int]]:
        counts[file_type] = counts.get(file_type, 0) + 1
        result = func_to_decorate(doc, file_type)
        return result, counts

    return wrapper


# Don't touch above this line

@file_type_aggregator
def process_doc(doc: str, file_type: str) -> str:
    return f"Processing doc: '{doc}'. File Type: {file_type}"
