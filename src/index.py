import pygame
from game_loops.game_loop import GameLoop


def main():

    pygame.init()

    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))

    game = GameLoop(screen)
    game.run()


if __name__ == "__main__":
    main()
