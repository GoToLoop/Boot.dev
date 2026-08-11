# pyright: reportCallInDefaultInitializer = hint

from circleshape import CircleShape
from shot import Shot

import pygame
from pygame import Surface, Vector2, draw, event, key
from typing import Final, Self, cast, override

from constants import (
    PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS,
    SHIP_WIDTH_RATIO, LINE_WIDTH, SHIP_COLOR, Signum, Tri
)

class Player(CircleShape):
    """Represents the player-controlled spaceship, handling input processing, 
    rotation, movement, bullet-shooting and rendering on screen.
    """

    unit_vector: Final = Vector2(0, 1) # starting by pointing downwards
    """Base vector pointing downwards (normalized length=1), used as the initial
    reference direction for rotation and movement calculations for the ship and
    for its projectiles' velocities.
    """

    quit_event: Final = event.Event(pygame.QUIT) # (SDL 256)
    """Preconstructed ``pygame.QUIT`` event posted to the event queue when 
    the player requests to exit the game via the ESC key.
    """

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


    @override
    def init(self,
        x: float, y: float,
        radius: float=0.0,
        vx: float=0.0, vy: float=0.0
    ) -> Self:
        self.rotation = self.shoot_cooldown = 0.0
        return super().init(x, y, radius, vx, vy)


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


    def move(self, Δ: float, _rotated: Vector2=Vector2()): # Δ: amount to move
        """Translate player position forward/backward along its facing vector"""
        _rotated.update(Player.unit_vector)
        _rotated.rotate_ip(self.rotation) # same dir as ship
        _rotated *= PLAYER_SPEED * Δ # scaled to distance traveled
        self.position += _rotated # updated player position


    def rotate(self, Δ: float): # amount to rotate (Δ in seconds)
        """Adjust the ship's rotation angle by the specified amount."""
        self.rotation += PLAYER_TURN_SPEED * Δ


    def triangle(
        self, _move: Vector2=Vector2(), _right: Vector2=Vector2()
    ) -> Tri:
        """Calculate and return the three vertices of the ship's triangular
        isosceles polygon based on its current position and rotation.
        """
        pos = self.position; rad = self.radius; rot = self.rotation

        _move.update(Player.unit_vector) # start by facing downwards
        _move.rotate_ip(rot) # facing same direction as ship now
        _move *= rad # scaled to ship's radius

        _right.update(Player.unit_vector) # start by facing downwards
        _right.rotate_ip(rot + 90) # clockwise sideways turn
        _right *= rad / SHIP_WIDTH_RATIO # scaled to a ratio of ship's radius

        a = pos + _move # a: front nose vertex
        b = (c := pos - _move) - _right # b: left-rear vertex; c: center-rear
        c += _right # c: right-rear vertex now

        return (a.x, a.y), (b.x, b.y), (c.x, c.y) # isosceles shape


    @override
    def draw(self, screen: Surface):
        """Render the player ship as a polygon outline onto the target
        display surface.
        """
        draw.polygon(screen, SHIP_COLOR, self.triangle(), LINE_WIDTH)


    @override
    def update(self, Δ: float): # amount to rotate or move (Δ in seconds)
        """Poll keyboard input to handle ship rotation, movement, shooting and
        enqueue a quit event during each frame.
        """
        self.shoot_cooldown -= Δ
        keys = key.get_pressed()

        rot = cast(Signum, (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (
            keys[pygame.K_a] or keys[pygame.K_LEFT])) # 1, 0, -1

        mov = cast(Signum, (keys[pygame.K_w] or keys[pygame.K_UP]) - (
            keys[pygame.K_s] or keys[pygame.K_DOWN])) # 1, 0, -1

        rot and self.rotate(rot * Δ) # turn right: +1; turn left: -1
        mov and self.move(mov * Δ) # forward: +1; backward: -1

        keys[pygame.K_SPACE] and self.can_shoot() and self.shoot()

        keys[pygame.K_ESCAPE] and event.post(Player.quit_event)
