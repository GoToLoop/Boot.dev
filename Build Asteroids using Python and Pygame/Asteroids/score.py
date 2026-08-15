from dataclasses import dataclass
from typing import Final, Self

@dataclass(init=False)
class Score:
    """Tracks the player's current and high scores."""
    current_score: int = 0
    high_score: int = 0

    def init(self) -> Self:
        """Resets the current score to 0."""
        self.current_score = 0
        return self


    def update_high_score(self) -> Self:
        """Updates the high score if the current score is higher."""
        self.high_score = max(self.high_score, self.current_score)
        return self


score: Final = Score()
"""Active game score tracker variable."""
