from circleshape import CircleShape
from shot import Shot

import pygame
from typing import Final, Literal, Tuple, cast, override

from constants import (
    PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS,
    SHIP_WIDTH_RATIO, LINE_WIDTH, SHIP_COLOR
)

Sign = Literal[1, 0, -1]

class Player(CircleShape):
    """Represents the player-controlled spaceship, handling input processing, 
    rotation, movement, bullet-shooting and rendering on screen.
    """

    unit_vector: Final = pygame.Vector2(0, 1) # starting by pointing downwards
    quit_event: Final = pygame.event.Event(pygame.QUIT)

    def __init__(self, x: float, y: float):
        """Initialize the player ship at the specified coordinates with 
        a standard radius and a rotation angle representing the offset 
        relative to the initial downward-facing origin vector.
        """
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation: float = 0.0
        """Offset on how many degrees to clockwise-rotate ``unit_vector``"""

        self.shoot_cooldown: float = 0.0
        """Countdown timer tracking the remaining time in seconds before the
        player is allowed to fire another shot.
        """


    def can_shoot(self) -> bool:
        """Check if the shoot cooldown has expired; if so, reset the cooldown 
        timer and return True, otherwise return False.
        """
        if self.shoot_cooldown > 0: return False
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        return True


    def shoot(self):
        """Create & launch a new shot projectile from the player's current
        position, oriented & scaled to move in the direction the ship is facing.
        """
        bullet = Shot(*self.position) # shot starts at same position as ship
        bullet.velocity.update(Player.unit_vector) # start vel facing downwards
        bullet.velocity.rotate_ip(self.rotation) # shot moves same dir as ship
        bullet.velocity *= PLAYER_SHOOT_SPEED  # scale shot to move much faster


    def move(self, Δ: float): # amount to move (Δ in seconds)
        """Translate player position forward/backward along its facing vector"""
        rotated = Player.unit_vector.rotate(self.rotation) # same dir as ship
        rotated *= PLAYER_SPEED * Δ # scaled to distance traveled
        self.position += rotated # updated player position


    def rotate(self, Δ: float): # amount to rotate (Δ in seconds)
        """Adjust the ship's rotation angle by the specified amount."""
        self.rotation += PLAYER_TURN_SPEED * Δ


    def triangle(self) -> Tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        """Calculate and return the three vertices of the ship's triangular
        isosceles polygon based on its current position and rotation.
        """
        pos = self.position; rad = self.radius; rot = self.rotation

        forward = Player.unit_vector.rotate(rot) # same direction as ship now
        forward *= rad # scaled to ship's radius
         
        right = Player.unit_vector.rotate(rot + 90) # clockwise sideways turn
        right *= rad / SHIP_WIDTH_RATIO # scaled to a ratio of the ship's radius

        a = pos + forward # a: front nose vertex
        b = (c := pos - forward) - right # b: left-rear vertex; c: center-rear
        c += right # c: right-rear vertex now

        return a, b, c # isosceles shape


    @override
    def draw(self, screen: pygame.SurfaceType):
        """Render the player ship as a polygon outline onto the target
        display surface.
        """
        pygame.draw.polygon(screen, SHIP_COLOR, self.triangle(), LINE_WIDTH)


    @override
    def update(self, Δ: float): # amount to rotate or move (Δ in seconds)
        """Poll keyboard input to handle ship rotation, movement, shooting and
        enqueue a quit event during each frame.
        """
        self.shoot_cooldown -= Δ
        keys = pygame.key.get_pressed()

        rot = cast(Sign, (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (
            keys[pygame.K_a] or keys[pygame.K_LEFT]))

        mov = cast(Sign, (keys[pygame.K_w] or keys[pygame.K_UP]) - (
            keys[pygame.K_s] or keys[pygame.K_DOWN]))

        rot and self.rotate(rot * Δ) # +1: turn right; -1: turn left
        mov and self.move(mov * Δ) # +1: forward; -1: backward

        keys[pygame.K_SPACE] and self.can_shoot() and self.shoot()

        keys[pygame.K_ESCAPE] and pygame.event.post(Player.quit_event)
