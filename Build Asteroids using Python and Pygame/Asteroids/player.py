from circleshape import CircleShape

from constants import (
    PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED,
    WIDTH_RATIO, LINE_WIDTH, SHIP_COLOR
)

import pygame
from typing import Final, Tuple, override

class Player(CircleShape):

    unit_vector: Final = pygame.Vector2(0, 1) # starting by pointing downwards
    quit_event: Final = pygame.event.Event(pygame.QUIT)

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0 # angle in degrees in relation to `unit_vector`


    def triangle(self) -> Tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        pos = self.position; rad = self.radius; rot = self.rotation

        forward = Player.unit_vector.rotate(rot) # same direction as ship now
        forward *= rad # scaled to ship's radius

        right = Player.unit_vector.rotate(rot + 90) # clockwise sideways turn
        right *= rad / WIDTH_RATIO # scaled to a ratio of the ship's radius

        a = pos + forward # front nose vertex
        b = (c := pos - forward) - right # left-rear base vertex
        c += right # right-rear base vertex

        return a, b, c # isosceles shape


    def move(self, Δ: float): # amount to move (Δ in seconds)
        rotated = Player.unit_vector.rotate(self.rotation) # same dir as ship
        rotated *= PLAYER_SPEED * Δ # scaled to distance traveled
        self.position += rotated # updated player position


    def rotate(self, Δ: float): self.rotation += PLAYER_TURN_SPEED * Δ

    @override
    def draw(self, screen: pygame.SurfaceType):
        pygame.draw.polygon(screen, SHIP_COLOR, self.triangle(), LINE_WIDTH)


    @override
    def update(self, Δ: float): # amount to rotate or move (Δ in seconds)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.rotate(-Δ)

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.rotate(Δ)

        elif keys[pygame.K_w] or keys[pygame.K_UP]: self.move(Δ)

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]: self.move(-Δ)

        elif keys[pygame.K_ESCAPE]: pygame.event.post(Player.quit_event)
