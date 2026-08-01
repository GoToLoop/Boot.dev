#!/usr/bin/env python3

import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BG

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        if event_loop(): return

        screen.fill(BG)

        pygame.display.flip()


def event_loop() -> bool: # True = QUIT(SDL 256)
    for event in pygame.event.get():
        if event.type is pygame.QUIT: return True
    return False


__name__ == "__main__" and main()  # pyright: ignore[reportUnusedExpression]
