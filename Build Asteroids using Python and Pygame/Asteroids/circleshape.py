import pygame
from abc import ABCMeta, abstractmethod
from typing import override

class CircleShape(pygame.sprite.Sprite, metaclass=ABCMeta):
    containers: tuple[pygame.sprite.Group, ...] # declared, but not created yet

    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"): super().__init__(*self.containers)
        else: super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.radius = radius


    @abstractmethod
    def draw(self, screen: pygame.Surface): ...

    @abstractmethod
    @override
    def update(self, Δ: float): ...
