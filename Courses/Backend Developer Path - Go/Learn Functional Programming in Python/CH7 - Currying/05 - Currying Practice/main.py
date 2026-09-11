from collections.abc import Callable

ResizeFunc = Callable[[int, int], tuple[int, int]]
SetMinSizeFunc = Callable[..., ResizeFunc]

# Don't touch above this line

def new_resizer(max_width: int, max_height: int) -> SetMinSizeFunc:
    def with_min_size(min_width: int = 0, min_height: int = 0) -> ResizeFunc:
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resizer(width: int, height: int) -> tuple[int, int]:
            return (
                clamp(width, min_width, max_width),
                clamp(height, min_height, max_height)
            )

        return resizer

    return with_min_size


from typing import overload

@overload
def clamp(num: int, min_val: int, max_val: int) -> int: ...

@overload
def clamp(num: float, min_val: float, max_val: float) -> float: ...

def clamp(num: float, min_val: float, max_val: float) -> float:
    return max( min_val, min(num, max_val) )
