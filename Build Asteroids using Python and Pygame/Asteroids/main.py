#!/usr/bin/env python3

import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

BG = pygame.colordict.THECOLORS["black"]

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


def event_loop() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: return True
    else: return False



__name__ == "__main__" and main()  # pyright: ignore[reportUnusedExpression]
