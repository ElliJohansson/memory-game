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


    def menu(self):
        pygame.display.set_caption("Menu")

        while self.running:

            self.screen.fill((255,255,255))
            pos = pygame.mouse.get_pos()

            play_button = Buttons(self.screen, "PLAY", 350, 100)
            play_button.draw_rect()

            exit_button = Buttons(self.screen, "EXIT", 350, 400)
            exit_button.draw_rect()

            score_button = Buttons(self.screen, "SCORES", 330, 250)
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

            back_button = Buttons(self.screen, "<-BACK", 30, 500)
            back_button.draw_rect()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if back_button.rect.collidepoint(pos):
                        self.menu()
                        
            pygame.display.update()
            memory_game.update(events, self.screen)



    def scores(self):

        pygame.display.set_caption("Scores")

        while self.running:

            self.screen.fill((255,255,255))
            pos = pygame.mouse.get_pos()

            back_button = Buttons(self.screen, "<-BACK", 30, 500)
            back_button.draw_rect()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(pos):
                        self.menu()

            pygame.display.update()