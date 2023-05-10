import pygame
import pickle
from game_loops.memory_game import MemoryGame
from UI.buttons import Buttons


class GameLoop():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        # self.memory_game = MemoryGame()

    def draw_text(self, text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        self.screen.blit(img, (x, y))

    def menu(self):
        pygame.display.set_caption("Menu")

        while self.running:

            self.screen.fill((255, 255, 255))
            pos = pygame.mouse.get_pos()

            play_button = Buttons(self.screen, "PLAY", 40, 350, 100)
            play_button.draw_rect()

            exit_button = Buttons(self.screen, "EXIT", 40, 350, 400)
            exit_button.draw_rect()

            score_button = Buttons(self.screen, "SCORES", 40, 330, 250)
            score_button.draw_rect()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.rect.collidepoint(pos):
                        self.play()
                    if score_button.rect.collidepoint(pos):
                        self.scores()
                    if exit_button.rect.collidepoint(pos):
                        self.running = False

            pygame.display.update()

    def play(self):

        pygame.display.set_caption("Cat Memory Game")
        memory_game = MemoryGame()

        while self.running:

            pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            back_button = Buttons(self.screen, "<-BACK", 20, 5, 550)
            back_button.draw_rect()

            restart_button = Buttons(self.screen, "RESTART", 20, 300, 550)
            restart_button.draw_rect()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(pos):
                        self.menu()
                    if restart_button.rect.collidepoint(pos):
                        self.play()

            pygame.display.update()
            memory_game.update(events, self.screen)

    def scores(self):

        pygame.display.set_caption("Scores")

        """try:
            with open("score.dat", "rb") as file:
                saved_scores = pickle.load(file)
        except FileNotFoundError:
            saved_scores = []"""

        while self.running:

            self.screen.fill((255, 255, 255))
            pos = pygame.mouse.get_pos()

            back_button = Buttons(self.screen, "<-BACK", 20, 5, 550)
            back_button.draw_rect()

            #saved_scores.sort(reverse=True)
            """score_str = "Scores"
            for i, score in enumerate(saved_scores[:5]):
                score_str += f" {i+1}. {score} seconds,"
            score_str = score_str[:-1]

            score_text = pygame.font.SysFont(
                "gentium", 30).render(score_str, True, (0, 0, 0))
            self.screen.blit(score_text, (350, 300))

            y = 350
            for i, score in enumerate(saved_scores[:5]):
                score_text = pygame.font.SysFont("gentium", 30).render(f"{i+1}. {score}", True, (0, 0, 0))
                self.screen.blit(score_text, (350, y))
                y += 40"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(pos):
                        self.menu()

            pygame.display.update()
