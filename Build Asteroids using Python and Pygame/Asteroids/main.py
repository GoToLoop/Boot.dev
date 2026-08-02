#!/usr/bin/env python3

from re import S

from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BG

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

        Δ = clock.tick(60) / 1000 # milliseconds


def check_quit() -> bool: # True = QUIT(SDL 256)
    return any( event.type is pygame.QUIT for event in pygame.event.get() )


__name__ == "__main__" and main()  # pyright: ignore[reportUnusedExpression]
