class Wall:
    armor: int = 10
    height: int = 5

    def get_cost(wall) -> int: return wall.armor * wall.height

    # don't touch below this line

    def fortify(self) -> None:
        self.armor *= 2
