import pygame
from game_loops.memory_game import MemoryGame
from UI.buttons import Buttons


class GameLoop():
    def __init__(self, screen):
        self.screen = screen
        self.running = True


    def draw_text(self, text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        self.screen.blit(img, (x, y))


    def run(self):
        pygame.display.set_caption("Menu")

        while self.running:
            self.screen.fill((255,255,255))
            play_button = Buttons(self.screen, "PLAY", 350, 100)
            play_button.draw_rect()

            exit_button = Buttons(self.screen, "EXIT", 350, 400)
            exit_button.draw_rect()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.rect.collidepoint(pos):
                        self.play()
                    if exit_button.rect.collidepoint(pos):
                        self.running = False

            pos = pygame.mouse.get_pos()

            pygame.display.update()

    def play(self):

        pygame.display.set_caption("Cat Memory Game")
        memory_game = MemoryGame()

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.timer_running:
                        self.saved_time = pygame.time.get_ticks() - self.start_time
                        self.timer_running = False

            memory_game.update(events, self.screen)
            pygame.display.update()


