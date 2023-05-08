import pygame
from game_loops.memory_game import MemoryGame


def main():
    pygame.init()

    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Cat Memory Game")


    memory_game = MemoryGame()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        memory_game.update(events, screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
