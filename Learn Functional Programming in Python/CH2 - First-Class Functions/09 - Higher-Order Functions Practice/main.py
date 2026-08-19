from collections.abc import Iterable
from itertools import filterfalse

def restore_documents(originals: Iterable[str], backups: Iterable[str]
) -> set[str]:
    return set(filterfalse(str.isdigit, map(str.upper, (*originals, *backups))))
