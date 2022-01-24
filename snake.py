import pygame
from utilities import GREEN, direction, Point


class Snake:
    '''Snake object'''
    body = [Point(x=10, y=10), Point(x=11, y=10)]
    color = GREEN
    velocity = direction.RIGHT
    has_eaten = False

    def get_head(self) -> None:
        '''Eat a fruit'''
        return self.body[-1]

    def move(self) -> None:
        '''Move the snake'''
        head = self.get_head()
        self.body.append(head.shift(self.velocity))
        if self.has_eaten:
            self.has_eaten = False
        else:
            self.body.pop(0)

    def eat(self) -> None:
        '''Eat a fruit'''
        self.has_eaten = True

    def draw_snake(self, surface: pygame.Surface) -> None:
        '''Draw the snake on the surface'''
        for segment in self.body:
            pygame.draw.rect(surface, self.color, segment.to_rect())
