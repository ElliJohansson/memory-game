import pygame
from load_image import load_image


class Tiles(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split(".")[0]
        self.cat_image = load_image(filename)
        self.flipped_image = load_image(filename)
        pygame.draw.rect(self.flipped_image, (0, 0, 0),
                         self.flipped_image.get_rect())

        self.image = self.flipped_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shown = False

    def update(self):
        self.image = self.cat_image if self.shown else self.flipped_image

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False
