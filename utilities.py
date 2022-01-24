from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

import pygame


SQUARE_SIZE = 20
SCREEN_LATTICE_X = 40
SCREEN_LATTICE_Y = 30
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
WHITE = (255, 255, 255)


class direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


@dataclass
class Point:
    x: int
    y: int

    def shift(self, dir: direction) -> Point:
        vx, vy = dir.value
        return Point(self.x+vx, self.y+vy)

    def to_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x*SQUARE_SIZE, self.y*SQUARE_SIZE,
                           SQUARE_SIZE-2, SQUARE_SIZE-2)
