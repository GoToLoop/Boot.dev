def find_longest_word(doc: str, longest: str = "") -> str:
    word, *rest = doc.split(' ', 1)
    if len(word) > len(longest): longest = word
    return find_longest_word(rest[0], longest) if rest else longest
