import pygame
import random
import os
#from load_image import load_images

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

def main():
    pygame.init()
    pygame.display.set_caption("Cat Memory Game")

    screen = pygame.display.set_mode((1280,960))

    tile_size = 150

    rows = 2
    cols = 3
    tiles_rect = []
    tiles_images = []

    images = load_images(3)

    image_index = 0
    
    for row in range(rows):
        row_tiles = []
        for col in range (cols):
            rect = pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size)
            row_tiles.append(rect)
            tiles_images.append(images[image_index])
            image_index += 1
        tiles_rect.append(row_tiles)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((255,255,255))
        for row in range(rows):
            for col in range(cols):
                rect = tiles_rect[row][col]
                image = tiles_images[row * cols + col]
                screen.blit(image, rect)
                pygame.draw.rect(screen, (0,0,0), rect, 2)
        pygame.display.flip()


if __name__ == "__main__":
    main()