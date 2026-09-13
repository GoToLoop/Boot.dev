from functools import lru_cache

INV = slice(None, None, -1) # [::-1]
OUTER = slice(1, -1)        # [1:-1]

@lru_cache
def is_palindrome(word: str) -> bool: return word == word[INV]

@lru_cache
def is_palindrome_regular(word: str) -> bool:
    def helper(left: int, right: int) -> bool:
        if left >= right: return True
        return helper(left+1, right-1) if word[left] == word[right] else False
    return helper(0, len(word) - 1)


@lru_cache
def is_palindrome_slowest(word: str) -> bool:
    if len(word) < 2: return True
    return is_palindrome_slowest(word[OUTER]) if word[0] == word[-1] else False
