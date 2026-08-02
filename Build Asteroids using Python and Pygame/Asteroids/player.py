from circleshape import CircleShape

from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, WIDTH_RATIO, LINE_WIDTH, SHIP_COLOR
)

import pygame
from typing import Final, Tuple, override

class Player(CircleShape):

    starting_direction: Final = pygame.Vector2(0, 1) # pointing downwards
    quit_event: Final = pygame.event.Event(pygame.QUIT)

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0 # angle in degrees


    def triangle(self) -> Tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        pos = self.position; rad = self.radius; rot = self.rotation

        forward = rad * Player.starting_direction.rotate(rot)
        right = rad / WIDTH_RATIO * Player.starting_direction.rotate(rot + 90)

        a = pos + forward # front nose
        b = (rear := pos - forward) - right # left-rear base
        c = rear + right # right-rear base

        return a, b, c


    def rotate(self, Δ: float): self.rotation += Δ * PLAYER_TURN_SPEED

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, SHIP_COLOR, self.triangle(), LINE_WIDTH)


    @override
    def update(self, Δ: float): # amount to rotate (Δ in seconds)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.rotate(-Δ)

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.rotate(Δ)

        elif keys[pygame.K_ESCAPE]: pygame.event.post(Player.quit_event)
