import os
import random
import pygame
from sprites.tiles import Tiles
from game_logic.timer import Timer


class MemoryGame:
    """A class that contains the main game and it's logic.
    """

    def __init__(self):

        self.tile_pairs = 6
        self.fps = 60
        self.saved_score = 0
        self.matched = []

        self.timer = Timer()

        # getting the cat pictures
        self.all_cats = os.listdir(os.path.join(
            os.getcwd(), "src/pictures/cats"))
        self.image_width = 150
        self.image_height = 150
        self.borders = 5
        self.tiles_group = pygame.sprite.Group()

        # flipping and timing
        self.flipped = []
        self.block_game = False
        self.frame_count = 1
        self.create_grid()

    def create_grid(self):
        """Creates the grid with cat picture tiles.
        """
        self.cats = self.select_random_cats()
        self.generate_tiles(self.cats)

    def generate_tiles(self, cats):
        """Creates the level of the game, e.g. how many rows and
        columns of tiles there are.
        """
        n = len(cats)
        cols = min(n, 4)
        rows = (n + cols - 1) // cols

        # self.tiles_group.empty()

        for row in range(rows):
            for col in range(cols):
                i = row * cols + col
                if i >= n:
                    break
                x = col * (self.image_width + self.borders)
                y = row * (self.image_height + self.borders)
                tile = Tiles(cats[i], x, y, i)
                self.tiles_group.add(tile)

    def select_random_cats(self):
        """Selects a number of random pictures to use as the tiles 
        and multiplies it with two so there are matching pairs.
        Returns:
            A list of random cat pictures in a random order.
            """
        cats = random.sample(self.all_cats, self.tile_pairs)
        cats *= 2
        random.shuffle(cats)
        return cats

    def stop_timer(self):
        """Stops the timer and saves the time (score) in a variable.
        """
        if self.check_level_completion():
            if self.timer.timer_running:
                self.timer.saved_time = pygame.time.get_ticks() - self.timer.start_time
                self.saved_score = (self.timer.saved_time//1000)
                self.timer.timer_running = False

    def update(self, events, screen):
        """Args:
            events: list of events
            screen: display of application
        """
        self.user_input(events)
        self.draw(screen)
        self.timer.update()
        self.stop_timer()
        self.level_completion(screen)

    def draw(self, screen):
        """Draws the tiles and timer on a white screen.
        Args:
            screen: display of the application
        """
        screen.fill((255, 255, 255))

        self.tiles_group.draw(screen)
        screen.blit(self.timer.draw_timer(), (650, 10))
        self.tiles_group.update()

    def user_input(self, events):
        """Checks if game is blocked and forwards the actions to
        the appropriate method.
        Args:
            events: list of events
        """
        if not self.block_game:
            self.handle_mouse_clicks(events)
        else:
            self.handle_block_game()

    def handle_mouse_clicks(self, events):
        """Checks if user has clicked on the tiles.
        Args:
            events: list of events
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for tile in self.tiles_group:
                    if tile.rect.collidepoint(event.pos):
                        self.handle_tile_click(tile)

    def handle_tile_click(self, tile):
        """Shows clicked tile and checks if it is the second flipped tile.
        Args: 
            tile: game tile containing a picture of a cat
        """
        if tile.name not in self.matched:
            self.flipped.append(tile)
            tile.show()
            if len(self.flipped) == 2:
                self.handle_tile_pair()

    def handle_tile_pair(self):
        """Blocks the game if the flipped tiles aren't matching.
        """
        if self.flipped[0].name != self.flipped[1].name or self.flipped[0].id == self.flipped[1].id:
            self.block_game = True
        else:
            for tile in self.tiles_group:
                if tile.name == self.flipped[0].name:
                    self.matched.append(tile.name)
            self.flipped = []

    def handle_block_game(self):
        """Waits for one second and flips the unmatching tiles back.
        """
        self.frame_count += 1
        if self.frame_count == self.fps:
            self.frame_count = 0
            self.block_game = False

            for tile in self.tiles_group:
                if tile in self.flipped:
                    tile.hide()
            self.flipped = []

    def check_level_completion(self):
        """Checks if the level is completed, i.e. all tiles are shown.
        Returns:
            True if the level is completed, otherwise False.
        """
        num_shown_tiles = sum(tile.shown for tile in self.tiles_group)
        return num_shown_tiles == len(self.tiles_group)

    def level_completion(self, screen):
        """Displays a message after the level is completed.
        """
        completion_text = pygame.font.SysFont(
            "gentium", 30).render("Congrats!", True, (0, 0, 0))

        if self.check_level_completion():
            screen.blit(completion_text, (300, 500))
