import os
import random
import pygame
from sprites.tiles import Tiles


class MemoryGame:
    def __init__(self):

        self.tile_pairs = 6

        self.all_cats = os.listdir(os.path.join(os.getcwd(), "src/pictures"))
        self.image_width = 150
        self.image_height = 150
        self.borders = 5
        self.tiles_group = pygame.sprite.Group()
        self.flipped = []
        self.create_grid()

    def create_grid(self):
        self.cats = self.select_random_cats()
        self.generate_tiles(self.cats)

    def generate_tiles(self, cats):
        n = len(cats)
        cols = min(n, 4)
        rows = (n + cols - 1) // cols

        self.tiles_group.empty()

        for row in range(rows):
            for col in range(cols):
                i = row * cols + col
                if i >= n:
                    break
                x = col * (self.image_width + self.borders)
                y = row * (self.image_height + self.borders)
                tile = Tiles(cats[i], x, y)
                self.tiles_group.add(tile)

    def select_random_cats(self):
        cats = random.sample(self.all_cats, self.tile_pairs)
        cats *= 2
        random.shuffle(cats)
        return cats

    def update(self, events, screen):
        self.user_input(events)
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255, 255, 255))

        self.tiles_group.draw(screen)
        self.tiles_group.update()

    def user_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for tile in self.tiles_group:
                    if tile.rect.collidepoint(event.pos):
                        self.flipped.append(tile.name)
                        tile.show()
