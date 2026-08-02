from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, SHIP_COLOR

import pygame
from typing import override, Tuple

class Player(CircleShape):
    init_tri_vec = pygame.Vector2(0, 1)

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0 # angle in degrees


    def triangle(self) -> Tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        pos = self.position; rad = self.radius; rot = self.rotation; 

        forward = rad * self.init_tri_vec.rotate(rot)
        right = rad / 1.5 * self.init_tri_vec.rotate(rot + 90)

        a = pos + forward
        b = (pf := pos - forward) - right
        c = pf + right

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

        elif keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
