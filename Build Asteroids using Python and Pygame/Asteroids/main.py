#!/usr/bin/env python3

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

from typedgroup import TypedGroup
from traittypes import Drawable, Updatable, Spritable

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG, LOGGING

import pygame
from platform import python_version

if LOGGING: from logger import log_state

def main():
    welcome_msg()

    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    updatables: TypedGroup[Updatable] = TypedGroup()
    drawables: TypedGroup[Drawable] = TypedGroup()
    asteroids: TypedGroup[Spritable] = TypedGroup()

    Player.containers = updatables, drawables
    Player(SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1)

    Asteroid.containers = asteroids, updatables, drawables
    AsteroidField.container = updatables
    AsteroidField() # spawns asteroids

    clock = pygame.time.Clock()
    Δ = 0.0 # frame-to-frame transpired time in seconds

    while True:
        LOGGING and log_state() # pyright: ignore[reportPossiblyUnboundVariable]
        if check_quit(): break

        screen.fill(BG)
        updatables.update(Δ)
    
        for shape in drawables: shape.draw(screen)

        pygame.display.flip() # render screen canvas surface
        Δ = clock.tick(FPS) / 1000 # ms to seconds (~16 to ~0.0167)


def welcome_msg():
    print("\nStarting Asteroids with pygame version:", pygame.ver)
    print("Using SDL version:", pygame.SDL)
    print("On Python version", python_version())

    print("\nScreen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


def check_quit() -> bool: # True = QUIT(SDL 256)
    quit_requested = pygame.event.peek(pygame.QUIT)
    pygame.event.clear(pump = False)
    return quit_requested


__name__ == "__main__" and main()
