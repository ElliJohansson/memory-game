import os
import random
import pygame

dirname = os.path.dirname(__file__)


def load_images(grid_size):
    image_list = []
    image_files = os.listdir(os.path.join(dirname, "pictures"))
    selected = random.sample(image_files, grid_size)

    for image_name in selected:
        file = pygame.image.load(os.path.join(dirname, "pictures", image_name))
        image_list.append(file)
        image_list.append(file)

    random.shuffle(image_list)

    return image_list
