import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(filename):
    """Load images that are used in the game tiles

    Args:
        filename: name of file containing the images

    Returns the loaded images.
    """
    return pygame.image.load(os.path.join(dirname, "pictures/cats", filename))
