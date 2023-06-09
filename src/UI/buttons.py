import pygame


class Buttons():
    """Class to make the clickable buttons in the UI.
    """

    def __init__(self, screen, text, size, x, y):

        self.font = pygame.font.SysFont("gentium", size)
        self.text_color = ((0, 0, 0))

        self.text = text
        self.screen = screen

        self.text_surface = self.font.render(text, True, self.text_color)
        self.text_width, self.text_heigth = self.font.size(text)

        self.rect_color = (249, 230, 230)
        self.rect_width = self.text_width + 20
        self.rect_heigth = self.text_heigth + 20

        self.rect = pygame.Rect(x, y, self.rect_width, self.rect_heigth)

        self.rect_surface = pygame.Surface((self.rect_width, self.rect_heigth))

    def draw_rect(self):
        """Draw rectangle around the button
        """
        self.rect_surface.fill(self.rect_color)
        self.rect_surface.blit(self.text_surface, (10, 10))
        self.screen.blit(self.rect_surface, self.rect)
