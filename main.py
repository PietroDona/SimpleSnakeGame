import pygame
from utilities import SCREEN_LATTICE_X, SCREEN_LATTICE_Y, SQUARE_SIZE, BLUE
from utilities import direction
from game import Game
from snake import Snake
from fruit import Fruit
from rules import SneakEatFruit, DieOnBorders, DieSelfIntersect


def gameLoop():
    '''Main loop function'''
    # Initialize pygame
    pygame.init()
    game_surface = pygame.display.set_mode(
        size=(SCREEN_LATTICE_X*SQUARE_SIZE,
              SCREEN_LATTICE_Y*SQUARE_SIZE)
    )
    game_clock = pygame.time.Clock()
    # set windows title
    pygame.display.set_caption("Simple Snake Game")

    # Initialize the game
    game = Game()
    snake = Snake()
    fruit = Fruit()
    fruit.random_position()
    rules = [SneakEatFruit(), DieOnBorders(), DieSelfIntersect()]

    # Main loop
    while game.running:
        # Clear the screen
        game_surface.fill(BLUE)
        # Check for user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT and snake.velocity != direction.RIGHT):
                    snake.velocity = direction.LEFT
                if (event.key == pygame.K_RIGHT and snake.velocity != direction.LEFT):
                    snake.velocity = direction.RIGHT
                if (event.key == pygame.K_DOWN and snake.velocity != direction.UP):
                    snake.velocity = direction.DOWN
                if (event.key == pygame.K_UP and snake.velocity != direction.DOWN):
                    snake.velocity = direction.UP

        # Perform game actions
        snake.move()
        for rule in rules:
            rule.check_rule(game, snake, fruit)

        # Draw the objects on screen
        snake.draw_snake(game_surface)
        fruit.draw_fruit(game_surface)
        game.draw_score(game_surface)
        pygame.display.update()
        game_clock.tick(game.speed)

    # Render game over screen
    game.draw_game_over(game_surface)
    pygame.display.update()
    endgame = True
    while endgame:
        # Check for user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                endgame = False

    # Quit everything
    pygame.quit()
    quit()


if __name__ == "__main__":
    gameLoop()
