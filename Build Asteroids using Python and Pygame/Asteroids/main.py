#!/usr/bin/env python3

from asteroidfield import AsteroidField
from player import Player
from headupdisplay import Hud

from logger import log_event, log_state
from platform import python_version

import pygame
from spritegroups import updatables, drawables, asteroids, shots

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG, LOGGING, MILLIS_TO_SECONDS
)

def main():
    welcome_msg()
    print(pygame.init(), "(started/failed) submodules")

    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("Asteroids")

    player = Player(SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1) # screen center
    AsteroidField() # spawns asteroids at a fixed time

    hud = Hud() # renders & tracks the current length of asteroids & shots

    clock = pygame.time.Clock()
    Δ = 0.0 # frame-to-frame transpired time in seconds

    while True:
        LOGGING and log_state()
        if check_quit(): break

        screen.fill(BG) # clear screen canvas using background color

        updatables.update(Δ)
        drawables.draw(screen)

        check_for_asteroid_hit()
        if check_death_by_collision(player): break

        hud.render_info(screen, clock)

        pygame.display.flip() # render screen canvas surface
        Δ = clock.tick(FPS) / MILLIS_TO_SECONDS # ms to seconds (~16 to ~0.0167)


def welcome_msg():
    print("\nStarting Asteroids with pygame version:", pygame.ver)
    print("Using SDL version:", pygame.SDL)
    print("On Python version", python_version())

    print("\nScreen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT, '\n')


def check_quit() -> bool: # True = QUIT(SDL 256)
    quit_requested = pygame.event.peek(pygame.QUIT) # checks for any QUIT events
    pygame.event.clear(pump = False) # erases any leftover enqueued events
    return quit_requested # True if any QUIT event was in the event's queue


def check_for_asteroid_hit():
    for asteroid in asteroids:
        for shot in shots:
            if shot.collides_with(asteroid):
                LOGGING and log_event("asteroid_shot")
                shot.kill()
                asteroid.split()
                break


def check_death_by_collision(ship: Player) -> bool: # True = Dead!
    for circle in asteroids:
        if circle.collides_with(ship):
            LOGGING and log_event("player_hit")
            print("\nGame over!")
            return True
    return False


__name__ == "__main__" and main()
