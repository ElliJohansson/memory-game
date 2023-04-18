import pygame
from load_image import load_images


def create_grid(rows, cols):
    tile_size = 150

    tiles_rect = []
    tiles_images = []

    images = load_images((rows*cols)//2)

    image_index = 0

    for row in range(rows):
        row_tiles = []
        for col in range(cols):
            rect = pygame.Rect(col*tile_size, row*tile_size,
                               tile_size, tile_size)
            row_tiles.append(rect)
            tiles_images.append(images[image_index])
            image_index += 1
        tiles_rect.append(row_tiles)

    return tiles_rect, tiles_images

if __name__ == "__main__":
    asd = create_grid(2,2)
    print(asd[1])