from typing import Iterable

def destroy_walls(wall_health: Iterable[int]) -> list[int]:
    return [w for w in wall_health if w > 0]

from numbers import Complex

def destroy_walls_complex(wall_health: Iterable[Complex]) -> list[Complex]:
    return [w for w in wall_health if float(w.real) > 0]
