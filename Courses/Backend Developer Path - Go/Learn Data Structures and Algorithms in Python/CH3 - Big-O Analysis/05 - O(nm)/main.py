from collections.abc import Collection

def get_avg_brand_followers(
    all_handles: Collection[Collection[str]], brand_name: str
) -> float:
    matches = 0

    for audiences in all_handles:
        for nickname in audiences:
            if brand_name in nickname: matches += 1

    return matches / len(all_handles)
