import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(filename):
    return pygame.image.load(os.path.join(dirname, "pictures", filename))
