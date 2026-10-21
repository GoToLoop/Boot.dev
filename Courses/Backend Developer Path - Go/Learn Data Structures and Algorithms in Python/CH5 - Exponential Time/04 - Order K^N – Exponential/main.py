def letter_combinations(digits: str) -> list[str]:
    if not digits: return []

    combos = [""]

    for digit in digits:
        if not ( letters := digit_to_letters.get(digit) ):
            raise ValueError("invalid digit: " + digit)

        combos = [ combo + letter for combo in combos for letter in letters ]

    return combos


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
