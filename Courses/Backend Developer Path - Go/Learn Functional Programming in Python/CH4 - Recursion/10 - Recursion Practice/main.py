type Nested = dict[int, dict[int, Nested]]

def count_nested_levels(docs: Nested, target_id: int, level: int = 1) -> int:
    for id in docs:
        if id == target_id: return level
        level_count = count_nested_levels(docs[id], target_id, level + 1)
        if level_count > 0: return level_count
    return -1
