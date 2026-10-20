def letter_combinations(digits: str) -> list[str]:
    if not digits: return []

    result = [""]

    for d in digits:
        if not ( letters := digit_to_letters.get(d) ):
            raise ValueError("invalid digit: " + d)

        result = [ combo + letter for combo in result for letter in letters ]

    return result


# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
