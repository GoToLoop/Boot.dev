Memo = dict[str, int]

def word_count_memo(doc: str, memos: Memo) -> tuple[int, Memo]:
    if doc not in (memos := memos.copy()): memos[doc] = word_count(doc)
    return memos[doc], memos


# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
