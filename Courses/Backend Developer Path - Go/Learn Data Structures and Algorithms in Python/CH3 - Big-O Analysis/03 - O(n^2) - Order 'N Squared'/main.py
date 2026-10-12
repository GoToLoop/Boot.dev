from collections.abc import Iterable

def does_name_exist(
    first_names: Iterable[str], last_names: Iterable[str], full_name: str
) -> bool:
    for first in first_names:
        for last in last_names:
            if first + ' ' + last == full_name: return True
    return False
