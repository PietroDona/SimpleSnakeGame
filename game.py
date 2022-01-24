import pygame
from utilities import WHITE, BLUE, SCREEN_LATTICE_X, SCREEN_LATTICE_Y, SQUARE_SIZE


class Game():
    running = True
    speed = 10
    score = 0

    def game_over(self):
        self.running = False

    def add_score(self, points) -> None:
        self.score += points
        self.speed = 10 + self.score/100

    def draw_score(self, surface: pygame.Surface):
        font = pygame.font.SysFont("arial", 20)
        value = font.render(f"Score: {self.score}", True, WHITE)
        surface.blit(value, [0, 0])

    def draw_game_over(self, surface: pygame.Surface):
        surface.fill(BLUE)
        font = pygame.font.SysFont("arial", 40)
        text = font.render("GAME OVER", True, WHITE)
        text_rect = text.get_rect(
            center=(SQUARE_SIZE*SCREEN_LATTICE_X/2,
                    SQUARE_SIZE*SCREEN_LATTICE_Y/3))
        surface.blit(text, text_rect)

        score_text = font.render(f"Your score is {self.score}", True, WHITE)
        score_text_rect = score_text.get_rect(
            center=(SQUARE_SIZE*SCREEN_LATTICE_X/2,
                    SQUARE_SIZE*SCREEN_LATTICE_Y/2))
        surface.blit(score_text, score_text_rect)

        font = pygame.font.SysFont("arial", 20)
        info_text = font.render("press any key to exit", True, WHITE)
        info_text_rect = info_text.get_rect(
            center=(SQUARE_SIZE*SCREEN_LATTICE_X/2,
                    SQUARE_SIZE*SCREEN_LATTICE_Y*3/4))
        surface.blit(info_text, info_text_rect)
