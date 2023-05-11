import pygame
from load_image import load_image


class Tiles(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, id):
        """Args:
            filename: name of the file with a cat picture
            x: width of the cat picture
            y: heigth of the cat picture
        """
        super().__init__()

        self.name = filename.split(".")[0]
        self.cat_image = load_image(filename)
        self.flipped_image = load_image(filename)
        pygame.draw.rect(self.flipped_image, (0, 0, 0),
                         self.flipped_image.get_rect())

        self.image = self.flipped_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shown = False
        self.id = id

    def update(self):
        """Changes the image to a picture of a cat or a black square (tile's backside)
        """
        self.image = self.cat_image if self.shown else self.flipped_image

    def show(self):
        """Shows the picture side (cat) of the tile.
        """
        self.shown = True

    def hide(self):
        """Hides the picture side and shows a black tile.
        """
        self.shown = False
