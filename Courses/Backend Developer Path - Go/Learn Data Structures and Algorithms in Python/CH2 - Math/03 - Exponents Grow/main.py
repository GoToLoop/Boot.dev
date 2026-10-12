from typing import cast

RATIO_BY_TYPE = { "fitness": 4, "cosmetic": 3 }

def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    month_ratio = cast(int, RATIO_BY_TYPE.get(influencer_type, 2) ** num_months)
    return month_ratio * follower_count
