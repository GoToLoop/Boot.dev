class Wall:
    def __init__(wall, depth: int, height: int, width: int):
        wall.depth = depth; wall.height = height; wall.width = width
        wall.volume = depth * height * width
