def exponential_growth(followers: int, factor: int, days: int) -> list[int]:
    return [ followers * factor ** day for day in range(days + 1) ]
