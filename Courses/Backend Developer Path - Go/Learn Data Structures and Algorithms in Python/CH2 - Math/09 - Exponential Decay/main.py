def decayed_followers(
    initial_followers: int, fraction_lost_daily: float, days: int
) -> float:
    return initial_followers * (1 - fraction_lost_daily) ** days
