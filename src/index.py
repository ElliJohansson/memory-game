import pygame
from create_grid import create_grid


def main():
    pygame.init()
    pygame.display.set_caption("Cat Memory Game")

    running = True
    rows = 3
    cols = 4
    screen = pygame.display.set_mode((1280, 960))
    tiles_rect, tiles_images = create_grid(rows, cols)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        for row in range(rows):
            for col in range(cols):
                rect = tiles_rect[row][col]
                image = tiles_images[row * cols + col]
                screen.blit(image, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        pygame.display.flip()


if __name__ == "__main__":
    main()
