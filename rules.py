from abc import ABC, abstractmethod
from game import Game
from snake import Snake
from fruit import Fruit
from utilities import SCREEN_LATTICE_X, SCREEN_LATTICE_Y


class Rule(ABC):
    @abstractmethod
    def check_rule(self, game: Game, snake: Snake, fruit: Fruit):
        pass


class SneakEatFruit(Rule):
    def check_rule(self, game: Game, snake: Snake, fruit: Fruit):
        if snake.get_head() == fruit.get_position():
            snake.eat()
            game.add_score(fruit.points)
            fruit.random_position()


class DieOnBorders(Rule):
    def check_rule(self, game: Game, snake: Snake, fruit: Fruit):
        head = snake.get_head()
        if head.x == SCREEN_LATTICE_X or head.x == -1:
            game.game_over()
        if head.y == SCREEN_LATTICE_Y or head.y == -1:
            game.game_over()


class DieSelfIntersect(Rule):
    def check_rule(self, game: Game, snake: Snake, fruit: Fruit):
        head = snake.get_head()
        if head in snake.body[:-1]:
            game.game_over()
