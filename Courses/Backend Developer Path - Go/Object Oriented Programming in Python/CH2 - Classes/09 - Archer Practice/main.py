from dataclasses import dataclass

@dataclass
class Archer:
    name: str; health: int; num_arrows: int

    def take_hit(archer):
        archer.health -= 1
        if archer.health <= 0: raise Exception(archer.name + " is dead")


    def shoot(a, target: "Archer"):
        if a.num_arrows <= 0: raise Exception(a.name + " can't shoot")
        a.num_arrows -= 1

        print(a.name, "shoots", target.name)
        target.take_hit()


    # don't touch below this line

    def get_status(self) -> tuple[str, int, int]:
        return self.name, self.health, self.num_arrows

    def print_status(self) -> None:
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
