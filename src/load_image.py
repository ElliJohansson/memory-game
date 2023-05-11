import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(filename):
    """a function that loads the images that are
    used in the game tiles
    """
    return pygame.image.load(os.path.join(dirname, "pictures/cats", filename))
