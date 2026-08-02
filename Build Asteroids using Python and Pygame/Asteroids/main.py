#!/usr/bin/env python3

from re import S

from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG

import pygame
from logger import log_state

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1)

    clock = pygame.time.Clock()
    Δ = 0.0

    while True:
        log_state()
        if check_quit(): return

        screen.fill(BG)
        player.update(Δ)
        player.draw(screen)

        pygame.display.flip()

        Δ = clock.tick(FPS) / 1000 # ms to seconds (±16 to ±0.0167)


def check_quit() -> bool: # True = QUIT(SDL 256)
    return bool(pygame.event.get(pygame.QUIT))


__name__ == "__main__" and main() # pyright: ignore[reportUnusedExpression]
