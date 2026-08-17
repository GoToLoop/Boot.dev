from typing import Sequence, Optional

def get_median_font_size(font_sizes: Sequence[int]) -> Optional[int]:
    idx = len( ordered := sorted(font_sizes) ) - 1 >> 1
    return ordered[idx] if ordered else None
