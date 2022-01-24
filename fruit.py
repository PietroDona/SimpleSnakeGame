import pygame
import random
from utilities import SCREEN_LATTICE_X, SCREEN_LATTICE_Y, RED, Point


class Fruit:
    color = RED
    position = Point(0, 0)
    points = 10

    def random_position(self) -> None:
        newx = random.randrange(0, SCREEN_LATTICE_X)
        newy = random.randrange(0, SCREEN_LATTICE_Y)
        self.position = Point(newx, newy)

    def get_position(self) -> Point:
        return self.position

    def draw_fruit(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.position.to_rect())
